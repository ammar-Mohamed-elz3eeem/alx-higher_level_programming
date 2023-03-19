#!/usr/bin/python3
"""
Delete script using sqlalchemy ORM
"""


from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))

    Base.metadata.create_all(bind=engine)

    sess = Session(engine)
    new_state = State(name="California")

    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    sess.add(new_state)
    sess.commit()
    sess.close()
