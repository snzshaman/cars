"""
Программа для импорта cars.csv в рамках проктики по Python
Имортирует cars.csv с машинами и разбирает машины по классам.
Реализованы различне проверки корректности данных.
"""
import csv
from os.path import splitext
from car_class import BaseCar, Car, Truck, SpecMachine  # используем наши классы


def get_car_list(csv_filename) -> list[BaseCar]:
    """
    Читает CSV-файл построчно.
    Если строка с ошабкой, выводит номер строки и ошибку.
    Если строка без ошибок, добавляет строку в car_list.
    :param csv_filename: str
    :return: list[BaseCar]
    """

    car_list = []
    car_types = ["car", "truck", "spec_machine"]

    with open(csv_filename, encoding="utf-8") as csv_fd:
        reader = csv.reader(csv_fd, delimiter=";")
        headers = next(reader)
        for line_num, row in enumerate(reader, start=2):
            if not row or len(row) < 7:
                print(f"Строка {line_num}: недостаточно колонок → {row}")
                continue

            car_type, brand, seats_raw, \
                photo_file_name, body_whl_raw, \
                carrying_raw, extra_raw = map(str.strip, row)

            # car_type
            if car_type not in car_types:
                print(f"Строка {line_num}: некорректный car_type = {car_type!r}")
                continue

            # brand
            if not brand:
                print(f"Строка {line_num}: пустой brand")
                continue

            # carrying
            try:
                carrying = float(carrying_raw)
            except (ValueError):
                print(f"Строка {line_num}: carrying не число = {carrying_raw!r}")
                continue
            if carrying < 0:
                print(f"Строка {line_num}: carrying < 0 = {carrying}")
                continue

            # создаём объект по типу
            match car_type:
                case "car":
                    try:
                        passenger_seats_count = int(seats_raw)
                        obj = Car(brand, photo_file_name, carrying, passenger_seats_count)
                    except (ValueError):
                        print(f"Строка {line_num}: некорректный passenger_seats_count = {seats_raw!r}")
                        continue

                case "truck":
                    body_whl = body_whl_raw.strip()
                    if body_whl and len(body_whl.split("x")) != 3:
                        print(f"Строка {line_num}: некорректный body_whl = {body_whl!r}")
                        continue
                    obj = Truck(brand, photo_file_name, carrying, body_whl)

                case "spec_machine":
                    extra = extra_raw.strip()
                    if not extra:
                        print(f"Строка {line_num}: пустое extra для spec_machine")
                        continue
                    obj = SpecMachine(brand, photo_file_name, carrying, extra)

                case _:
                    print(f"Строка {line_num}: неизвестный car_type = {car_type}")
                    continue

            car_list.append(obj)

    return car_list


if __name__ == "__main__":
    cars = get_car_list("cars.csv")
    print(cars)

    # шапка
    print(f"    type     |      brand     | seats |   photo   |   body_whl    | carrying | extra")

    for c in cars:
        match c:
            case Car():
                body = "-"
                seats = c.passenger_seats_count
                extra = "-"
            case Truck():
                body = f"{c.body_length}x{c.body_width}x{c.body_height}"
                seats = "-"
                extra = "-"
            case SpecMachine():
                body = "-"
                seats = "-"
                extra = c.extra

        print(f"{c.car_type:<12} | {c.brand:<14} | {seats:<5} | "
              f"{c.photo_file_name:<9} | {body:<13} | {c.carrying:<8} | {extra}")
