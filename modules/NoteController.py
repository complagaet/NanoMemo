#Controller in MVC(Model-View-Controller)
class NoteController:
    def __init__(self, note_manager):
        self.note_manager = note_manager

    def main_menu(self):
        while True:
            print("\nВыберите действие:")
            print("1 - Показать все заметки")
            print("2 - Добавить заметку")
            print("3 - Удалить заметку по имени")
            print("4 - Сбросить хранилище")
            print("5 - Показать имя пользователя")
            print("6 - Установить имя пользователя")
            print("7 - Выход")

            choice = input("Введите номер действия: ")

            # Обрабатываем выбор пользователя
            if choice == "1":
                self.note_manager.list_notes()
            elif choice == "2":
                name = input("Введите название заметки: ")
                tags_input = input("Введите теги через запятую: ")
                text = input("Введите текст заметки: ")
                tags = [tag.strip() for tag in tags_input.split(",")]
                self.note_manager.add_note(name, tags, text)
            elif choice == "3":
                name = input("Введите название заметки для удаления: ")
                self.note_manager.delete_note_by_name(name)
            elif choice == "4":
                self.note_manager.reset_storage()
            elif choice == "5":
                self.show_username()
            elif choice == "6":
                self.set_username()
            elif choice == "7":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор, попробуйте снова.")
    def show_username(self):
        username = self.note_manager.get_username()
        print(f"Имя пользователя: {username}")

    def set_username(self):
        new_username = input("Введите новое имя пользователя: ")
        self.note_manager.set_username(new_username)
