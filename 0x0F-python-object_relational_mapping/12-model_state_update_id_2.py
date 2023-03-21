#!/usr/bin/python3
"""Start link class to table in database
"""


import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

from sqlalchemy import (create_engine)

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
    # Query to retrive
    state_to_update = session.query(State)\
        .where(State.id == 2)\
        .first()
    # Update the retrive record
    state_to_update.name = 'New Mexico'
    # Commit the update
    session.commit()
