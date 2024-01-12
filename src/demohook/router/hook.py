from db.crud import create_or_update_hook
from db.model.demo import get_db
from db.store import redis as redis_store
from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi.responses import ORJSONResponse
from logger import logger
from scheme.hook import HookDemo
from scheme.response import WebHookResponse
from sqlalchemy.orm import Session

hook_router = APIRouter()

def publish_to_next_level(hook: HookDemo):
    logger.debug("publish to next level")
    return

@hook_router.post("/hook1/", response_model=WebHookResponse, response_class=ORJSONResponse)
async def alarm(hook: HookDemo,  background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    response = WebHookResponse(
        code=200,
        label="success",
    )
    try:
        create_or_update_hook(db, hook)
        await redis_store.set_key(hook.id, hook.model_dump_json())
        background_tasks.add_task(publish_to_next_level, hook)
    except Exception as e:
        logger.error(e)
        response.code = 500
        response.label = "fail"

    return response