#!/usr/bin/python3
"""adds a new State object “Louisiana” to the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    get_state = session.query(State).filter(State.name == "Louisiana").first()
    print("{}".format(get_state.id))

    session.commit()
    session.close()
