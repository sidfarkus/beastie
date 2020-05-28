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
splash_duration = 5

active = 0
beasties = [
  Beastie(name="glubglub", description="A glubglub", abilities=[], image_path="beastie1.png"),
  Beastie(name="fizzle", description="zzordk", abilities=[], image_path="beastie2.png")
]

def render_active_beastie(screen, beastie):
  screen.blit(beastie.surface(), (0, 0))

while not done:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.locals.K_ESCAPE:
        done = True
      if event.key == pygame.locals.K_UP:
        active = (active - 1) % len(beasties)
      if event.key == pygame.locals.K_DOWN:
        active = (active + 1) % len(beasties)
    if event.type == pygame.QUIT:
      done = True

  screen.fill((230, 240, 250))

  if splash_duration >= 0:
    screen.blit(splash, (0, 0))
  else:
    render_active_beastie(screen, beasties[active])

  pygame.display.flip()
  clock.tick(60)

pygame.quit()