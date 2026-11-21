from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Student Course API!",
        "status": "running",
        "available_endpoints": [
            "/api/health",
            "/api/courses",
            "/api/courses/1",
            "/api/courses/9999"
        ]
    }), 200

courses = [
    {
        "id": 1,
        "course_code": "CS 101",
        "course_name": "Introduction to Programming",
        "description": "Introduction to programming concepts and problem solving."
    },
    {
        "id": 2,
        "course_code": "IT 204",
        "course_name": "Networking Fundamentals",
        "description": "Basic networking concepts and network devices."
    },
    {
        "id": 3,
        "course_code": "IT 301",
        "course_name": "Database Management",
        "description": "Introduction to databases and data management."
    },
    {
        "id": 4,
        "course_code": "IT 305",
        "course_name": "Web Development",
        "description": "Fundamentals of web development."
    },
    {
        "id": 5,
        "course_code": "IT 310",
        "course_name": "System Integration",
        "description": "Introduction to system integration and APIs."
    }
]

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "Student Course API",
        "message": "The Student Course API is running."
    }), 200

@app.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify(courses), 200

@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = next((c for c in courses if c["id"] == course_id), None)

    if course is None:
        return jsonify({
            "error": "Course not found",
            "message": f"No course with ID {course_id} exists.",
            "status": 404
        }), 404

    return jsonify(course), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
