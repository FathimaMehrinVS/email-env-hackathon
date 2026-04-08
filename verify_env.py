from env import EmailEnv

def test_email_env():
    env = EmailEnv()
    
    # Test reset
    obs = env.reset()
    print(f"Initial Observation: {obs}")
    assert "email" in obs
    assert obs["email"] == "Congratulations! You've won a $1000 gift card. Click here to claim."
    
    # Test step 1: Spam + delete -> 1.0 reward
    obs, reward, done, info = env.step("delete")
    print(f"Step 1: reward={reward}, done={done}, next_obs={obs}")
    assert reward == 1.0
    assert done == False
    
    # Test step 2: Important + mark_important -> 1.0 reward
    obs, reward, done, info = env.step("mark_important")
    print(f"Step 2: reward={reward}, done={done}, next_obs={obs}")
    assert reward == 1.0
    assert done == False
    
    # Test step 3: Spam + ignore -> -1.0 reward
    obs, reward, done, info = env.step("ignore")
    print(f"Step 3: reward={reward}, done={done}, next_obs={obs}")
    assert reward == -1.0
    assert done == True
    assert obs["email"] == None
    
    # Test state
    idx, is_done = env.state()
    print(f"State: index={idx}, done={is_done}")
    assert idx == 3
    assert is_done == True

    print("\nAll tests passed successfully!")

if __name__ == "__main__":
    test_email_env()
