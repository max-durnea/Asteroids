import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init
	screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	clock=pygame.time.Clock()
	dt=0
	player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
	updatable=pygame.sprite.Group()
	drawable=pygame.sprite.Group()
	asteroids=pygame.sprite.Group()
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	shots=pygame.sprite.Group()
	Shot.containers = (updatable, drawable, shots)
	updatable.add(player)
	drawable.add(player)
	AsteroidField()
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		for sprite in updatable:
			sprite.update(dt)
		for asteroid in asteroids:
			if player.collides_with(asteroid):
				print("Game Over!")
				return
			for shot in shots:
				if asteroid.collides_with(shot):
					asteroid.split()
					shot.kill()
		screen.fill("black")
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip()

		dt=clock.tick(60)/1000


if __name__ == "__main__":
	main()