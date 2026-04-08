from fastapi import FastAPI
from env import EmailEnv

app = FastAPI()

env = EmailEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs}

@app.post("/step")
def step(action: dict):
    act = action.get("action")
    obs, reward, done, info = env.step(act)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/")
def root():
    return {"message": "Email Env is running"}