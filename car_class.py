"""
Библиотека для создания ирархии классво в рамках проктики по Python
Релазованы 4 класса:
BaseCar
Car(BaseCar)
Truck(BaseCar)
SpecMachine(BaseCar)
"""

from os.path import splitext


class BaseCar:
    """
    Базовый класс автомобиля.
        example = BaseCar(car_type, brand, photo_file_name, carrying)

    Атрибуты:
        car_type (str): тип автомобиля. Допустимо: 'car', 'truck' или 'spec_machine'.
        brand (str): марка автомобиля.
        photo_file_name (str): имя файла с фото. Допустимо 'name.jpg'.
        carrying (float): грузоподъёмность, неотрицательное число.

    Методы:
        get_photo_file_ext(): вернуть расширение файла фото, например '.jpg'.
    """

    def __init__(self,
                 car_type: str,
                 brand: str,
                 photo_file_name: str,
                 carrying: float) -> None:
        """
        Инициализация класса BaseCar
        :param car_type (str): тип автомобиля. Допустимо: 'car', 'truck' или 'spec_machine'.
        :param brand (str): марка автомобиля.
        :param photo_file_name (str): имя файла с фото. Допустимо 'name.jpg'.
        :param carrying (float): грузоподъёмность, неотрицательное число.
        """
        self.car_type: str = car_type
        self.brand: str = brand
        self.photo_file_name: str = photo_file_name
        self.carrying: float = carrying

    def get_photo_file_ext(self) -> str:
        """
        Функция возвращает рассширение файла
        :return: str
        """
        return splitext(self.photo_file_name)[1]


class Car(BaseCar):
    """
    Легковой автомобиль.
    example = Car(brand, photo_file_name, carrying, passenger_seats_count)

    Атрибуты:
        car_type не указывается, всегда равен 'car'.
        brand (str): марка автомобиля.
        photo_file_name (str): имя файла с фото. Допустимо 'name.jpg'.
        carrying (float): грузоподъёмность, неотрицательное число.
        passenger_seats_count (int): пассажирские места, неотрицательное число.

    Методы:
        get_photo_file_ext(): вернуть расширение файла фото, например '.jpg'.
    """

    def __init__(self,
                 brand: str,
                 photo_file_name: str,
                 carrying: float,
                 passenger_seats_count: int) -> None:
        """
        Инициализация класса Car
        :param brand (str): марка автомобиля.
        :param photo_file_name (str): имя файла с фото. Допустимо 'name.jpg'.
        :param carrying (float): грузоподъёмность, неотрицательное число.
        :param passenger_seats_count (int): пассажирские места, неотрицательное число.
        """
        super().__init__("car", brand, photo_file_name, carrying)
        self.passenger_seats_count: int = passenger_seats_count


class Truck(BaseCar):
    """
    Грузовой автомобиль.
    example = Truck(brand, photo_file_name, carrying, body_whl)

    Атрибуты:
        car_type не указывается, всегда равен 'truck'.
        brand (str): марка автомобиля.
        photo_file_name (str): имя файла с фото. Допустимо 'name.jpg'.
        carrying (float): грузоподъёмность, неотрицательное число.
        body_whl (str): Размер кузова ДxШxВ, м, например '2.5x3x2'.

    Методы:
        get_photo_file_ext(): вернуть расширение файла фото, например '.jpg'.
        get_body_dimensions(): вернуть (длина, ширина, высота) кузова.
    """

    def __init__(self,
                 brand: str,
                 photo_file_name: str,
                 carrying: float,
                 body_whl: str) -> None:
        """
        Инициализация класса Truck
        :param brand (str): марка автомобиля.
        :param photo_file_name (str): имя файла с фото. Допустимо 'name.jpg'.
        :param carrying (float): грузоподъёмность, неотрицательное число.
        :param body_whl (str): Размер кузова ДxШxВ, м, например '2.5x3x2'.
        """
        super().__init__("truck", brand, photo_file_name, carrying)
        self.body_whl: str = body_whl
        self._parse_body_whl()

    def _parse_body_whl(self) -> None:
        """
        Парсит body_whl и задаёт свойства length, width, height
        :return: None
        """
        if not self.body_whl:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0
            return

        try:
            length_str, width_str, height_str = self.body_whl.split('x')
            self.body_length = float(length_str)
            self.body_width = float(width_str)
            self.body_height = float(height_str)
        except (ValueError):
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0

    def get_body_volume(self) -> float:
        """
        Объём кузова
        :return: float
        """
        return self.body_length * self.body_width * self.body_height


class SpecMachine(BaseCar):
    """
    СпецМашина.
    example = SpecMachine(brand, photo_file_name, carrying, extra)

    Атрибуты:
        car_type не указывается, всегда равен 'spec_machine'.
        brand (str): марка автомобиля.
        photo_file_name (str): имя файла с фото. Допустимо 'name.jpg'.
        carrying (float): грузоподъёмность, неотрицательное число.
        extra (str): Дополнительная информация.

    Методы:
        get_photo_file_ext(): вернуть расширение файла фото, например '.jpg'.
    """

    def __init__(self,
                 brand: str,
                 photo_file_name: str,
                 carrying: float,
                 extra: str) -> None:
        """
        Инициализация класса SpecMachine
        :param brand (str): марка автомобиля.
        :param photo_file_name (str): имя файла с фото. Допустимо 'name.jpg'.
        :param carrying (float): грузоподъёмность, неотрицательное число.
        :param extra (str): Дополнительная информация.
        """
        super().__init__("spec_machine", brand, photo_file_name, carrying)
        self.extra: str = extra


if __name__ == "__main__":
    # Проверка BaseCar
    base = BaseCar("car", "VAZ", "f1.jpeg", 2.0)
    assert base.car_type == "car", "error car_type!"
    assert base.car_type == "car", "BaseCar: неверный car_type"
    assert base.brand == "VAZ", "BaseCar: неверный brand"
    assert base.get_photo_file_ext() == ".jpeg", "BaseCar: неверное расширение файла"
    assert base.carrying == 2.0, "BaseCar: неверный carrying"

    # Проверка Car
    car = Car("Toyota", "c1.jpg", 1.5, 4)
    assert car.car_type == "car", "Car: неверный car_type"
    assert car.passenger_seats_count == 4, "Car: неверный passenger_seats_count"

    # Проверка Truck c корректным body_whl
    truck = Truck("MAN", "t1.jpg", 10.0, "2.0x3.0x4.0")
    assert truck.car_type == "truck", "Truck: неверный car_type"
    assert truck.body_length == 2.0, "Truck: неверная длина"
    assert truck.body_width == 3.0, "Truck: неверная ширина"
    assert truck.body_height == 4.0, "Truck: неверная высота"
    assert truck.get_body_volume() == 24.0, "Truck: неверный объём"

    # Проверка Truck с нулевыми размерами
    truck_zero = Truck("Volvo", "t2.jpg", 8.0, "0x0x0")
    assert truck_zero.body_whl == "0x0x0", "Truck: неверный truck_zero.body_whl"
    assert truck_zero.get_body_volume() == 0.0, "Truck: неверный truck_zero.get_body_volume"

    # Проверка SpecMachine
    spec = SpecMachine("CAT", "s1.png", 5.0, "буровая установка")
    assert spec.car_type == "spec_machine", "SpecMachine: неверный car_type"
    assert spec.extra == "буровая установка", "SpecMachine: неверный extra"
