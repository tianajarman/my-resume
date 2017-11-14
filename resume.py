from flask import Flask, render_template
app = Flask(__name__)


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
