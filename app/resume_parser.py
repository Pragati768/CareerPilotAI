from pypdf import PdfReader


def extract_resume_text(pdf_file):

    try:
        reader = PdfReader(pdf_file)

        if reader.is_encrypted:
            raise ValueError("Password-protected PDFs are not supported.")

        extracted_text = ""

        for page in reader.pages:
            text = page.extract_text() or ""
            extracted_text += text + "\n"

        if not extracted_text.strip():
            raise ValueError("No readable text found in the PDF.")

        return extracted_text.strip()

    except Exception as error:
        raise ValueError(f"Resume parsing failed: {error}")