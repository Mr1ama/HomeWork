"""Точка входа в консольный каталог космических миссий."""

from missions import MISSIONS, display_missions, find_missions_by_direction


def main():
    print("=== Каталог космических миссий ===")
    display_missions(MISSIONS)


    direction = input("\nВведите направление для поиска: ")
    results = find_missions_by_direction(direction)

    print("=== Результаты поиска ===")
    if results:
        display_missions(results)
    else:
        print(f"Миссии по направлению «{direction.strip()}» не найдены.")


if __name__ == "__main__":
    main()