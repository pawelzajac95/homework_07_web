from sqlalchemy import func
from sql_alchemy import Student, Grade, Base, Subject, Group

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example7.db', echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

query_result = session.query(
    Grade.group_id_id,
    Group.group_name,
    func.avg(Grade.grade).label('average_grade')
).join(Group).filter(
    Grade.subject_id == 1
).group_by(
    Grade.group_id_id,
    Group.group_name
).all()

for row in query_result:
    print(row)
