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
        return f''' 
            Name: {self.first_name} {self.last_name}
            Position: {self.position_id}
        '''  

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
        return f''' 
            Event Type: {self.type}
            Event Description: {self.description}
            Event Date: {self.date}
            Event is Active ? : {self.is_active}
            Event Staff: TBD  
        '''
         
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
        return f''' 
            Position Name : {self.name}
            Position Tipout Percentage : {self.tipout_percent}%
        '''

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





class Tips(Base):
    __tablename__ = 'tips'

    id = Column(Integer(), primary_key=True)
    event_id = Column(Integer()) # this is a foreign key / proxy association 
    user_id = Column(Integer()) # this is a foreign key / proxy association 
    tipout_amount = Column(Integer())
    check_number = Column(Integer()) 

    def __init__(self, event_id, user_id, tipout_amount, check_number="NOT PAID"):
        self.event_id = event_id  # this is a foreign key / proxy association 
        self.user_id = user_id  # this is a foreign key / proxy association 
        self.tipout_amount = tipout_amount
        self.check_number = check_number

    def __repr__(self):
        return f''' 
                Event ID : {self.event_id}
                User ID : {self.user_id}
                Tipout Amount : {self.tipout_amount}
                Check Number : {self.check_number}
            ''' 
        

class Schedules(Base):
    __tablename__ = 'schedules'

    id = Column(Integer(), primary_key=True)
    event_id = Column(Integer()) # this is a foreign key / proxy association 
    event_type = Column(String())
    user_id = Column(Integer()) # this is a foreign key / proxy association 
    position_id = Column(Integer()) # this is a foreign key / proxy association 
    arrival_time = Column(Integer())

    def __init__(self, event_id, event_type, user_id, position_id, arrival_time):
        self.event_id = event_id  # this is a foreign key / proxy association 
        self.event_type = event_type
        self.user_id = user_id  # this is a foreign key / proxy association 
        self.position_id = position_id
        self.arrival_time = arrival_time

    def __repr__(self):
        return f''' 
                Event ID : {self.event_id}
                Event Type : {self.event_type}
                User ID : {self.user_id}
                Position : {self.position_id}
                Arrival Time : {self.arrival_time}
        '''
        # return f'{self.event_id, self.event_type, self.user_id, self.position_id, self.arrival_time}'
        
              
        
        
        
        
# Current Tasks: (no logic yet)
# ✔ 
# ✔ add schemas for tips and schedule 
# ✔ add print methods for each Class
# work on many-to-many relationships / associations on my tips and schedule tables
# seed tips, schedule, and events tables 





# come back to whether or not i need to create classes for tips and schedule (i think i do)