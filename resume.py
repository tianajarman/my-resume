from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/courses')
def courses():
    courses = [
        'MISY 225: Introduction to Programming Business Applications',
        'MISY 330: Database Design & Implementation',
        'BUAD 306: Service & Operations Management',
        'CISC 355: Computers, Ethics & Society',
        'ACCT 352: Law & Social Issues in Business'
    ]
    return render_template('courses.html', courses=courses)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
