from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    position_id = Column(Integer())

    def __init__(self, first_name, last_name, position_id = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.position_id = position_id

    def __repr__(self):
        print(f''' 
              Name: {self.first_name} {self.last_name}
              Position: {self.position_id}
              ''')    

    # def add_user():
    #     pass

    # def edit_user():
    #     pass

    # @classmethod
    # def view_all(cls):
    #     pass

class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer(), primary_key=True)
    type = Column(String())
    date = Column(Integer())
    description = Column(String())
    tip_total = Column(Integer())
    is_active = Column(String())

    def __init__(self, type, description, date):
        self.type = type
        self.description = description
        self.date = date
        tip_total = 0
        is_active = True

    def __repr__(self):
        # this might be replaced with a query? tbd ... 
        print(f''' 
              Event Type: {self.type}
              Event Description: {self.description}
              Event Date: {self.date}
              Event is Active ? : {self.is_active}
              Event Staff: TBD  
              ''')   
         
    def close_out_event(self):
        pass

    # def create_event_schedule(self):
    #     pass

    # def edit_staff_schedule(self):
    #     pass

    # def print_staff_schedule(self):
    #     pass

    # @classmethod
    # def view_all(cls):
    #     pass

    # @classmethod
    # def view_all_open(cls):
    #     pass

    # @classmethod
    # def view_all_closed(cls):
    #     pass

class Positions(Base):
    __tablename__ = 'positions'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    tipout_percent = Column(Integer())

    def __init__(self, name):
        self.name = name
        self.tipout_percent = 0

    def __repr__(self):
        # this might be replaced with a query? tbd ... 
        print(f''' 
              Position Name : {self.name}
              Position Tipout Percentage : {self.tipout_percent}%
              ''')  

    # def edit_tipout(self):
    #     pass

    # def delete_position(self):
    #     pass

    # @classmethod
    # def view_all(cls):
    #     pass

    # @classmethod
    # def add_position(cls):
    #     pass



# Current Tasks: (no logic yet)
# ✔ step 1: set up classes -> tables -- find out about tips & schedule 
# ✔ step 1b: add seed data so I can test methods 
# ✔ step 2: set up class methods ? since we are using queries do we need methods? 
# ✔ step 3: set up instance methods ? since we are using queries do we need methods? 


# come back to whether or not i need to create classes for tips and schedule (i think i do)
