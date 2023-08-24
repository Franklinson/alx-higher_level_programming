#!/usr/bin/python3
'''fetching data from the city and state class'''


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_and_city = session.query(City, State).order_by(City.id).\
        join(State, City.state_id == State.id).all()
    for city, state in state_and_city:
        print("{}:{} {}".format(state.name city.id city.name)
    session.close()
