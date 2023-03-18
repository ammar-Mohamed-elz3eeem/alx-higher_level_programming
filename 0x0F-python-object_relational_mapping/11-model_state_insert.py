#!/usr/bin/python3
"""
search for a state in the states table
"""


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1],
        argv[2],
        argv[3]
    ))
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    state = State(name="Louisiana")
    sess.add(state)
    sess.commit()

    state_id = sess.query(State.id).filter(State.name == 'Louisiana').one()
    print(state_id.id)
    sess.close()
