import pygame
import os
from beastie import Beastie

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

size = (320,240)
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)

done = False
clock = pygame.time.Clock()

splash = pygame.image.load("splash.png")
splash_duration = 5000.0

active = 0
beasties = [
  Beastie(name="cubey", description="A cubey", abilities=[], image_path="cubey1.png"),
  Beastie(name="slimo", description="Found in valleys", abilities=[], image_path="slimo.png"),
  Beastie(name="circles", description="Sir Circles the XXVII", abilities=[], image_path="sircirclesI.png")
]

def render_active_beastie(screen, beastie):
  screen.blit(beastie.surface(), (0, 0))

while not done:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        done = True
      if event.key == pygame.K_UP:
        active = (active - 1) % len(beasties)
      if event.key == pygame.K_DOWN:
        active = (active + 1) % len(beasties)
    if event.type == pygame.QUIT:
      done = True

  screen.fill((230, 240, 250))

  if splash_duration >= 0:
    screen.blit(splash, (0, 0))
    splash_duration -= clock.get_time()
  else:
    render_active_beastie(screen, beasties[active])

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
