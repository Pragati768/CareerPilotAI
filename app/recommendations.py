
SKILL_GUIDE = {
    "python": {
        "learning": "Learn Python fundamentals, functions, OOP and data structures.",
        "project": "Build a Python-based expense tracker.",
        "questions": [
            "What are Python lists and tuples?",
            "What is the difference between a list and a dictionary?",
            "Explain object-oriented programming in Python."
        ]
    },

    "java": {
        "learning": "Learn Java OOP, collections, exception handling and multithreading.",
        "project": "Build a Java-based library management system.",
        "questions": [
            "Explain the four pillars of OOP.",
            "What is the difference between an interface and an abstract class?",
            "What is exception handling in Java?"
        ]
    },

    "sql": {
        "learning": "Learn SQL queries, joins, subqueries, grouping and indexing.",
        "project": "Build a student database management system.",
        "questions": [
            "What is the difference between WHERE and HAVING?",
            "Explain different types of SQL joins.",
            "What is a primary key?"
        ]
    },

    "react": {
        "learning": "Learn components, props, state, hooks and React Router.",
        "project": "Build a job application tracking dashboard.",
        "questions": [
            "What are React components?",
            "What is the difference between props and state?",
            "What is the use of useEffect?"
        ]
    },

    "fastapi": {
        "learning": "Learn API routes, request validation, Pydantic and HTTP methods.",
        "project": "Build a REST API for a task management application.",
        "questions": [
            "What is FastAPI?",
            "What is Pydantic used for?",
            "What is the difference between GET and POST?"
        ]
    },

    "machine learning": {
        "learning": "Learn supervised learning, unsupervised learning, model evaluation and feature engineering.",
        "project": "Build a student performance prediction model.",
        "questions": [
            "What is supervised learning?",
            "Explain overfitting and underfitting.",
            "What is the difference between classification and regression?"


          
        ]
    },

    "c++": {
        "learning": "Learn C++ fundamentals, STL, pointers, OOP, recursion and data structures.",
        "project": "Build a student record management system using C++.",
        "questions": [
            "What is the difference between C and C++?",
            "What are pointers in C++?",
            "What is the difference between vector and array?"
         ]
    },

    "c#": {
        "learning": "Learn C# syntax, OOP, collections, exception handling and .NET fundamentals.",
        "project": "Build a library management application using C#.",
        "questions": [
            "What is the difference between a class and an object?",
            "What is the difference between value and reference types?",
            "What is the .NET framework?"
        ]
    },

    "javascript": {
        "learning": "Learn variables, functions, arrays, objects, promises, async/await and DOM manipulation.",
        "project": "Build an interactive job application tracker.",
        "questions": [
            "What is the difference between let, const and var?",
            "What is a JavaScript promise?",
            "What is the difference between == and ===?"
        ]
    },

    "html": {
        "learning": "Learn HTML elements, forms, semantic tags, tables and accessibility.",
        "project": "Build a personal portfolio webpage.",
        "questions": [
            "What are semantic HTML elements?",
            "What is the difference between div and span?",
            "What is the purpose of HTML forms?"
        ]
    },

    "css": {
        "learning": "Learn selectors, box model, Flexbox, Grid, positioning and responsive design.",
        "project": "Create a responsive portfolio website.",
        "questions": [
            "Explain the CSS box model.",
            "What is the difference between Flexbox and Grid?",
            "What are CSS media queries?"
        ]
    },

    "data structures": {
        "learning": "Learn arrays, linked lists, stacks, queues, trees, graphs and hash maps.",
        "project": "Build a visual data structure learning application.",
        "questions": [
            "What is the difference between stack and queue?",
            "What is a binary tree?",
            "What is a hash map?"
        ]
    },

    "dbms": {
        "learning": "Learn database fundamentals, normalization, keys, transactions and SQL.",
        "project": "Build a student database management system.",
        "questions": [
            "What is database normalization?",
            "What are primary and foreign keys?",
            "What are ACID properties?"
        ]
    },

    "docker": {
        "learning": "Learn containers, images, Dockerfiles, volumes and container networking.",
        "project": "Containerize a Python Flask application.",
        "questions": [
            "What is Docker?",
            "What is the difference between an image and a container?",
            "What is a Dockerfile?"
        ]
    }
}


def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        skill = skill.strip().lower()

        if not skill:
            continue

        guide = SKILL_GUIDE.get(skill)

        if guide:
            recommendation = {
                "skill": skill,
                "learning": guide["learning"],
                "project": guide["project"],
                "interview_questions": guide["questions"]
            }

        else:
            recommendation = {
                "skill": skill,
                "learning": f"Start with the fundamentals of {skill} and practise its core concepts.",
                "project": f"Build a small practical project using {skill}.",
                "interview_questions": [
                    f"What is {skill}?",
                    f"What are the important concepts of {skill}?",
                    f"Where is {skill} used in real-world applications?"
                ]
            }

        recommendations.append(recommendation)

    return recommendations
