"""Точка входа в консольный каталог космических миссий."""

from missions import MISSIONS, display_missions


def main():
    print("=== Каталог космических миссий ===")
    display_missions(MISSIONS)

if __name__ == "__main__":
    main()