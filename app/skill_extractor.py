
import re

# Technical skills supported by CareerPilot AI
TECHNICAL_SKILLS = [
      # Programming languages
    "python", "java", "c++", "c", "javascript",
    "typescript", "c#", "php", "go", "ruby",

    # Web development
    "html", "css", "react", "angular", "vue",
    "node.js", "express.js", "bootstrap", "tailwind css",

    # Backend and APIs
    "fastapi", "flask", "django", "spring boot",
    "rest api", "graphql",

    # Databases
    "sql", "mysql", "postgresql", "mongodb",
    "sqlite", "redis", "oracle",

    # Data science
    "data science", "data analysis", "pandas",
    "numpy", "matplotlib", "seaborn", "excel",
    "power bi", "tableau",

    # AI and machine learning
    "artificial intelligence", "machine learning",
    "deep learning", "natural language processing",
    "generative ai", "llm", "rag",
    "tensorflow", "pytorch", "scikit-learn",

    # Cloud and DevOps
    "aws", "azure", "google cloud", "docker",
    "kubernetes", "jenkins", "linux", "git",
    "github", "ci/cd",

    # Core computer science
    "data structures", "algorithms",
    "object oriented programming",
    "operating systems", "computer networks",
    "dbms"
]


def extract_skills(text):

    if not text:
        return []

    text = text.lower()

    found_skills = []

    for skill in TECHNICAL_SKILLS:

        # Match complete terms rather than accidental substrings
        if skill == "c":
             pattern = r"(?<!\w)c(?!\w|\+\+|#)"
        else:
          pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)
    return sorted(found_skills)
