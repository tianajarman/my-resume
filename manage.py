from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    jackson = Professor(name='Vincent E. Jackson II', department='Accounting & MIS')
    sharma = Professor(name='Pratyush Nidhi Sharma', department='Accounting & MIS')
    lynch = Professor(name='Thomas Gregory Lynch', department='Computer & Information Sciences')
    wang = Professor(name='Jiannan Wang', department='Accounting & MIS')
    course1 = Course(course_number= 'MISY 225', title='Introduction to Programming Business Applications', description='Learning to program in Java.', professor=jackson)
    course2 = Course(course_number='MISY 330', title='Database Design & Implementation', description='Learning data mining alogorithms and the SQL language.', professor=sharma)
    course3 = Course(course_number='CISC 355', title='Computers, Ethics & Society', description='Analyzing the impact of computers on our society.', professor=lynch)
    course4 = Course(course_number='MISY 350', title='Web Application Development', description='Fundamentals of web development, including Python and Flask.', professor=wang)
    db.session.add(jackson)
    db.session.add(sharma)
    db.session.add(lynch)
    db.session.add(wang)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
