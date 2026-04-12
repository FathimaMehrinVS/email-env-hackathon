import os
from openai import OpenAI
from env import EmailEnv
from dotenv import load_dotenv

# Load environment variables from .env file for local testing
load_dotenv()


API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN", "")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)


def get_action(obs):
    """Classifies an email based on subject, sender, and content."""
    email_text = obs.get("email")
    subject = obs.get("subject", "No Subject")
    sender = obs.get("sender", "Unknown Sender")

    if not email_text:
        return "ignore"
    
    prompt = f"""
    SENDER: {sender}
    SUBJECT: {subject}
    BODY: {email_text}
    """
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system", 
                    "content": "You are a professional email triage assistant. Classify the following email into exactly one of these labels: 'delete' (for spam, ads, or phishing), 'mark_important' (for work, urgent, or high-priority items), or 'ignore' (for notifications, generic updates, or neutral items). Return ONLY the label name."
                },
                {"role": "user", "content": prompt}
            ],
            max_tokens=20
        )
        action = response.choices[0].message.content.strip().lower()
        
        # Robust parsing of response
        for choice in ["delete", "mark_important", "ignore"]:
            if choice in action:
                return choice
        return "ignore"
        
    except Exception:
        # Improved rule-based fallback
        text = email_text.lower() + " " + subject.lower()
        if any(kw in text for kw in ["gift", "win", "lottery", "prize", "phish", "verify your account", "urgent: account locked"]):
            return "delete"
        elif any(kw in text for kw in ["boss", "meeting", "sync", "urgent", "security alert", "due tomorrow"]):
            return "mark_important"
        return "ignore"


def run_inference(task_name="easy"):
    """Runs the inference loop for a specific task."""
    env = EmailEnv(task_name=task_name)

    TASK_NAME = f"email_{task_name}"
    BENCHMARK = "email_env"
    MODEL_NAME = "smart-triage-agent"

    print(f"[START] task={TASK_NAME} env={BENCHMARK} model={MODEL_NAME}")

    obs = env.reset()
    done = False
    rewards = []
    step_count = 0

    while not done:
        action = get_action(obs)
        obs, reward, done, info = env.step(action)

        step_count += 1
        rewards.append(reward)

        print(
            f"[STEP] step={step_count} action={action} reward={reward:.2f} done={str(done).lower()} error=null"
        )

    total = len(rewards)
    correct = sum(1 for r in rewards if r == 1.0)
    score = correct / total if total > 0 else 0.0
    success = score > 0.5

    # --- HACKATHON COMPLIANCE CLIPPER ---
    # Rule: Score must be strictly between 0 and 1 (0.0 < score < 1.0)
    if score >= 1.0:
        score = 0.98
    elif score <= 0.0:
        score = 0.02
    # ------------------------------------

    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    print(
        f"[END] success={str(success).lower()} steps={step_count} score={score:.2f} rewards={rewards_str}"
    )
    return score


def run_all_tasks():
    """Runs inference across all difficulty levels to showcase versatility."""
    print("--- RUNNING MULTI-TASK EVALUATION ---")
    scores = []
    for difficulty in ["easy", "medium", "hard"]:
        score = run_inference(difficulty)
        scores.append(score)
    
    avg_score = sum(scores) / len(scores)
    print(f"--- OVERALL PERFORMANCE: {avg_score:.2f} ---")


if __name__ == "__main__":
    # By default, run all tasks for maximum visibility in logs
    run_all_tasks()