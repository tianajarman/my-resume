import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


class Professor(db.Model):
    __tablename__ = 'professors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    department = db.Column(db.Text)
    courses = db.relationship('Course', backref='professor')


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.Integer)
    title = db.Column(db.String(256))
    description = db.Column(db.Text)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))


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


@app.route('/professor')
def show_all_professors():
    professors = Professor.query.all()
    return render_template('professor-all.html', professors=professors)


if __name__ == '__main__':
    app.run()
