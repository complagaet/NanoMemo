from modules.storage_template import storage as storage_template
from modules.NoteManager import NoteManager
from modules.NoteController import NoteController

def main():
    note_manager = NoteManager("storage/", storage_template)  # Создаем менеджер заметок
    controller = NoteController(note_manager)  # Создаем контроллер и передаем менеджер заметок
    controller.main_menu()  # Запускаем главное меню

if __name__ == '__main__':
    main()
