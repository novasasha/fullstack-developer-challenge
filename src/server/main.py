from fastapi import FastAPI
from data.messages import messages

app = FastAPI()

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