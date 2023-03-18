#!/usr/bin/python3
"""
Delete script using sqlalchemy ORM
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
    rows = sess.query(State).filter(State.name.contains('a'))
    [sess.delete(row) for row in rows]
    sess.commit()
    data = sess.query(State)

    [print("{}: {}".format(row.id, row.name))
     for row in data]
    sess.close()
