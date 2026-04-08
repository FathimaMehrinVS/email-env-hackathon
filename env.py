class EmailEnv:
    def __init__(self):
        self.emails = [
            {"text": "Congratulations! You've won a $1000 gift card. Click here to claim.", "label": "spam"},
            {"text": "Meeting reminder: Project sync tomorrow at 10 AM in Room 402.", "label": "important"},
            {"text": "URGENT: Your account has been compromised. Reset your password now.", "label": "spam"}
        ]
        self.reset()

    def _get_obs(self):
        if self.done or self.current_index >= len(self.emails):
            return {"email": None}
        return {"email": self.emails[self.current_index]["text"]}

    def reset(self):
        self.current_index = 0
        self.done = False
        return self._get_obs()

    def step(self, action):
        if self.done:
            return self._get_obs(), 0.0, True, {}

        current_email = self.emails[self.current_index]
        reward = -1.0

        if current_email["label"] == "spam" and action == "delete":
            reward = 1.0
        elif current_email["label"] == "important" and action == "mark_important":
            reward = 1.0
        
        self.current_index += 1
        if self.current_index >= len(self.emails):
            self.done = True

        return self._get_obs(), reward, self.done, {}

    def state(self):
        return {
        "current_index": self.current_index,
        "done": self.done
         }