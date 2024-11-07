from modules.Storage import Storage
from modules.NoteDisplay import NoteDisplay
from modules.NoteBuilder import NoteBuilder
# Facade pattern, Model in MVC(Model-View-Controller)
class NoteManager:
    def __init__(self, storage_path, storage_template):
        self.storage = Storage(storage_path, storage_template)
        self.display = NoteDisplay()
        self.storage.register_observer(self.display)

    def add_note(self, name, tags, text):
        builder = NoteBuilder()
        note = (
            builder
            .set_name(name)
            .add_tag(*tags)
            .set_text(text)
            .build()
        )
        self.storage.data["notes"].append(note)
        self.storage.write()
        print("Заметка добавлена!")

    def delete_note_by_name(self, name):
        notes = self.storage.data["notes"]
        self.storage.data["notes"] = [note for note in notes if note["name"] != name]
        self.storage.write()
        print(f"Заметка '{name}' удалена!")

    def list_notes(self):
        self.display.update(self.storage.data)

    def reset_storage(self):
        print("Сбрасываем данные...")
        self.storage.reset()
        print("Все данные были сброшены!")
