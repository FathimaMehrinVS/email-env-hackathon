from tasks import get_task_data

class EmailEnv:
    def __init__(self, task_name="easy"):
        self.task_name = task_name
        self.emails, self.allowed_actions = get_task_data(self.task_name)
        self.reset()

    def _get_obs(self):
        if self.done or self.current_index >= len(self.emails):
            return {"email": None, "subject": None, "sender": None}
        
        current_email = self.emails[self.current_index]
        return {
            "email": current_email["text"],
            "subject": current_email["subject"],
            "sender": current_email["sender"]
        }

    def reset(self, task_name=None):
        if task_name:
            self.task_name = task_name
            self.emails, self.allowed_actions = get_task_data(self.task_name)
            
        self.current_index = 0
        self.done = False
        return self._get_obs()

    def step(self, action):
        if self.done:
            return self._get_obs(), 0.0, True, {}

        if self.current_index >= len(self.emails):
            self.done = True
            return self._get_obs(), 0.0, True, {}

        current_email = self.emails[self.current_index]
        reward = -1.0

        # Logic for selection
        if current_email["label"] == action:
            reward = 1.0
        
        self.current_index += 1
        if self.current_index >= len(self.emails):
            self.done = True

        return self._get_obs(), reward, self.done, {"task": self.task_name}

    def state(self):
        return {
            "current_index": self.current_index,
            "done": self.done,
            "task": self.task_name
        }