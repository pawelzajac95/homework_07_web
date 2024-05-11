from sqlalchemy import func
from sql_alchemy import Student, Grade, Base

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
    func.avg(Grade.grade).label('average_grade')
).join(Grade).group_by(
    Student.id,
    Student.first_name,
    Student.last_name
).order_by(
    func.avg(Grade.grade).desc()
).limit(5)

for row in query_result:
    print(row)
