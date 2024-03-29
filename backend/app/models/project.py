from app import db

project_tree = db.Table(
    'project_tree',
    db.Column('parent_id', db.Integer, db.ForeignKey('project.id')),
    db.Column('children_id', db.Integer, db.ForeignKey('project.id'))
)

class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String)
    start_time = db.Column(db.DateTime)
    stop_time = db.Column(db.DateTime)
    parents = db.relationship(
        'Project',
        secondary=project_tree,
        primaryjoin=("Project.id==project_tree.c.children_id"),
        secondaryjoin=("Project.id==project_tree.c.parent_id"),
        backref=db.backref('children', lazy='dynamic'),
        lazy='dynamic'
    )

    def __repr__(self):
        return '<Project {}>'.format(self.name)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def serialize(self):
        return {
            "name": self.name,
            "description": self.description,
            "start_time": self.start_time.timestamp() if self.start_time else None,
            "stop_time": self.stop_time.timestamp() if self.stop_time else None,
            "id": self.id
        }
