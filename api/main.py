from fastapi import FastAPI

app = FastAPI()


@app.get("/information", status_code=200)
async def information() -> dict[str, str]:
    return {"status_code": "100", "message": "Continue"}


@app.get("/successful", status_code=200)
async def successful() -> dict[str, str]:
    return {"status_code": "200", "message": "OK"}


@app.get("/redirection", status_code=301)
async def redirection() -> dict[str, str]:
    return {"status_code": "301", "message": "Multiple Choices"}


@app.get("/client_error", status_code=400)
async def client_error() -> dict[str, str]:
    return {"status_code": "400", "message": "Bad Request"}


@app.get("/server_error", status_code=500)
async def server_error() -> dict[str, str]:
    return {"status_code": "500", "message": "Internal Server Error"}
