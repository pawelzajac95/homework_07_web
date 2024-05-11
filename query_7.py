from sql_alchemy import Grade, Student, Subject, Group, Base, Lecturer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased

engine = create_engine('sqlite:///example7.db', echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

query_result = session.query(
    Student.first_name,
    Student.last_name,
    Group.group_name,
    Subject.subject_name,
    Grade.grade
).join(
    Grade,
    Student.id == Grade.student_id
).join(
    Group,
    Student.group_id == Group.id
).join(
    Subject,
    Grade.subject_id == Subject.id
).order_by(
    Student.last_name,
    Student.first_name
).all()
