# ATS-Score-Checker
Resume Analyzer
Overview
The Resume Analyzer is a desktop application built using Python and Tkinter that evaluates resumes based on the presence of specific keywords and basic formatting criteria. It provides feedback on the resume's structure, content relevance, and overall score to help users improve their resumes for job applications.

Features
Keyword Matching: Scores the resume based on the presence of keywords across various domains like Full Stack Development, Cloud, Machine Learning, and more.
Basic Formatting Checks: Provides feedback on resume length and formatting, and checks for the presence of essential sections.
File Support: Supports analysis of resumes in TXT, PDF, and DOCX formats.
User Feedback: Offers suggestions for improvement and a final score based on the resume content.
Requirements
Python 3.x
tkinter (for GUI)
PyPDF2 (for PDF file reading)
python-docx (for DOCX file reading)
Standard Python libraries (re)
Installation
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
Install Required Packages: Install the required Python packages using pip:

bash
Copy code
pip install PyPDF2 python-docx
Usage
Run the Application:

bash
Copy code
python resume_analyzer.py
Upload and Analyze Resume:

Click on the "Upload and Analyze Resume" button.
Select a resume file (TXT, PDF, or DOCX) from your file system.
The application will read the resume, analyze it based on predefined criteria, and display the results in a pop-up window.
Code Details
analyze_resume(text)
This function takes the resume text as input and evaluates it based on the following criteria:

Keyword Matching: Identifies the presence of domain-specific keywords and assigns points.
Basic Formatting Checks: Evaluates the resume length and the presence of numeric data.
Section Checks: Ensures that essential sections like "Experience" and "Skills" are present.
upload_and_analyze_resume()
This function handles the file selection dialog, reads the resume content based on the file type (TXT, PDF, DOCX), and invokes the analyze_resume function to process and analyze the resume.

Known Issues
The tool assumes that resumes are in English and may not handle non-English text well.
PDF extraction might not be perfect for all documents due to varying formats.
Contributing
Contributions to improve the Resume Analyzer are welcome. Please submit issues or pull requests to the repository.

Contact
For any questions or feedback, please reach out to nandanmyd321@gmail.com

