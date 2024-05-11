from sqlalchemy import func
from sql_alchemy import Grade, Student, Subject, Group, Base, Lecturer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased

engine = create_engine('sqlite:///example7.db', echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

l_lecturer = aliased(Lecturer)

query_result = session.query(
    Subject.subject_name,
    Subject.lecturer_id,
    l_lecturer.last_name
).join(
    l_lecturer,
    Subject.lecturer_id == l_lecturer.id
).group_by(
    Subject.subject_name
).all()

for row in query_result:
    print(row)
