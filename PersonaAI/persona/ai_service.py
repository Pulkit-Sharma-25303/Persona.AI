import requests
import json
import re
import pdfplumber
from docx import Document
from django.conf import settings
from .models import Project

def extract_text_from_file(file_path):
    """Extracts text from a PDF or DOCX file."""
    text = ""
    try:
        if file_path.lower().endswith('.pdf'):
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
        elif file_path.lower().endswith('.docx'):
            doc = Document(file_path)
            for para in doc.paragraphs:
                text += para.text + "\n"
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
    return text

def analyze_resume_with_ollama(resume_text):
    """
    Sends resume text to a local Ollama instance with an enhanced prompt to separate experience from projects.
    """
    prompt = f"""
    You are a top-tier career coach and resume expert. Your task is to analyze the following resume text and extract the key information into a structured JSON format. You must differentiate between professional work experience and personal/academic projects.
    Provide the output in a clean, parsable JSON format ONLY. Do not include any introductory text, explanations, or markdown formatting.

    The JSON object must have the following structure:
    {{
      "job_title": "The person's most recent or desired job title.",
      "summary": "A detailed and compelling professional summary of 4-5 sentences.",
      "skills": "A comma-separated string of all key skills, programming languages, and tools.",
      "work_experience": [
        {{
          "title": "The job title held at the company.",
          "company": "The company name.",
          "description": "A concise paragraph summarizing the key responsibilities and achievements."
        }}
      ],
      "projects": [
        {{
          "name": "The name of the personal or academic project.",
          "technologies": "The key technologies used in the project.",
          "description": "A concise paragraph summarizing what the project is and what was accomplished."
        }}
      ]
    }}

    Analyze the entire resume. Populate the 'work_experience' list with entries from sections like 'Work Experience', 'Internships', and 'Employment'. Populate the 'projects' list with entries from sections like 'Projects' or 'Personal Projects'. Extract ALL entries you find for both categories.

    Resume Text:
    ---
    {resume_text}
    ---
    """

    ollama_api_url = "http://localhost:11434/api/generate"
    payload = {
        "model": "gemma2:2b",
        "prompt": prompt,
        "format": "json",
        "stream": False
    }

    try:
        response = requests.post(ollama_api_url, json=payload)
        response.raise_for_status()
        response_data = response.json()
        return json.loads(response_data.get('response', '{}'))
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama API: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from Ollama response: {e}")
        raw_response = response_data.get('response', '')
        json_match = re.search(r'```json\n({.*})\n```', raw_response, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except json.JSONDecodeError:
                print("Failed to decode JSON even after finding markdown block.")
        return None

def process_resume(portfolio):
    """The main function to orchestrate resume processing."""
    if not portfolio.resume:
        return

    resume_path = portfolio.resume.path
    print(f"Processing resume for {portfolio.user.username} at {resume_path}")
    
    text = extract_text_from_file(resume_path)
    if not text:
        print("Could not extract text from resume.")
        return

    data = analyze_resume_with_ollama(text)
    if not data:
        print("AI analysis failed or returned no data.")
        return

    portfolio.job_title = data.get('job_title', portfolio.job_title)
    portfolio.about_me_generated = data.get('summary', portfolio.about_me_generated)
    portfolio.skills_input = data.get('skills', portfolio.skills_input)
    portfolio.save()

    # --- UPDATED LOGIC TO HANDLE SEPARATE LISTS ---
    portfolio.projects.all().delete()
    
    work_experience = data.get('work_experience', [])
    projects = data.get('projects', [])
    
    display_counter = 0

    # First, create entries for work experience, setting the category correctly
    for exp in work_experience:
        Project.objects.create(
            portfolio=portfolio,
            category='experience', # Set the category
            name=exp.get('title', 'Professional Role'),
            technologies=exp.get('company', ''), # Storing company name in the technologies field
            description_generated=exp.get('description', ''),
            display_order=display_counter
        )
        display_counter += 1
        
    # Next, create entries for projects, setting the category correctly
    for proj in projects:
        Project.objects.create(
            portfolio=portfolio,
            category='project', # Set the category
            name=proj.get('name', 'Personal Project'),
            technologies=proj.get('technologies', ''), # Storing actual technologies
            description_generated=proj.get('description', ''),
            display_order=display_counter
        )
        display_counter += 1

    print(f"Successfully processed and updated portfolio for {portfolio.user.username}")

