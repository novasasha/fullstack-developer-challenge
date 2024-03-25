from fastapi import FastAPI
from data.messages import messages
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/messages")
async def read_messages():
    return {
        "messages": messages,
        "count": len(messages),
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        port=8000,
    )