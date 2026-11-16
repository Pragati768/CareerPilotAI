
from app.skill_extractor import extract_skills


def analyze_job_description(job_description):

    if not job_description or not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    required_skills = extract_skills(job_description)

    if not required_skills:
        raise ValueError(
            "No recognized technical skills found in the job description."
        )

    return {
        "required_skills": required_skills,
        "total_required_skills": len(required_skills)
    }
