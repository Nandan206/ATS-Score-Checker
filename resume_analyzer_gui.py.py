import re
import tkinter as tk
from tkinter import filedialog, messagebox

def analyze_resume(text):
    # Define the keywords for scoring across various domains
    keywords = {
        'fullstack': ['JavaScript', 'Node.js', 'React', 'HTML', 'CSS', 'API', 'MongoDB', 'SQL', 'Angular', 'Vue.js'],
        'cloud': ['AWS', 'Azure', 'GCP', 'DevOps', 'CI/CD', 'Kubernetes', 'Docker', 'Terraform', 'CloudFormation', 'EC2'],
        'machine learning': ['Python', 'TensorFlow', 'PyTorch', 'Data Science', 'AI', 'Machine Learning', 'NLP', 'Keras', 'Scikit-learn'],
        'data science': ['Pandas', 'NumPy', 'R', 'Statistics', 'SQL', 'Tableau', 'Power BI', 'Data Analysis', 'Big Data'],
        'cybersecurity': ['Firewall', 'IDS', 'IPS', 'SIEM', 'Penetration Testing', 'Malware', 'Encryption', 'Network Security', 'Cyber Threats'],
        'networking': ['Cisco', 'Routing', 'Switching', 'TCP/IP', 'DNS', 'DHCP', 'VPN', 'LAN', 'WAN', 'Network Protocols'],
        'software development': ['Java', 'C++', 'Python', 'Agile', 'Scrum', 'SDLC', 'Version Control', 'Git', 'CI/CD'],
        'database management': ['SQL', 'NoSQL', 'MongoDB', 'MySQL', 'Oracle', 'Database Design', 'Normalization', 'PostgreSQL', 'DBA'],
        'project management': ['Project Planning', 'Agile', 'Scrum', 'Risk Management', 'MS Project', 'JIRA', 'Stakeholder Management'],
        'UI/UX design': ['Figma', 'Sketch', 'Adobe XD', 'Wireframing', 'Prototyping', 'User Research', 'Design Thinking', 'UI Design', 'UX Design'],
        'business analysis': ['Business Requirements', 'Process Mapping', 'UML', 'Stakeholder Engagement', 'Data Modeling', 'SWOT Analysis'],
        'finance': ['Financial Analysis', 'Excel', 'Budgeting', 'Forecasting', 'Financial Modeling', 'Investment', 'Risk Management', 'Accounting'],
        'marketing': ['SEO', 'Content Marketing', 'Google Analytics', 'Social Media', 'Email Marketing', 'PPC', 'Branding', 'Market Research'],
        'human resources': ['Recruitment', 'Employee Relations', 'Onboarding', 'HRIS', 'Performance Management', 'Talent Management'],
        'sales': ['Lead Generation', 'Salesforce', 'CRM', 'Negotiation', 'Customer Relations', 'Sales Strategy', 'B2B Sales'],
        'operations management': ['Supply Chain', 'Logistics', 'Inventory Management', 'Process Improvement', 'Lean Manufacturing', 'Six Sigma'],
        'legal': ['Contract Law', 'Litigation', 'Legal Research', 'Compliance', 'Intellectual Property', 'Corporate Law', 'Legal Writing'],
        'healthcare': ['Patient Care', 'EMR', 'HIPAA', 'Clinical Research', 'Medical Coding', 'Healthcare Management', 'Pharmaceuticals'],
        'education': ['Curriculum Design', 'Instructional Design', 'E-learning', 'Classroom Management', 'Educational Technology', 'Assessment'],
        'architecture': ['AutoCAD', 'Blueprints', 'Construction Management', '3D Modeling', 'Sustainable Design', 'Building Codes', 'LEED'],
        'engineering': ['Mechanical Engineering', 'Electrical Engineering', 'CAD', 'FEA', 'Manufacturing Processes', 'Product Design', 'Prototyping'],
    }

    # Initialize the score
    score = 0
    max_score = 100

    # Keyword Matching Score
    matched_keywords = []
    for domain, words in keywords.items():
        for word in words:
            if re.search(r'\b' + word + r'\b', text, re.IGNORECASE):
                score += 2  # Add 2 points for each relevant keyword found
                matched_keywords.append(word)

    # Basic Formatting Checks
    feedback = []
    if len(text) < 500:
        feedback.append("The resume seems to be too short. Consider adding more details about your experience.")
        score -= 10
    if not any(char.isdigit() for char in text):
        feedback.append("Consider adding dates or numbers to indicate your work experience timeline.")
        score -= 5

    # Experience and Skills Section Presence
    if 'experience' in text.lower():
        score += 10
    else:
        feedback.append("The resume lacks a clear 'Experience' section. Consider adding it.")

    if 'skills' in text.lower():
        score += 10
    else:
        feedback.append("The resume lacks a 'Skills' section. It's important to list relevant skills.")

    # Calculate final score
    score = max(0, min(score, max_score))

    # Generate feedback based on the score
    if score > 80:
        feedback.insert(0, "Excellent resume! It is well-structured and relevant to the job role.")
    elif score > 60:
        feedback.insert(0, "Good resume, but it could be improved with more specific details and better formatting.")
    else:
        feedback.insert(0, "The resume needs significant improvement. Focus on adding relevant content and improving formatting.")

    matched_keywords_str = ', '.join(matched_keywords) if matched_keywords else 'No specific keywords matched.'
    feedback.append(f"Matched Keywords: {matched_keywords_str}")

    return f"ATS Score: {score}/{max_score}. " + ' '.join(feedback)

def upload_and_analyze_resume():
    # Open file dialog to select resume
    file_path = filedialog.askopenfilename(
        title="Select Resume",
        filetypes=(("Text files", "*.txt"), ("PDF files", "*.pdf"), ("Word files", "*.docx"))
    )
    if not file_path:
        return  # If no file selected, return

    # Read the file content
    file_extension = file_path.split('.')[-1]
    if file_extension == 'txt':
        with open(file_path, 'r') as file:
            resume_text = file.read()
    elif file_extension == 'pdf':
        import PyPDF2
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            resume_text = ''.join(page.extract_text() for page in reader.pages)
    elif file_extension == 'docx':
        import docx
        doc = docx.Document(file_path)
        resume_text = '\n'.join(paragraph.text for paragraph in doc.paragraphs)
    else:
        messagebox.showerror("Error", "Unsupported file format!")
        return

    # Analyze the resume
    feedback = analyze_resume(resume_text)

    # Display the result
    messagebox.showinfo("Resume Analysis", feedback)

# Set up Tkinter window
root = tk.Tk()
root.title("Resume Analyzer")

# Create Upload Button
upload_button = tk.Button(root, text="Upload and Analyze Resume", command=upload_and_analyze_resume)
upload_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
