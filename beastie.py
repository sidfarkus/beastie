from dataclasses import dataclass
from typing import Any, List
import pygame

@dataclass
class Ability:
  name: str
  description: str

class Beastie:
  name: str
  description: str
  abilities: List[Ability]
  image_path: str
  cached_img: Any

  def __init__(self, name: str, description: str, abilities: List[Ability], image_path: str):
    self.name = name
    self.description = description
    self.abilities = abilities
    self.image_path = image_path

  def surface(self):
    if not self.cached_img:
      self.cached_img = pygame.image.load(self.image_path)
    return self.cached_img