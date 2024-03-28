if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    import uvicorn

    load_dotenv()
    port = os.getenv("API_PORT", 8000)

    uvicorn.run(
        "src.server.main:app",
        port=int(port),
        reload=True,
        reload_dirs=["src/server"],
    )