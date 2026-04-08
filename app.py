from fastapi import FastAPI
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
    uvicorn.run("app:app", host="0.0.0.0", port=7860)

def main():
    run_inference()

if __name__ == "__main__":
    main()