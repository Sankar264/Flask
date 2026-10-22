from flask import Flask, render_template

app = Flask(__name__)

# Each student record contains id, name, and marks percentage.
students = [
    {"id": 1, "name": "Ananya", "percentage": 92},
    {"id": 2, "name": "Bharath", "percentage": 84},
    {"id": 3, "name": "Charan", "percentage": 78},
    {"id": 4, "name": "Divya", "percentage": 67},
    {"id": 5, "name": "Eshwar", "percentage": 88},
    {"id": 6, "name": "Farah", "percentage": 73},
    {"id": 7, "name": "Gokul", "percentage": 59},
    {"id": 8, "name": "Harini", "percentage": 81},
    {"id": 9, "name": "Ishaan", "percentage": 46},
    {"id": 10, "name": "Jyothi", "percentage": 95}
]

def calculate_grade(percentage):
    if percentage > 80:
        return "A"
    elif percentage > 70:
        return "B"
    elif percentage > 60:
        return "C"
    elif percentage > 50:
        return "D"
    else:
        return "F"

@app.route('/')
def home():
    for student in students:
        student["grade"] = calculate_grade(student["percentage"])
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
