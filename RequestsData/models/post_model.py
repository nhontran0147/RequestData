import json


class Post:
    def __init__(self, title="", point=0, creator="", comment=0):
        self._title = title
        self._point = point
        self._creator = creator
        self._comment = comment

    def to_string(self):
        result = "Title: " + self._title + "\n\t" + str(self._point) + "points by " + self._creator + "| " + str(
            self._comment) + " comments."
        return result

    def to_json(self):
        return {
            "title": self._title,
            "point": self._point,
            "creator": self._creator,
            "comment": self._comment
        }

    def print_log(self):
        val = json.dumps(self.to_json(), indent=2)
        print(val)

    def get_title(self):
        return self._title

    def get_point(self):
        return self._point

    def get_creator(self):
        return self._creator

    def get_comments(self):
        return self._comment