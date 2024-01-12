
from db.model.demo import EventOrm
from scheme.hook import HookDemo as HookDemoScheme
from sqlalchemy.orm import Session


def create_or_update_hook(db: Session, alarm: HookDemoScheme):
    """
    创建或更新 DemoHook
    """
    demo_orm = EventOrm(
        **alarm.model_dump(by_alias=True)
    )
    db.merge(demo_orm)
    db.commit()
    # db.refresh(alarm_orm)
    return 
