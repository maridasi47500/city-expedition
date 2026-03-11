from resume_matcher.matching import resume_job_desc_match

resume_path = "My_Resume.docx"
job_desc_path = "Job_desc.docx"

match_percentage = resume_job_desc_match(resume_path, job_desc_path)

print("Match percentage:", match_percentage)
