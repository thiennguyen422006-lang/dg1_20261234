import json
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/api/health")
def health():
    return {"status": "OK", "mssv": "20261234"}

@app.route("/")
@app.route("/api/student")
@app.route("/api/students")
def student_list():
    students = [
        {"mssv": "20261234", "name": "Nguyen Duc Thien", "class": "DG1"}
    ]
    
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Danh sach Sinh vien</title>
    </head>
    <body>
        <h1>Danh sach Sinh vien</h1>
        <ul>
        {% for student in students %}
            <li>MSSV: {{ student.mssv }} - Ten: {{ student.name }} - Lop: {{ student.class }}</li>
        {% endfor %}
        </ul>
    </body>
    </html>
    """
    return render_template_string(html_template, students=students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
