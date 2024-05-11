from connect_db import session
from sql_alchemy import Student, Group, Lecturer, Subject, Grade
import random
from faker import Faker
from datetime import date, timedelta

fake = Faker()

groups = ['Grupa A', 'Grupa B', 'Grupa C']
for group_name in groups:
    group = Group(group_name=group_name)
    session.add(group)
    session.commit()

subjects = ['Matematyka', 'Fizyka', 'Chemia', 'Informatyka',
            'Historia', 'Biologia', 'Język angielski']
lecturer_ids = list(range(1, 5))

for subject_name in subjects:
    lecturer_id = random.choice(lecturer_ids)
    subject = Subject(subject_name=subject_name, lecturer_id=lecturer_id)
    session.add(subject)
    session.commit()


for _ in range(40):
    first_name = fake.first_name()
    last_name = fake.last_name()
    group_id = random.randint(1, 3)
    student = Student(first_name=first_name,
                      last_name=last_name, group_id=group_id)
    session.add(student)
    session.commit()

    for _ in range(4):
        first_name = fake.first_name()
        last_name = fake.last_name()
        lecturer = Lecturer(first_name=first_name, last_name=last_name)
        session.add(lecturer)
        session.commit()

    students_ids = list(range(1, 41))
    subjects_ids = list(range(1, 8))

    for student_id in students_ids:
        for subject_id in subjects_ids:
            for _ in range(20):
                grade = round(random.uniform(2, 5), 2)
                date_given = fake.date_between(
                    start_date='-1y', end_date=date.today())

                group_id = random.randint(1, 3)
                new_grade = Grade(student_id=student_id, subject_id=subject_id, group_id=group_id, grade=grade,
                                  date_given=date_given)
                session.add(new_grade)
                session.commit()
