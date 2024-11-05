class NoteBuilder:
    def __init__(self):
        self._name = ""
        self._tags = []
        self._text = ""

    def set_name(self, name):
        self._name = name
        return self

    def add_tag(self, tag):
        self._tags.append(tag)
        return self

    def set_text(self, text):
        self._text = text
        return self

    def build(self):
        return {
            "name": self._name,
            "tags": self._tags,
            "text": self._text
        }
