
def match_skills(resume_skills, required_skills):

    # Normalize skills to lowercase and remove duplicates
    resume_set = {
        skill.strip().lower() for skill in resume_skills
    }

    required_set = {
        skill.strip().lower() for skill in required_skills
    }

    # Find matching skills
    matching_skills = sorted(resume_set & required_set)

    # Find skills missing from the resume
    missing_skills = sorted(required_set - resume_set)

    # Find additional skills in the resume
    extra_skills = sorted(resume_set - required_set)

    # Calculate skill overlap percentage
    if len(required_set) == 0:
        match_percentage = 0.0
    else:
        match_percentage = round(
            (len(matching_skills) / len(required_set)) * 100,
            2
        )

    return {
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "extra_skills": extra_skills,
        "match_percentage": match_percentage
    }

 