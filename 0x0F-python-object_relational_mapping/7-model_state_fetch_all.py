#!/usr/bin/python3
'''fetching data using sqlalchemy'''


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine =create_engine( "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))

    Session = sessionmarker(bind=engine)

    session = Session()

    for state in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(state.id, state.name))
