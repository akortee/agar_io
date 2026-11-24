"""Модуль модели игры Agar.io."""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import List, Tuple

Color = Tuple[int, int, int]


def _random_color() -> Color:
    """Генерирует случайный цвет в формате RGB."""
    return (
        random.randint(30, 220),
        random.randint(30, 220),
        random.randint(30, 220),
    )


@dataclass
class Circle:
    """Модель круга на плоскости."""

    x: float
    y: float
    radius: float
    color: Color


class AgarModel:
    """Хранит состояние игрока, гранул и счёт, обновляя координаты."""

    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        food_count: int = 25,
    ) -> None:
        """Инициализирует игровое поле, объекты и счётчик очков."""
        self.width: int = width
        self.height: int = height
        self.food_count: int = food_count
        self.score: int = 0
        self.player: Circle = Circle(
            x=width / 2.0,
            y=height / 2.0,
            radius=15.0,
            color=_random_color(),
        )
        self.foods: List[Circle] = [
            self._make_food() for _ in range(self.food_count)
        ]

    def _make_food(self) -> Circle:
        """Создаёт гранулу со случайным цветом в случайной точке поля."""
        return Circle(
            x=random.uniform(10.0, self.width - 10.0),
            y=random.uniform(10.0, self.height - 10.0),
            radius=5.0,
            color=_random_color(),
        )

    def update(
        self,
        target: Tuple[float, float],
        speed: float = 4.0,
    ) -> None:
        """Плавно перемещает игрока к курсору и обрабатывает еду."""
        dx = target[0] - self.player.x
        dy = target[1] - self.player.y
        dist = math.hypot(dx, dy)

        if dist > 0.5:
            # Гасим скорость у центра, чтобы круг не перескакивал курсор
            slowdown = min(1.0, dist / max(1.0, self.player.radius))
            step = min(dist, speed * slowdown)
            self.player.x += (dx / dist) * step
            self.player.y += (dy / dist) * step

        for i, food in enumerate(self.foods):
            center_dist = math.hypot(
                self.player.x - food.x,
                self.player.y - food.y,
            )
            if center_dist < self.player.radius + food.radius:
                # Рост по площади: r_new = sqrt(r_player^2 + r_food^2)
                self.player.radius = math.hypot(
                    self.player.radius,
                    food.radius,
                )
                self.score += 1
                self.foods[i] = self._make_food()
