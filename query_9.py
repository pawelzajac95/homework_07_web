from sql_alchemy import Grade, Student, Subject, Group, Base, Lecturer
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased

engine = create_engine('sqlite:///example7.db', echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


query_result = session.query(
    Subject.lecturer_id,
    Subject.subject_name,
    func.avg(Grade.grade).label('average_grade')
).join(
    Grade,
    Subject.id == Grade.subject_id
).join(
    Lecturer,
    Subject.lecturer_id == Lecturer.id
).group_by(
    Subject.lecturer_id
).all()

for row in query_result:
    print(row)
