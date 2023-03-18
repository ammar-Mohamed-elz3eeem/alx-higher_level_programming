#!/usr/bin/python3
"""
get states from states table that contain char a on its name
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ))
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    sess = Session()
    states = sess.query(State).filter(State.name.contains('a')).\
        order_by(State.id).all()
    [print("{}: {}".format(state.id, state.name))
        for state in states]
