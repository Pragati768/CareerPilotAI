
import pytest

from app.job_analyzer import analyze_job_description


def test_analyze_job_description():

    job_description = """
    We need a developer skilled in Python, SQL,
    React, FastAPI and Machine Learning.
    """

    result = analyze_job_description(job_description)

    assert "python" in result["required_skills"]
    assert "sql" in result["required_skills"]
    assert "react" in result["required_skills"]

    assert result["total_required_skills"] == 5


def test_empty_job_description():

    with pytest.raises(ValueError):
        analyze_job_description("")


def test_no_recognized_skills():

    with pytest.raises(ValueError):
        analyze_job_description(
            "We need a hardworking and creative candidate."
        )

