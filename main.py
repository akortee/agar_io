"""Точка входа в программу."""

from src.app import App


def main() -> None:
    """Создаёт и запускает приложение."""
    App().run()


if __name__ == "__main__":
    main()
