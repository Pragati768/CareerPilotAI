
from app.matcher import match_skills


def test_match_skills():

    resume_skills = [
        "python", "java", "sql", "react", "git"
    ]

    required_skills = [
        "python", "sql", "fastapi",
        "machine learning", "react"
    ]

    result = match_skills(resume_skills, required_skills)

    assert result["matching_skills"] == [
        "python", "react", "sql"
    ]

    assert result["missing_skills"] == [
        "fastapi", "machine learning"
    ]

    assert result["extra_skills"] == [
        "git", "java"
    ]

    assert result["match_percentage"] == 60.0


def test_empty_resume():

    result = match_skills(
        [],
        ["python", "java"]
    )

    assert result["match_percentage"] == 0.0
    assert result["missing_skills"] == ["java", "python"]


def test_empty_requirements():

    result = match_skills(
        ["python", "java"],
        []
    )

    assert result["match_percentage"] == 0.0


def test_all_skills_match():

    result = match_skills(
        ["python", "sql"],
        ["python", "sql"]
    )

    assert result["match_percentage"] == 100.0


def test_match_skills_handles_duplicates_and_case():
    resume_skills = [" Python ", "PYTHON", "SQL"]
    required_skills = ["python", " sql ", "Java", "Java"]

    result = match_skills(resume_skills, required_skills)

    assert result["matching_skills"] == ["python", "sql"]
    assert result["missing_skills"] == ["java"]
    assert result["extra_skills"] == []
    assert result["match_percentage"] == 66.67