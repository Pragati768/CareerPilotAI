
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from app.resume_parser import extract_resume_text
from app.skill_extractor import extract_skills
from app.job_analyzer import analyze_job_description
from app.matcher import match_skills
from app.recommendations import generate_recommendations

# Initialize Flask application
app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

# Application configuration
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
app.config["SECRET_KEY"] = "careerpilot-development-key"

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        resume_file = request.files.get("resume")
        job_description = request.form.get("job_description", "")

        try:
            # Validate resume upload
            if not resume_file or not resume_file.filename:
                raise ValueError("Please upload your resume PDF.")

            filename = secure_filename(resume_file.filename)

            if not filename.lower().endswith(".pdf"):
                raise ValueError("Please upload a PDF file.")

            if resume_file.mimetype != "application/pdf":
                raise ValueError(
                    "Invalid file type. Please upload a valid PDF."
                )

            # Validate job description
            if not job_description.strip():
                raise ValueError("Please enter a job description.")

            # Step 1: Extract resume text
            resume_text = extract_resume_text(resume_file.stream)

            # Step 2: Extract resume skills
            resume_skills = extract_skills(resume_text)

            if not resume_skills:
                raise ValueError(
                    "No recognized technical skills found in your resume."
                )

            # Step 3: Analyze job description
            job_result = analyze_job_description(job_description)

            # Step 4: Compare resume and job skills
            match_result = match_skills(
                resume_skills,
                job_result["required_skills"]
            )

            # Step 5: Generate recommendations
            recommendations = generate_recommendations(
                match_result["missing_skills"]
            )

            # Prepare final result
            result = {
                "resume_skills": resume_skills,
                "required_skills": job_result["required_skills"],
                "matching_skills": match_result["matching_skills"],
                "missing_skills": match_result["missing_skills"],
                "extra_skills": match_result["extra_skills"],
                "match_percentage": match_result["match_percentage"],
                "recommendations": recommendations
            }

            return render_template(
                "index.html",
                result=result,
                error=None
            )

        except ValueError as error:
            return render_template(
                "index.html",
                result=None,
                error=str(error)
            )

        except Exception:
            app.logger.exception("Unexpected error during resume analysis")

            return render_template(
                "index.html",
                result=None,
                error="Something went wrong while analyzing your resume. Please try again."
            ), 500

    return render_template(
        "index.html",
        result=None,
        error=None
    )

# Handle files larger than 5 MB
@app.errorhandler(413)
def file_too_large(error):
    return render_template(
        "index.html",
        result=None,
        error="File is too large. Maximum upload size is 5 MB."
    ), 413

if __name__ == "__main__":
    app.run(debug=True)