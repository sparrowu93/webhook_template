
from contextlib import asynccontextmanager

from fastapi import FastAPI
from logger import logger
from router.hook import hook_router


async def startup():
    logger.debug("Starting up...")
    

async def shutdown():
    logger.debug("Shutting down...")
    

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()
    yield
    await shutdown()

app = FastAPI(lifespan=lifespan)
app.include_router(hook_router, prefix="/hook")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
