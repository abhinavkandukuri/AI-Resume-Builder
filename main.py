from prompt_templates import resume_prompt
from resume_agent import generate_resume

name = input("Enter name: ")
skills = input("Enter skills: ")
education = input("Enter education: ")
projects = input("Enter projects: ")
role = input("Enter target role: ")

final_prompt = resume_prompt.format(
    name=name,
    skills=skills,
    education=education,
    projects=projects,
    role=role
)

result = generate_resume(final_prompt)

print("\\n GENERATED RESUME:\\n")
print(result)