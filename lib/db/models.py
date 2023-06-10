from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    position_id = Column(Integer(), ForeignKey('position.id'))  # this is a foreign key

    def __repr__(self):
        return f''' 
            ID: {self.id}
            Name: {self.first_name} {self.last_name}
            Position: {self.position_id}
        '''  

class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer(), primary_key=True)
    type = Column(String())
    date = Column(Integer())
    description = Column(String())
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f''' 
            Event ID : {self.id}
            Event Type: {self.type}
            Event Description: {self.description}
            Event Date: {self.date}
            Event is Active ? : {self.is_active}
            Event Staff: TBD  
        '''
         
    def close_out_event(self):
        pass


class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f''' 
            Position ID : {self.id}
            Position Name : {self.name}
        '''
    

class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column(Integer(), primary_key=True)
    event_id = Column(Integer(), ForeignKey("event.id")) # this is a foreign key 
    event_type = Column(String())
    staff_id = Column(Integer(), ForeignKey("staff.id")) # this is a foreign key 
    position_id = Column(Integer(), ForeignKey("position.id")) # this is a foreign key
    arrival_time = Column(Integer())

    def __repr__(self):
        return f''' 
                Event ID : {self.event_id}
                Event Type : {self.event_type}
                Staff ID : {self.staff_id}
                Position : {self.position_id}
                Arrival Time : {self.arrival_time}
        '''
        


