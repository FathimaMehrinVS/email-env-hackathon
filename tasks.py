def get_all_emails():
    """Returns a full bank of emails for various tasks."""
    return {
        "easy": [
            {"sender": "notifications@bank.com", "subject": "Monthly Statement Available", "text": "Your monthly bank statement for April is now available for download.", "label": "ignore"},
            {"sender": "boss@company.com", "subject": "URGENT: Meeting moved to 9AM", "text": "The project sync has been moved up. Please be there on time.", "label": "mark_important"},
            {"sender": "win-prizes@spam.net", "subject": "YOU WON A NEW IPHONE!", "text": "Click here immediately to claim your free iPhone 15 Pro Max!", "label": "delete"},
            {"sender": "hr@company.com", "subject": "Open Enrollment for Benefits", "text": "Please review the attached documents for your health insurance renewal.", "label": "mark_important"},
            {"sender": "newsletter@tech.com", "subject": "Weekly Tech Digest", "text": "Here are the top 10 stories in tech this week.", "label": "ignore"},
            {"sender": "phisher@fake-login.com", "subject": "Security Alert: Verify your account", "text": "Your account has been locked. Click here to verify your identity.", "label": "delete"}
        ],
        "medium": [
            {"sender": "colleague@work.com", "subject": "Quick question about the spreadsheet", "text": "Hey, which tab has the Q3 projections? Thanks!", "label": "mark_important"},
            {"sender": "no-reply@amazon.com", "subject": "Your order has shipped", "text": "Your package is on its way and will arrive tomorrow.", "label": "ignore"},
            {"sender": "deals@travel-deals.com", "subject": "90% off Phuket flights!", "text": "Unbelievable prices for next summer. Book now!", "label": "delete"},
            {"sender": "it-support@company.com", "subject": "Mandatory Password Reset", "text": "Company policy requires a password reset every 90 days. Please use the intranet portal.", "label": "mark_important"},
            {"sender": "linkedin@notifications.com", "subject": "You have 3 new connection requests", "text": "Check out who wants to connect with you on LinkedIn.", "label": "ignore"},
            {"sender": "suspicious@unknown.ru", "subject": "Invoice_9921_Attached", "text": "Please see the attached invoice for your recent payment of $4,500.", "label": "delete"}
        ],
        "hard": [
            {"sender": "partner@consultancy.com", "subject": "RE: Following up on our previous discussion", "text": "I've reviewed the documents you sent. Let's touch base on Thursday to finalize.", "label": "mark_important"},
            {"sender": "system@github.com", "subject": "[Security] Dependabot alert for your repo", "text": "A high-severity vulnerability was found in one of your dependencies.", "label": "mark_important"},
            {"sender": "marketing@local-gym.com", "subject": "We miss you! Come back for 1 month free", "text": "Renew your membership today and get the first month on us.", "label": "ignore"},
            {"sender": "admin@university-portal.edu", "subject": "Your library books are overdue", "text": "Please return the books listed below to avoid further fines.", "label": "ignore"},
            {"sender": "noreply@lottery-winner.com", "subject": "Notification of Cash Prize", "text": "You are the selected winner of our grand prize of $1,000,000.", "label": "delete"},
            {"sender": "stranger@gmail.com", "subject": "Hello from an old friend", "text": "I found your email address in my old address book. Remember me?", "label": "delete"}
        ]
    }

def get_task_data(task_name="easy"):
    all_data = get_all_emails()
    emails = all_data.get(task_name, all_data["easy"])
    # The actions stay the same as per user request
    allowed_actions = ["delete", "mark_important", "ignore"]
    return emails, allowed_actions

def grade_task(predicted_actions: list, expected_actions: list) -> float:
    if not expected_actions:
        return 0.0
    total = len(expected_actions)
    correct = sum(1 for p, e in zip(predicted_actions, expected_actions) if p == e)
    return correct / total
