from sqlalchemy import func
from sql_alchemy import Grade, Student, Subject, Group, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example7.db', echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


query_result = session.query(
    Grade.group_id_id, func.avg(Grade.grade).label('average_grade')
).group_by(Grade.group_id_id).all()


for row in query_result:
    print(row)
