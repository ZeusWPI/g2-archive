from . import app, db
from app import models
from flask import jsonify

@app.route("/projects")
def get_all_projects():
    return jsonify([project.serialize() for project in models.Project.query.all()])
