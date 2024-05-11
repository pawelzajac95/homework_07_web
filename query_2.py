from sqlalchemy import func
from sql_alchemy import Student, Grade, Base, Subject

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example7.db', echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

query_result = session.query(
    Student.id,
    Student.first_name,
    Student.last_name,
    Subject.subject_name,
    func.avg(Grade.grade).label('average_grade')
).join(Grade).join(Subject).filter(
    Grade.subject_id == 1
).group_by(
    Student.id,
    Student.first_name,
    Student.last_name,
    Subject.subject_name
).order_by(
    func.avg(Grade.grade).desc()
).all()

for row in query_result:
    print(row)
