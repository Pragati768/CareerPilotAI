
from app.skill_extractor import extract_skills


def test_extract_multiple_skills():

    text = """
    I know Python, Java, SQL, React and Machine Learning.
    """

    result = extract_skills(text)

    assert "python" in result
    assert "java" in result
    assert "sql" in result
    assert "react" in result
    assert "machine learning" in result


def test_empty_text():

    result = extract_skills("")

    assert result == []


def test_no_technical_skills():

    result = extract_skills(
        "I enjoy reading books and playing cricket."
    )

    assert result == []

def test_cpp_is_not_detected_as_c():
    result = extract_skills("I have experience in C++ and Python.")

    assert "c++" in result
    assert "c" not in result

def test_csharp_is_not_detected_as_c():
    result = extract_skills("I have experience in C# and Python.")

    assert "c#" in result
    assert "c" not in result