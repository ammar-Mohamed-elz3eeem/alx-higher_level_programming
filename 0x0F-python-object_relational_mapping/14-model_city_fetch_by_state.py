#!/usr/bin/python3
"""
Delete script using sqlalchemy ORM
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1],
        argv[2],
        argv[3]
    ), echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    data = sess.query(City, State.name).join(State).order_by(City.id).all()
    [print("{}: ({}) {}".format(
        row[1],
        row[0].id,
        row[0].name
        )) for row in data]
