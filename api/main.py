from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import JSONResponse

app = FastAPI()

# ステータスコードメッセージを定義
STATUS_MESSAGES = {
    "information": {
        100: "Continue",
        101: "Switching Protocols",
        102: "Processing",
        103: "Early Hints",
    },
    "successful": {
        200: "OK",
        201: "Created",
        202: "Accepted",
        203: "Non-Authoritative Information",
        204: "No Content",
        205: "Reset Content",
        206: "Partial Content",
        207: "Multi-Status",
        208: "Already Reported",
        226: "IM Used",
    },
    "redirection": {
        300: "Multiple Choices",
        301: "Moved Permanently",
        302: "Found",
        303: "See Other",
        304: "Not Modified",
        307: "Temporary Redirect",
        308: "Permanent Redirect",
    },
    "client_error": {
        400: "Bad Request",
        401: "Unauthorized",
        402: "Payment Required",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        406: "Not Acceptable",
        407: "Proxy Authentication Required",
        408: "Request Timeout",
        409: "Conflict",
        410: "Gone",
        411: "Length Required",
        412: "Precondition Failed",
        413: "Payload Too Large",
        414: "URI Too Long",
        415: "Unsupported Media Type",
        416: "Range Not Satisfiable",
        417: "Expectation Failed",
        418: "I'm a teapot",
        421: "Misdirected Request",
        422: "Unprocessable Entity",
        423: "Locked",
        424: "Failed Dependency",
        425: "Too Early",
        426: "Upgrade Required",
        428: "Precondition Required",
        429: "Too Many Requests",
        431: "Request Header Fields Too Large",
        451: "Unavailable For Legal Reasons",
    },
    "server_error": {
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout",
        505: "HTTP Version Not Supported",
        506: "Variant Also Negotiates",
        507: "Insufficient Storage",
        508: "Loop Detected",
        510: "Not Extended",
        511: "Network Authentication Required",
    },
}


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
