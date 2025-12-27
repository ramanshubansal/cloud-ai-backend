from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows any extension to call it
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_video(data: dict):
    # 'data' will contain your 'frames' list
    return {
        "success": True, 
        "fake_probability": 0.15, 
        "frames_received": len(data.get("frames", []))
    }
