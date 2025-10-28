# Persona.AI - AI-Powered Portfolio Generator

Persona.AI is a web application that leverages AI to automatically generate beautiful, professional portfolio websites directly from a user's resume. Upload your resume, let the AI extract and polish your information, choose a stunning design, and share your unique career story with the world.

✨ Key Features
📄 Resume Upload: Supports PDF and DOCX resume formats.
🧠 AI-Powered Content Extraction: Uses AI (configurable for local Ollama or cloud providers) to parse resumes, extracting:
Professional Summary
Key Skills \& Technologies
Work Experience (Categorized)
Projects (Categorized, with URLs)
🎨 Multiple Design Templates: Users can choose from various professional and creative themes for their portfolio:
Modern Dark
Clean Minimalist
Creative Artistic
Corporate Professional
Digital Experimental
👤 User Accounts: Secure user registration and login system.
✏️ Dashboard Management: A private dashboard for users to:
Upload/Manage Resumes
Select Design Templates
Upload Profile Pictures \& Background Images
Review and Manually Edit all AI-generated content (summary, skills, experience, projects, links).
Manually Add/Remove Experience \& Project entries.
🌐 Public Portfolio URL: Each user gets a unique, shareable URL for their generated portfolio (e.g., yoursite.com/username).
🚀 Deployment Ready: Configured for easy deployment on platforms like Render.
🛠️ Tech Stack
Backend: Python, Django
Database: PostgreSQL
AI:
Local: Ollama (e.g., Llama 3)
Production: Configurable via environment variable for Cloud AI APIs (Groq, Together AI, etc.)
Frontend: HTML, Tailwind CSS, JavaScript (for dynamic forms)
Resume Parsing: pdfplumber, python-docx
Deployment: Gunicorn, Whitenoise, dj-database-url, Render (example)
🚀 Getting Started (Local Development)
Follow these steps to set up and run the project on your local machine.
Prerequisites
Python 3.10+
PostgreSQL installed and running
Git
Setup Instructions
Clone the Repository:
git clone [https://github.com/Pulkit-Sharma-25303/Persona.AI/tree/main](https://github.com/Pulkit-Sharma-25303/Persona.AI/tree/main)
cd Persona.AI

Navigate to Project Directory:
Make sure you are in the directory containing manage.py. If your project files are inside a subfolder (e.g., PersonaAI), navigate into it:
cd PersonaAI

(Adjust PersonaAI if your folder name is different)
Create and Activate Virtual Environment:
python -m venv venv

# On Windows

.\venv\Scripts\activate

# On macOS/Linux

source venv/bin/activate

Install Dependencies:
pip install -r requirements.txt

Set Up PostgreSQL Database:
Create a PostgreSQL database and user for the project. For example:
CREATE DATABASE PersonaAI_db;
CREATE USER persona_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE PersonaAI_db TO persona_user;

(Ensure your database details match the default URL in settings.py or use environment variables)
Configure Environment Variables:
Create a .env file in the same directory as manage.py.
Add your SECRET_KEY (generate one if needed) and your local database URL:
SECRET_KEY='your_strong_random_secret_key'
DATABASE_URL='postgresql://persona_user:your_password@localhost/PersonaAI_db'

# Optional: For local Ollama

# OLLAMA_API_URL='http://localhost:11434/api/generate'

Important: Add .env to your .gitignore file!
Run Database Migrations:
python manage.py migrate

Create a Superuser (Optional but Recommended):
python manage.py createsuperuser

Run the Development Server:
python manage.py runserver

convert in readme file

Here’s a clean, well-structured version of your project content formatted as a `README.md` file for Persona.AI:

***

```markdown
# Persona.AI – AI-Powered Portfolio Generator

Persona.AI is a web application that leverages artificial intelligence to automatically generate professional portfolio websites directly from a user's resume. Upload your resume, let the AI extract and refine your information, choose a stunning design, and share your unique career story with the world.

## ✨ Key Features

### 📄 Resume Upload
- Supports PDF and DOCX resume formats.

### 🧠 AI-Powered Content Extraction
AI parses and structures resume data, extracting:
- Professional Summary  
- Key Skills & Technologies  
- Work Experience (categorized)  
- Projects (categorized with URLs)  

Supports configurable AI providers:
- Local: Ollama (e.g., Llama 3)  
- Cloud: Groq, Together AI, and more  

### 🎨 Multiple Design Templates
Choose from a variety of professional and creative themes:
- Modern Dark  
- Clean Minimalist  
- Creative Artistic  
- Corporate Professional  
- Digital Experimental  

### 👤 User Accounts
- Secure registration and login system.

### ✏️ Dashboard Management
Manage your portfolio content in a private dashboard:
- Upload/Manage resumes  
- Select design templates  
- Upload profile and background images  
- Review and manually edit AI-generated content (summary, skills, experience, projects)  
- Add or remove experiences and projects  

### 🌐 Public Portfolio URL
- Each user gets a unique, shareable URL (e.g., `yoursite.com/username`).

### 🚀 Deployment Ready
- Pre-configured for easy deployment on platforms like Render.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | Python, Django |
| Database | PostgreSQL |
| AI | Local (Ollama) or Cloud (Groq, Together AI) |
| Frontend | HTML, Tailwind CSS, JavaScript |
| Resume Parsing | pdfplumber, python-docx |
| Deployment | Gunicorn, Whitenoise, dj-database-url, Render |

---

## 🚀 Getting Started (Local Development)

### Prerequisites
- Python 3.10+  
- PostgreSQL installed and running  
- Git  

### Setup Instructions

#### 1. Clone the Repository
```

git clone https://github.com/YourUsername/Persona.AI.git
cd Persona.AI

```

#### 2. Navigate to Project Directory
If your project files are inside a subfolder (e.g., `PersonaAI`), navigate into it:
```

cd PersonaAI

```
(Adjust folder name if different.)

#### 3. Create and Activate Virtual Environment
```

python -m venv venv

# On Windows

.\venv\Scripts\activate

# On macOS/Linux

source venv/bin/activate

```

#### 4. Install Dependencies
```

pip install -r requirements.txt

```

#### 5. Set Up PostgreSQL Database
Create a database and user:
```

CREATE DATABASE PersonaAI_db;
CREATE USER persona_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE PersonaAI_db TO persona_user;

```
Ensure your database URL matches the configuration in `settings.py` or environment variables.

#### 6. Configure Environment Variables
Create a `.env` file in the same directory as `manage.py`:
```

SECRET_KEY='your_strong_random_secret_key'
DATABASE_URL='postgresql://persona_user:your_password@localhost/PersonaAI_db'

# Optional: For local Ollama

# OLLAMA_API_URL='http://localhost:11434/api/generate'

```
**Important:** Add `.env` to your `.gitignore` file.

#### 7. Run Database Migrations
```

python manage.py migrate

```

#### 8. Create a Superuser (Optional)
```

python manage.py createsuperuser

```

#### 9. Run the Development Server
```

python manage.py runserver

```

---

## 📬 Deployment
Persona.AI is ready for deployment on platforms like Render.  
Use Gunicorn for serving Django and Whitenoise for static files.  
Environment variables can be configured easily for production databases and external AI APIs.
```
