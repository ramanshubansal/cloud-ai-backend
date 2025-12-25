from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS so Chrome Extension can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Server running"}

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    frames = data.get("frames", [])

    # Dummy prediction for now
    score = 30 + (len(frames) % 60)

    return {
        "success": True,
        "fake_probability": score,
        "frames_received": len(frames)
    }

