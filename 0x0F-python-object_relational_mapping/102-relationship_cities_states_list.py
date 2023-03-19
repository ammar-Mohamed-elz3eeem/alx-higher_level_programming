#!/usr/bin/python3
"""
This module if for listing all cities
with thier corresponding state name
found in the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    sess = Session()
    data = sess.query(City).order_by(City.id).all()
    for row in data:
        print("{}: {} -> {}".format(row.id, row.name, row.state.name))
