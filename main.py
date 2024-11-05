from modules.Storage import Storage
from modules.storage_template import storage as storage_template

# Инициализируем хранилище
# storage_template - это структура объекта хранилища
STORAGE = Storage("storage/", storage_template)


def init():
    # Ниже показываю то, как этим хранилищем пользоваться

    print("--- Выводим содеримое хранилища\n", STORAGE.data)  # Выводим содеримое хранилища

    # Выводим имя пользователя - оно пустое если файла storage/storage.json не было
    print("--- Выводим имя пользователя - его нет, если данных нет\nusername: ", STORAGE.data["username"])

    STORAGE.data["username"] = "СУПЕР НИК ЕМОЕ"  # Меняем имя пользователя
    STORAGE.write()  # Сохраняем изменения

    print("--- Выводим имя пользователя после изменения\nusername: ", STORAGE.data["username"])  # Выводим имя пользователя еще раз

    # Давайте попробуем создать заметку
    # Это пример того, как мы можем их хранить
    # По идее нам нужно реализовать класс, который будет управлять заметками
    # А также, он должен уметь выдавать подобный объект, как ниже,
    # Чтобы можно было сохранить заметку в JSON формате
    note = {
        "name": f"Название заметки {len(STORAGE.data["notes"]) + 1}",
        "tags": ["Манты", "Пельмени"],
        "text": "Это супер текст самой заметки"
    }
    STORAGE.data["notes"].append(note)  # Добавляем нашу новую заметку
    STORAGE.write()  # Сохраняем изменения

    # Выводим содеримое хранилища и видим сохраненную заметку
    print("--- Выводим содеримое хранилища с новой заметкой\n", STORAGE.data)

    # Нужно будет сделать метод для красивого вывода, типо этого
    notes = STORAGE.data["notes"]
    print(f"МОИ ЗАМЕТКИ ({len(notes)})")
    for note in notes:
        print(f"---------------\nНазвание: {note['name']}")
        print(f"Теги: {', '.join(note['tags'])}")
        print(f"->\n{note['text'].strip()}")

    # Хранилище можно сбросить
    reset = input("Чтобы сбросить хранилище введите 1: ")
    if reset == "1":
        print("Сбрасываем данные")
        STORAGE.reset()  # Метод для сброса хранилища



if __name__ == '__main__':
    init()
