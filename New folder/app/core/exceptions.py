from fastapi import FastAPI,Request,status
from fastapi.responses import JSONResponse



def register_exception_handlers(app:FastAPI):
    @app.add_exception_handler(Exception)
    async def undaled_exceptional_handler(request:Request,exc:Exception):
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,CONTENT={'detail':str(exc)})
    



