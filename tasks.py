def get_sample_emails():
    return [
        {"text": "Congratulations! You've won a $1000 gift card. Click here to claim.", "label": "spam"},
        {"text": "Meeting reminder: Project sync tomorrow at 10 AM in Room 402.", "label": "important"},
        {"text": "URGENT: Your account has been compromised. Reset your password now.", "label": "spam"}
    ]

def task_easy():
    return get_sample_emails(), ["delete", "mark_important", "delete"]

def task_medium():
    return get_sample_emails(), ["delete", "mark_important", "delete"]

def task_hard():
    return get_sample_emails(), ["delete", "mark_important", "delete"]

def grade_task(predicted_actions: list, expected_actions: list) -> float:
    if not expected_actions:
        return 0.0
    
    total = len(expected_actions)
    correct = sum(1 for p, e in zip(predicted_actions, expected_actions) if p == e)
    return correct / total
