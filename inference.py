import os
from openai import OpenAI
from env import EmailEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN", "")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)


def get_action(email_text):
    if not email_text:
        return "ignore"
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Classify this email. Return ONLY one of: delete, mark_important, ignore."},
                {"role": "user", "content": email_text}
            ],
            max_tokens=10
        )
        action = response.choices[0].message.content.strip().lower()
        # Ensure only the required words are returned
        if "delete" in action:
            return "delete"
        elif "mark_important" in action:
            return "mark_important"
        elif "ignore" in action:
            return "ignore"
        return "ignore"
    except Exception:
        # Rule-based fallback if API fails
        text = email_text.lower()
        if any(kw in text for kw in ["congratulations", "urgent", "gift"]):
            return "delete"
        elif any(kw in text for kw in ["meeting", "reminder"]):
            return "mark_important"
        return "ignore"


def run_inference():
    env = EmailEnv()

    TASK_NAME = "email_task"
    BENCHMARK = "email_env"
    MODEL_NAME = "simple-agent"

    # START log
    print(f"[START] task={TASK_NAME} env={BENCHMARK} model={MODEL_NAME}")

    obs = env.reset()
    done = False
    rewards = []
    step_count = 0

    while not done:
        email_text = obs.get("email")

        if email_text is None:
            break

        action = get_action(email_text)

        obs, reward, done, info = env.step(action)

        step_count += 1
        rewards.append(reward)

        # STEP log (STRICT FORMAT)
        print(
            f"[STEP] step={step_count} action={action} reward={reward:.2f} done={str(done).lower()} error=null"
        )

    # Score calculation
    total = len(rewards)
    correct = sum(1 for r in rewards if r == 1.0)
    score = correct / total if total > 0 else 0.0

    success = score > 0.5

    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    # END log (STRICT FORMAT)
    print(
        f"[END] success={str(success).lower()} steps={step_count} score={score:.2f} rewards={rewards_str}"
    )

if __name__ == "__main__":
    run_inference()