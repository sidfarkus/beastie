from dataclasses import dataclass
from typing import Any
import pygame

@dataclass
class Ability:
  name: str
  description: str

@dataclass
class Beastie:
  name: str
  description: str
  abilities: List[Ability]
  image_path: str
  cached_img: Any

  def surface(self):
    if not cached_img:
      cached_img = pygame.image.load(self.image_path)
    return cached_img