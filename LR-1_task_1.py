class Table:
    # Класс для стола. У стола есть высота, ширина и материал
    def __init__(self, height, width, material):
        """
        Создаем стол. Нужно задать ему размеры и материал.

        height - высота стола (больше нуля), width - ширина стола (больше нуля), material - из чего сделан (строка)

        Пример:
        >>> my_table = Table(80, 120, "дерево")
        >>> my_table.material
        'дерево'
        """
        if height <= 0 or width <= 0:
            raise ValueError("Высота и ширина стола должны быть больше нуля.")
        self.height = height
        self.width = width
        self.material = material

    def find_area(self):
        """
        Находим площадь стола (высота * ширина), возвращаем число - площадь.
        """
        return self.height * self.width

    def change_color(self, new_color):
        """
        Меняем цвет стола (ну, как бы цвет материала).
        new_color - новый цвет (строка)

        Пример:
        >>> t = Table(80, 120, "дерево")
        >>> t.change_color("коричневое")
        >>> t.material
        'дерево коричневое'
        """
        self.material = f"{self.material} {new_color}".strip()


class Tree:
    # Класс для дерева. У дерева есть высота, возраст и вид
    def __init__(self, height, age, species):
        """
        Создаем дерево.
        height - высота в метрах (больше нуля), age - возраст в годах (больше или равно нулю), species - вид дерева (строка)
        """
        if height <= 0:
            raise ValueError("Дерево не может быть нулевой высоты!")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self.height = height
        self.age = age
        self.species = species

    def grow(self, years):
        """
        Дерево растет с годами.
        years - сколько лет прошло (больше нуля)
        Возвращаем новую высоту.
        """
        if years <= 0:
            raise ValueError("years должен быть больше нуля.")
        # Простой пример: высота растет линейно, например на 0.5 м за год
        growth_rate = 0.5
        self.height += growth_rate * years
        return self.height

    def check_if_old(self):
        """
        Проверяем, старое ли дерево.
        Возвращаем True если больше 50 лет, иначе False.
        """
        return self.age > 50


class SocialNetwork:
    # Класс для социальной сети. У нее есть название, пользователи и год создания
    def __init__(self, name, users_count, year):
        """
        Создаем соцсеть.
        name - название (строка), users_count - сколько пользователей (больше нуля), year - год создания (больше 2000)
        """
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным!")
        if year < 2000:
            raise ValueError("Соцсети до 2000 года? Сомнительно...")
        self.name = name
        self.users_count = users_count
        self.year = year

    def how_old(self, current_year):
        """
        Узнаем, сколько лет соцсети.
        current_year - какой сейчас год
        Возвращаем возраст.
        """
        return current_year - self.year

    def add_users(self, new_users):
        """
        Добавляем новых пользователей.
        new_users - сколько новых людей (больше нуля)
        """
        if new_users <= 0:
            raise ValueError("new_users должно быть больше нуля.")
        self.users_count += new_users