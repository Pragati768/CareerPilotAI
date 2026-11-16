
from app.recommendations import generate_recommendations


def test_generate_recommendations():

    result = generate_recommendations(["python", "sql"])

    assert len(result) == 2
    assert result[0]["skill"] == "python"
    assert result[1]["skill"] == "sql"

    assert "learning" in result[0]
    assert "project" in result[0]
    assert "interview_questions" in result[0]


def test_empty_missing_skills():

    result = generate_recommendations([])

    assert result == []


def test_unknown_skill():

    result = generate_recommendations(["docker"])

    assert len(result) == 1
    assert result[0]["skill"] == "docker"
    assert len(result[0]["interview_questions"]) == 3

def test_recommendations_for_cpp_and_javascript():
    result = generate_recommendations(["c++", "javascript"])

    assert len(result) == 2
    assert result[0]["skill"] == "c++"
    assert result[1]["skill"] == "javascript"

    for recommendation in result:
        assert recommendation["learning"]
        assert recommendation["project"]
        assert len(recommendation["interview_questions"]) == 3