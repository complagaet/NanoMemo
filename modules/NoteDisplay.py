from modules.observer import Observer

class NoteDisplay(Observer):
    def update(self, data):
        notes = data.get("notes", [])
        print(f"МОИ ЗАМЕТКИ ({len(notes)})")
        for note in notes:
            print("---------------")
            print(f"Название: {note['name']}")
            print(f"Теги: {', '.join(note['tags'])}")
            print("->")
            print(note['text'].strip())
