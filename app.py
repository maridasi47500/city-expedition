from flask import Flask, render_template

app = Flask(__name__)
from resume_matcher.matching import resume_job_desc_match

resume_path = "My_Resume.docx"
job_desc_path = "Job_desc.docx"

match_percentage = resume_job_desc_match(resume_path, job_desc_path)

print("Match percentage:", match_percentage)

@app.route("/")
def hello_world():
    return render_template("hey.html")
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hey.html")
