#!/usr/bin/python3
"""prints the first State object from the database"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    first_state = session.query(State).order_by(State.id).first()
    if state:
        print('{0}: {1}'.format(state.id, state.name))
    else:
        print("Nothing")
