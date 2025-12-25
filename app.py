from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import random  # Temporary placeholder until model added

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoFrames(BaseModel):
    width: int
    height: int
    frames: list

@app.post("/analyze")
def analyze_video(data: VideoFrames):
    # TEMP: placeholder until AI model is connected
    # This gives a variable score based on resolution
    base = 50 if data.height < 1080 else 30
    score = random.randint(base, base + 20)

    return {
        "fake_probability": score,
        "model": "MesoNet (cloud pending)",
        "note": "Cloud version active. AI model integration next step."
    }

# Local run option (Railway ignores)
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
