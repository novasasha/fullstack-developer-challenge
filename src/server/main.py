if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:app",
        port=8000,
        reload=True,
    )