from fastapi import FastAPI, status
from routes.task import router as task_router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from database import create_db_and_tables

app = FastAPI(title="Todo CRUD App")
app.include_router(task_router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
# Returns status code 400 - Bad Request for empty body and invalid path parameters
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.errors(), "body": exc.body},
    )
