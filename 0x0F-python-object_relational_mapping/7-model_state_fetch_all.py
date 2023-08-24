#!/usr/bin/python3
"""fetch data using sqlalchemy"""

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
    for instance in session.query(State).order_by(State.id).all():
        print("{}: {}".format(instance.id, instance.name))
