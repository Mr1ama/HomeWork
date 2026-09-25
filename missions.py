"""Данные и функции для каталога космических миссий."""

MISSIONS = [
    {"name": "Mars 2020", "year": 2020, "direction": "Марс"},
    {"name": "Artemis 1", "year": 2022, "direction": "Луна"},
    {"name": "Voyager 1", "year": 1977, "direction": "Дальний космос"},
    {"name": "Chandrayaan-3", "year": 2023, "direction": "Луна"},
]


def display_missions(missions):
    """Вывести миссии в удобном нумерованном формате."""
    for number, mission in enumerate(missions, start=1):
        print(f"{number}. {mission['name']}")
        print(f"Год запуска: {mission['year']}")
        print(f"Направление: {mission['direction']}")


def find_missions_by_direction(direction):
    """Вернуть миссии по направлению без учёта регистра."""
    normalized_direction = direction.strip().casefold()
    return [
        mission
        for mission in MISSIONS
        if mission["direction"].casefold() == normalized_direction
    ]