"""Модуль главного цикла приложения."""

from __future__ import annotations

import pygame

from src.models.animation_model import AgarModel
from src.renderers.renderer import Renderer


class App:
    """Управляет окном, событиями и игровым циклом."""

    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        fps: int = 60,
    ) -> None:
        """Инициализирует pygame, модель и рендерер."""
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode(
            (width, height)
        )
        pygame.display.set_caption("Agar.io")
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.fps: int = fps
        self.model: AgarModel = AgarModel(width=width, height=height)
        self.renderer: Renderer = Renderer(self.screen)

    def run(self) -> None:
        """Запускает главный цикл игры."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            mouse_pos = pygame.mouse.get_pos()
            self.model.update((float(mouse_pos[0]), float(mouse_pos[1])))
            self.renderer.draw(self.model)
            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()
