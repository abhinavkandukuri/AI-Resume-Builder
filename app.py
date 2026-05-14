import streamlit as st
from prompt_templates import resume_prompt
from resume_agent import generate_resume
from fpdf import FPDF

st.title("AI Resume Builder")

name = st.text_input("Enter your name")

skills = st.text_area("Enter your skills")

education = st.text_area("Enter your education")

projects = st.text_area("Enter your projects")

role = st.text_input("Enter target role")

if st.button("Generate Resume"):

    final_prompt = resume_prompt.format(
        name=name,
        skills=skills,
        education=education,
        projects=projects,
        role=role
    )

    result = generate_resume(final_prompt)

    st.subheader("Generated Resume")

    st.write(result)

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, result)

    pdf.output("resume.pdf")

    # Download button
    with open("resume.pdf", "rb") as file:
        st.download_button(
            label="Download Resume PDF",
            data=file,
            file_name="resume.pdf",
            mime="application/pdf"
        )