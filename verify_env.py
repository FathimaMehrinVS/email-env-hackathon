from env import EmailEnv

def test_easy_task():
    print("Testing Easy Task...")
    env = EmailEnv(task_name="easy")
    obs = env.reset()
    
    # Check fields
    assert "email" in obs and "subject" in obs and "sender" in obs
    assert obs["sender"] == "notifications@bank.com"
    
    # Statement -> ignore
    obs, reward, done, info = env.step("ignore")
    assert reward == 1.0
    
    # Urgent meeting -> mark_important
    obs, reward, done, info = env.step("mark_important")
    assert reward == 1.0
    
    print("Easy task logic verified.")

def test_hard_task():
    print("\nTesting Hard Task...")
    env = EmailEnv(task_name="hard")
    obs = env.reset()
    assert obs["sender"] == "partner@consultancy.com"
    
    # Consulting follow up -> mark_important
    _, reward, _, _ = env.step("mark_important")
    assert reward == 1.0
    print("Hard task logic verified.")

def test_inference_readiness():
    print("\nTesting Inference Compatibility...")
    from inference import get_action
    
    # Mock observation
    mock_obs = {
        "email": "WIN A PRIZE NOW",
        "subject": "SPECIAL OFFER",
        "sender": "spam@ext.net"
    }
    
    # Test the logic (Rule-based fallback should catch this as 'delete' if LLM fails)
    action = get_action(mock_obs)
    print(f"Inference returned action: {action}")
    assert action in ["delete", "mark_important", "ignore"]
    print("Inference readiness verified.")

if __name__ == "__main__":
    try:
        test_easy_task()
        test_hard_task()
        test_inference_readiness()
        # Removed emoji for Windows compatibility
        print("\n[SUCCESS] ALL LOCAL SYSTEM TESTS PASSED!")
    except Exception as e:
        print(f"\n[FAILURE] TEST FAILED: {str(e)}")
        import traceback
        traceback.print_exc()
        exit(1)
