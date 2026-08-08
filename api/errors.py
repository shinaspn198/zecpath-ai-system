from fastapi import Request
from fastapi.responses import JSONResponse


async def api_error_handler(request: Request, exc: Exception):

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "Internal server error",
            "path": request.url.path
        }
    )