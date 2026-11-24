"""Модуль отрисовки игры Agar.io."""

from __future__ import annotations

import pygame

from src.models.animation_model import AgarModel

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Renderer:
    """Отрисовывает объекты модели и счётчик очков на экране."""

    def __init__(self, screen: pygame.Surface) -> None:
        """Сохраняет поверхность экрана и шрифт для счёта."""
        self.screen: pygame.Surface = screen
        self.font: pygame.font.Font = pygame.font.SysFont("arial", 24)

    def draw(self, model: AgarModel) -> None:
        """Очищает экран белым, рисует объекты и выводит счёт."""
        self.screen.fill(WHITE)
        for food in model.foods:
            pygame.draw.circle(
                self.screen,
                food.color,
                (int(food.x), int(food.y)),
                int(food.radius),
            )
        pygame.draw.circle(
            self.screen,
            model.player.color,
            (int(model.player.x), int(model.player.y)),
            int(model.player.radius),
        )
        score_surf = self.font.render(f"Очки: {model.score}", True, BLACK)
        self.screen.blit(score_surf, (15, 15))
