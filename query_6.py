
from sql_alchemy import Grade, Student, Subject, Group, Base, Lecturer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased

engine = create_engine('sqlite:///example7.db', echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

query_result = session.query(
    Student.group_id,
    Student.id
).order_by(
    Student.group_id.asc()
).all()

for row in query_result:
    print(row)
