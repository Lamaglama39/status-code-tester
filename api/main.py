from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import JSONResponse
from .status_messages import STATUS_MESSAGES

app = FastAPI()


async def get_status_message(category: str, status_code: int):
    messages = STATUS_MESSAGES.get(category)
    if messages and status_code in messages:
        return JSONResponse(status_code=status_code, content={"status_code": status_code, "message": messages[status_code]})
    raise HTTPException(status_code=404, detail="不正なステータスコード")


@app.get("/information/{status_code}")
async def information(status_code: int = Path(..., description="ステータスコード")):
    return await get_status_message("information", status_code)


@app.get("/successful/{status_code}")
async def successful(status_code: int = Path(..., description="ステータスコード")):
    return await get_status_message("successful", status_code)


@app.get("/redirection/{status_code}")
async def redirection(status_code: int = Path(..., description="ステータスコード")):
    return await get_status_message("redirection", status_code)


@app.get("/client_error/{status_code}")
async def client_error(status_code: int = Path(..., description="ステータスコード")):
    return await get_status_message("client_error", status_code)


@app.get("/server_error/{status_code}")
async def server_error(status_code: int = Path(..., description="ステータスコード")):
    return await get_status_message("server_error", status_code)
