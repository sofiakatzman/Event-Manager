from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    position_id = Column(Integer())

class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    date = Column(Integer())
    description = Column(String())
    tip_total = Column(Integer())
    is_active = Column(String())


class Positions(Base):
    __tablename__ = 'positions'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    tipout_percent = Column(Integer())




# Current Tasks: (no logic yet)
# step 1: set up classes -> tables -- find out about tips & schedule 
# step 2: set up class methods ? since we are using queries do we need methods? 
# step 3: set up instance methods ? since we are using queries do we need methods? 


# come back to whether or not i need to create classes for tips and schedule (i think i do)

