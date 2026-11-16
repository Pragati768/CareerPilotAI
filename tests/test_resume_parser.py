import io
import pytest

from app.resume_parser import extract_resume_text


def test_invalid_pdf():

    invalid_file = io.BytesIO(b"invalid pdf")

    with pytest.raises(ValueError):
        extract_resume_text(invalid_file)