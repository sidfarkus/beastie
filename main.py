import pygame

pygame.init()

size = (320,240)
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

splash = pygame.image.load("splash.png")

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.fill((230, 240, 250))
  screen.blit(splash, (0, 0))

  pygame.display.flip()
  clock.tick(60)

pygame.quit()