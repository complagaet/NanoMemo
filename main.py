from modules.Storage import Storage
from modules.storage_template import storage as storage_template
from modules.NoteBuilder import NoteBuilder
from modules.NoteDisplay import NoteDisplay

# Инициализируем хранилище
# storage_template - это структура объекта хранилища
STORAGE = Storage("storage/", storage_template)

def init():
    # Ниже показываю то, как этим хранилищем пользоваться
    # Регистрируем NoteDisplay как наблюдателя
    display = NoteDisplay()
    STORAGE.register_observer(display)

    # Давайте попробуем создать заметку
    # Это пример того, как мы можем их хранить
    # По идее нам нужно реализовать класс, который будет управлять заметками
    # А также, он должен уметь выдавать подобный объект, как ниже,
    # Чтобы можно было сохранить заметку в JSON формате
    print("--- Выводим содеримое хранилища\n", STORAGE.data)  # Выводим содеримое хранилища
    print("--- Выводим имя пользователя - его нет, если данных нет")
    print("username:", STORAGE.data["username"])

    # Устанавливаем новое имя пользователя и сохраняем изменения
    STORAGE.data["username"] = "СУПЕР НИК ЕМОЕ"
    STORAGE.write()
    print("--- Выводим имя пользователя после изменения")
    print("username:", STORAGE.data["username"])

    # Выводим содержимое хранилища с новой заметкой
    print("--- Выводим содержимое хранилища с новой заметкой")
    display.update(STORAGE.data)  # Печатает данные в формате

    # Builder pattern для создания заметок
    # Создаем и добавляем новую заметку
    builder = NoteBuilder()
    note = (
        builder
        .set_name(f"Название заметки {len(STORAGE.data['notes']) + 1}")
        .add_tag("Манты")
        .add_tag("Пельмени")
        .set_text("Это супер текст самой заметки")
        .build()
    )
    STORAGE.data["notes"].append(note)
    STORAGE.write()  # Сохранение обновит список заметок через NoteDisplay

    # Хранилище можно сбросить
    reset = input("Чтобы сбросить хранилище введите 1: ")
    if reset == "1":
        print("Сбрасываем данные")
        STORAGE.reset()  # Сброс также приведет к обновлению заметок

if __name__ == '__main__':
    init()
