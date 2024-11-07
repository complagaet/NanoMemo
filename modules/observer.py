class Observer:
    def update(self, data):
        raise NotImplementedError("Subclasses must implement this method.")
# observer pattern: observer+NoteDisplay