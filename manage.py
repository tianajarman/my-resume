from flask_script import Manager
from resume import app, db, Professor

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    jackson = Professor(name='Vincent E. Jackson II', department='Accounting & MIS')
    sharma = Professor(name='Pratyush Nidhi Sharma', department='Accounting & MIS')
    lynch = Professor(name='Thomas Gregory Lynch', department='Computer & Information Sciences')
    wang = Professor(name='Jiannan Wang', department='Accounting & MIS')
    db.session.add(jackson)
    db.session.add(sharma)
    db.session.add(lynch)
    db.session.add(wang)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
