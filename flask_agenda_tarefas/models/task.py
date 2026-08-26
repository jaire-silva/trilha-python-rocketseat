from typing_extensions import override


class Task:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    @override
    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"

    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }