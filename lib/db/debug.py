from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import (Users, Events, Positions, Schedules, Tips)

if __name__ == '__main__':
    engine = create_engine("sqlite:///event_manager.db")
    session = Session(engine, future=True)

    import ipdb; ipdb.set_trace()