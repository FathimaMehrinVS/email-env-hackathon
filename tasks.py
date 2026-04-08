def get_sample_emails():
    return [
        {"text": "Congratulations! You've won a $1000 gift card. Click here to claim.", "label": "spam"},
        {"text": "Meeting reminder: Project sync tomorrow at 10 AM in Room 402.", "label": "important"},
        {"text": "URGENT: Your account has been compromised. Reset your password now.", "label": "spam"}
    ]

def task_easy():
    emails = [
        {"text": "Win a free iPhone! Click here.", "label": "spam"},
        {"text": "Project meeting at 2pm.", "label": "important"},
        {"text": "Lunch today?", "label": "ignore"}
    ]
    return emails, ["delete", "mark_important", "ignore"]

def task_medium():
    emails = [
        {"text": "Congratulations on your recent purchase. Here is your receipt.", "label": "ignore"},
        {"text": "URGENT: Server down, please check.", "label": "important"},
        {"text": "Claim your gift card today!", "label": "spam"}
    ]
    return emails, ["ignore", "mark_important", "delete"]

def task_hard():
    emails = [
        {"text": "RE: Following up on our previous discussion regarding the sync.", "label": "important"},
        {"text": "Your account subscription will expire soon unless you renew.", "label": "ignore"},
        {"text": "Limited time offer: Get 90% off on all items.", "label": "spam"}
    ]
    return emails, ["mark_important", "ignore", "delete"]

def grade_task(predicted_actions: list, expected_actions: list) -> float:
    if not expected_actions:
        return 0.0
    
    total = len(expected_actions)
    correct = sum(1 for p, e in zip(predicted_actions, expected_actions) if p == e)
    return correct / total

