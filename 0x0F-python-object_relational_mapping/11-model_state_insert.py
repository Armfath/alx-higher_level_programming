#!/usr/bin/python3
"""Start link class to table in database
"""


import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

from sqlalchemy import create_engine, bindparam, select

if __name__ == "__main__":
    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create the database schema
    Base.metadata.create_all(engine)
    # Create a sessionmaker to interact with the database
    Session = sessionmaker(bind=engine)
    # Open a session
    session = Session()
    # Create new state
    new_state = State(name='Louisiana')
    # Add new_state to the engine
    session.add(new_state)
    # Commit the add
    session.commit()
    # Print data
    most_recent_state = session.query(State)\
        .order_by(State.id.desc()).first()
    print(most_recent_state.id)
