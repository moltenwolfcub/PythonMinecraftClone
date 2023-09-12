import pygame
from typing import TYPE_CHECKING

from settings import *
from camera import Camera

if TYPE_CHECKING:
	import glm
	from main import MinecraftClone

class Player(Camera):
	def __init__(self, minecraft: 'MinecraftClone', pos: glm.vec3=glm.vec3(0,0,1), yaw: float=-90, pitch: float=0) -> None:
		super().__init__(pos, yaw, pitch)
		self.minecraft: 'MinecraftClone' = minecraft

	def update(self) -> None:
		self.keyboardControls()
		self.mouseControls()

		super().update()

	def mouseControls(self) -> None:
		dx, dy = pygame.mouse.get_rel()
		if dx:
			self.rotYaw(dx * SENSITIVITY)
		if dy:
			self.rotPitch(dy * SENSITIVITY)

	def keyboardControls(self) -> None:
		pressed = pygame.key.get_pressed()
		velocity = MOVEMENT_SPEED * self.minecraft.deltaTime
		if pressed[pygame.K_w]:
			self.moveForward(velocity)
		if pressed[pygame.K_s]:
			self.moveBack(velocity)
		if pressed[pygame.K_a]:
			self.moveLeft(velocity)
		if pressed[pygame.K_d]:
			self.moveRight(velocity)
		if pressed[pygame.K_LSHIFT]:
			self.moveDown(velocity)
		if pressed[pygame.K_SPACE]:
			self.moveUp(velocity)
