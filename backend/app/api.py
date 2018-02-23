from . import app, db
from app import models

@app.route("/persons")
def get_persons():
    t = models.Project("Testproject", "beschrijving enzo")
    db.session.add(t)
    db.session.commit()
    return t.name
