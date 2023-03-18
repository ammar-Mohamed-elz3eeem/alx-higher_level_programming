#!/usr/bin/python3
"""Start link class to table in database
"""


import sys
from sqlalchemy.ext.declarative import declarative_base
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
    state = sess.query(State).order_by(State.id).first()
    print("{}: {}".format(state.id, state.name))
    sess.close()
