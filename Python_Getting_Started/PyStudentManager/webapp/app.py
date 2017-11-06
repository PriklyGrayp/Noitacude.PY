__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

from flask import Flask, render_template, redirect, url_for, request

from students import Students

students = []

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def students_page():
    if request.method == 'POST':
        school_name = request.form.get('E or H school', '')
        new_student_name = request.form.get('name', '')
        new_student_id = request.form.get('id', '')

        new_student = Students(school_name = school_name, student_name = new_student_name, student_id = new_student_id)
        students.append(new_student)

        return redirect(url_for('students_page'))

    return render_template('index.html', students = students)


if __name__ == '__main__':
    app.run(debug=True)