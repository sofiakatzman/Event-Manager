from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    position_id = Column(Integer(), ForeignKey('positions.id'))  # this is a foreign key

    def __init__(self, first_name, last_name, position_id = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.position_id = position_id

    def __repr__(self):
        return f''' 
            Name: {self.first_name} {self.last_name}
            Position: {self.position_id}
        '''  

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
            Event Tip Total : {self.tip_total}
            Event Staff: TBD  
        '''
         
    def close_out_event(self):
        pass


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
    

class Tips(Base):
    __tablename__ = 'tips'

    id = Column(Integer(), primary_key=True)
    event_id = Column(Integer(), ForeignKey("events.id")) # this is a foreign key 
    user_id = Column(Integer(), ForeignKey("users.id")) # this is a foreign key
    tipout_amount = Column(Integer())
    check_number = Column(Integer()) 

    def __init__(self, event_id, user_id):
        self.event_id = event_id  
        self.user_id = user_id  
        self.tipout_amount = 0
        self.check_number = "NOT PAID"

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
    event_id = Column(Integer(), ForeignKey("events.id")) # this is a foreign key 
    event_type = Column(String())
    user_id = Column(Integer(), ForeignKey("users.id")) # this is a foreign key 
    position_id = Column(Integer(), ForeignKey("positions.id")) # this is a foreign key
    arrival_time = Column(Integer())

    def __init__(self, event_id, event_type, user_id, position_id, arrival_time):
        self.event_id = event_id  
        self.event_type = event_type
        self.user_id = user_id   
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
        













# Current Tasks: (no logic yet)
# ✔ 
# ✔ add schemas for tips and schedule 
# ✔ add repr methods for each Class
# work on many-to-many relationships / associations on my tips and schedule tables
# seed tips, schedule, and events tables
# --> at this point I can begin building out the CLI component with my data 
#  

# Removed Code: 
# Users
    # def add_user():
    #     pass

    # def edit_user():
    #     pass

    # @classmethod
    # def view_all(cls):
    #     pass
# Events
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
# Positions
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


