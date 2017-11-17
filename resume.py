import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


class Professor(db.Model):
    __tablename__ = 'professors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    department = db.Column(db.String(64))
    courses = db.relationship('Course', backref='professor')


class Course(db.Model):
    __tablename__ = 'courses'
    course_numer = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(64))
    professor_id = db.Column(db.Integer, db.ForeignKey(professors.id))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/courses')
def courses():
    courses = [
        ['MISY225', 'Introduction to Programming Business Applications',
            'Learning to program in Java.'],
        ['MISY330', 'Database Design & Implementation',
            'Learning data mining alogorithms and the SQL language'],
        ['CISC355', 'Computers, Ethics & Society',
            'Analyzing the impact of computers on our society.'],
        ['MISY350', 'Web Application Development',
            'Fundamentals of web development, including Python and Flask.']
    ]
    return render_template('courses.html', courses=courses)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
