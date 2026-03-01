"""
Модуль для работы с музыкальными инструментами.
Реализует иерархию классов: базовый класс MusicalInstrument
и дочерние классы StringInstrument и WindInstrument.
"""
class MusicalInstrument:
    """
    Базовый класс для представления музыкального инструмента.
    Attributes:
        name (str): Название инструмента
        manufacturer (str): Производитель инструмента
        year (int): Год выпуска
        _price (float): Цена инструмента (инкапсулирован для контроля валидности)
    """
    def __init__(self, name: str, manufacturer: str, year: int, price: float) -> None:
        """
        Инициализация музыкального инструмента.
        Args:
            name: Название инструмента
            manufacturer: Производитель инструмента
            year: Год выпуска
            price: Цена инструмента
        """
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
        self._price = price

    def __str__(self) -> str:
        """
        Возвращает строковое представление инструмента для пользователя.
        Returns:
            Строковое представление инструмента
        """
        return f"{self.name} от {self.manufacturer} ({self.year} г.)"

    def __repr__(self) -> str:
        """
        Возвращает техническое строковое представление инструмента.
        Returns:
            Техническое представление для разработчика
        """
        return (f"MusicalInstrument(name='{self.name}', "
                f"manufacturer='{self.manufacturer}', "
                f"year={self.year}, price={self._price})")

    def play(self) -> str:
        """
        Метод для игры на инструменте.
        Returns:
            Строка с описанием игры на инструменте
        """
        return f"Играю на {self.name}"

    def tune(self) -> str:
        """
        Метод для настройки инструмента.
        Returns:
            Строка с описанием настройки
        """
        return f"Настраиваю {self.name}"
    def get_price(self) -> float:
        """
        Получить цену инструмента.
        Returns:
            Цена инструмента
        """
        return self._price

    def set_price(self, new_price: float) -> None:
        """
        Установить новую цену инструмента.
        Инкапсуляция _price позволяет проводить валидацию при изменении цены.
        Args:
            new_price: Новая цена инструмента
        Raises:
            ValueError: Если цена отрицательная
        """
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = new_price

class StringInstrument(MusicalInstrument):
    """
    Класс для представления струнного музыкального инструмента.
    Наследуется от MusicalInstrument.
    Attributes:
        name (str): Название инструмента
        manufacturer (str): Производитель инструмента
        year (int): Год выпуска
        _price (float): Цена инструмента
        strings_count (int): Количество струн
        _string_material (str): Материал струн (инкапсулирован для контроля типа материала)
    """

    def __init__(self, name: str, manufacturer: str, year: int, price: float,
                 strings_count: int, string_material: str) -> None:
        """
        Инициализация струнного инструмента.
        Расширяет конструктор базового класса, добавляя специфичные для струнных атрибуты.

        Args:
            name: Название инструмента
            manufacturer: Производитель инструмента
            year: Год выпуска
            price: Цена инструмента
            strings_count: Количество струн
            string_material: Материал струн (нейлон, сталь, кишка)
        """
        super().__init__(name, manufacturer, year, price)
        self.strings_count = strings_count
        self._string_material = string_material

    def __str__(self) -> str:
        """
        Возвращает строковое представление струнного инструмента.
        Перегружает метод базового класса для добавления информации о струнах.
        Returns:
            Расширенное строковое представление
        """
        base_str = super().__str__()
        return f"{base_str}, {self.strings_count} струн"

    def __repr__(self) -> str:
        """
        Возвращает техническое строковое представление струнного инструмента.
        Перегружает метод базового класса.
        Returns:
            Техническое представление для разработчика
        """
        return (f"StringInstrument(name='{self.name}', "
                f"manufacturer='{self.manufacturer}', "
                f"year={self.year}, price={self._price}, "
                f"strings_count={self.strings_count}, "
                f"string_material='{self._string_material}')")

    def play(self) -> str:
        """
        Метод для игры на струнном инструменте.
        Перегружает метод базового класса.
        Причина перегрузки: струнные инструменты имеют специфичный способ
        извлечения звука (щипком, смычком), что отличается от других типов инструментов.
        Returns:
            Строка с описанием игры на струнном инструменте
        """
        return f"Играю на струнном инструменте {self.name}, перебирая {self.strings_count} струн из {self._string_material}"

    def change_strings(self, new_material: str) -> str:
        """
        Метод для замены струн на инструменте.
        Специфичный метод только для струнных инструментов.

        Args:
            new_material: Новый материал струн
        Returns:
            Строка с описанием замены струн
        """
        old_material = self._string_material
        self._string_material = new_material
        return f"Заменил струны на струнном инструменте {self.name} с {old_material} на {new_material}"

    def get_string_material(self) -> str:
        """
        Получить материал струн.
        Returns:
            Материал струн
        """
        return self._string_material


class WindInstrument(MusicalInstrument):
    """
    Класс для представления духового музыкального инструмента.
    Наследуется от MusicalInstrument.
    Attributes:
        name (str): Название инструмента
        manufacturer (str): Производитель инструмента
        year (int): Год выпуска
        _price (float): Цена инструмента
        instrument_type (str): Тип духового инструмента (деревянный/медный)
        _mouthpiece_type (str): Тип мундштука (инкапсулирован для контроля совместимости)
    """

    def __init__(self, name: str, manufacturer: str, year: int, price: float,
                 instrument_type: str, mouthpiece_type: str) -> None:
        """
        Инициализация духового инструмента.
        Расширяет конструктор базового класса.
        Args:
            name: Название инструмента
            manufacturer: Производитель инструмента
            year: Год выпуска
            price: Цена инструмента
            instrument_type: Тип инструмента (деревянный/медный)
            mouthpiece_type: Тип мундштука
        """
        super().__init__(name, manufacturer, year, price)
        self.instrument_type = instrument_type
        self._mouthpiece_type = mouthpiece_type

    def __str__(self) -> str:
        """
        Возвращает строковое представление духового инструмента.
        Перегружает метод базового класса.
        Returns:
            Расширенное строковое представление
        """
        base_str = super().__str__()
        return f"{base_str}, тип: {self.instrument_type}"

    def __repr__(self) -> str:
        """
        Возвращает техническое строковое представление духового инструмента.
        Перегружает метод базового класса.
        Returns:
            Техническое представление для разработчика
        """
        return (f"WindInstrument(name='{self.name}', "
                f"manufacturer='{self.manufacturer}', "
                f"year={self.year}, price={self._price}, "
                f"instrument_type='{self.instrument_type}', "
                f"mouthpiece_type='{self._mouthpiece_type}')")
    def play(self) -> str:
        """
        Метод для игры на духовом инструменте.
        Перегружает метод базового класса.
        Причина перегрузки: духовые инструменты имеют уникальный способ
        извлечения звука через вдувание воздуха и использование мундштука,
        что кардинально отличается от других типов инструментов.
        Returns:
            Строка с описанием игры на духовом инструменте
        """
        return f"Играю на духовом инструменте {self.name}, вдувая воздух через мундштук {self._mouthpiece_type} типа"

    def clean_instrument(self) -> str:
        """
        Метод для чистки духового инструмента.
        Специфичный метод только для духовых инструментов.
        Returns:
            Строка с описанием чистки
        """
        return f"Чищу духовой инструмент {self.name} от конденсата и загрязнений"

    def get_mouthpiece_type(self) -> str:
        """
        Получить тип мундштука.
        Returns:
            Тип мундштука
        """
        return self._mouthpiece_type


if __name__ == "__main__":
    print(" Пример работы классов \n")

    guitar = StringInstrument(
        name="Акустическая гитара",
        manufacturer="Yamaha",
        year=2020,
        price=25000.0,
        strings_count=6,
        string_material="нейлон"
    )

    trumpet = WindInstrument(
        name="Труба",
        manufacturer="Bach",
        year=2019,
        price=75000.0,
        instrument_type="медный",
        mouthpiece_type="чашеобразный"
    )

    print("Струнный инструмент:")
    print(f"str: {str(guitar)}")
    print(f"repr: {repr(guitar)}")
    print(f"Игра: {guitar.play()}")
    print(f"Настройка: {guitar.tune()}")
    print(f"Цена: {guitar.get_price()} руб.")
    print(f"Материал струн: {guitar.get_string_material()}")
    print(f"{guitar.change_strings('сталь')}")
    print()

    print("Духовой инструмент:")
    print(f"str: {str(trumpet)}")
    print(f"repr: {repr(trumpet)}")
    print(f"Игра: {trumpet.play()}")
    print(f"Настройка: {trumpet.tune()}")
    print(f"Цена: {trumpet.get_price()} руб.")
    print(f"Тип мундштука: {trumpet.get_mouthpiece_type()}")
    print(f"{trumpet.clean_instrument()}")