import os
import sys
from fastapi import FastAPI

# Add the parent directory to sys.path to allow importing root-level modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from env import EmailEnv
from inference import run_inference

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

def start_server():
    import uvicorn
    # Now that app is in the server package, we need the full import path
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

def main():
    run_inference()

if __name__ == "__main__":
    main()