import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .data.messages import init as init_messages, reset as reset_messages
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)
import sqlite3

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Seeding db...")
    init_messages()
    logger.info("DB seeded")
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/messages")
async def read_messages(offset: int = 0, limit: int = 10):
    connection = sqlite3.connect('messages.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM messages LIMIT ? OFFSET ?', (limit, offset))
    messages = cursor.fetchall()

    # get count of all messages
    cursor.execute('SELECT COUNT(*) FROM messages')
    count = cursor.fetchone()[0]

    connection.close()

    return {
        "messages": messages,
        "count": count,
        "offset": offset,
        "limit": limit,
    }


@app.post("/reset", status_code=204)
async def reset():
    reset_messages()
    init_messages()
