import sys

import pygame
import moderngl

from settings import *
from shaders import Shaders
from scene import Scene
from player import Player

class MinecraftClone:

	def __init__(self) -> None:
		pygame.init()
		pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
		pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
		pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
		pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 24)

		pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), flags= pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
		pygame.display.set_caption("Minecraft Clone - 0 FPS")

		self.context = moderngl.create_context()
		self.context.enable(flags= moderngl.DEPTH_TEST | moderngl.CULL_FACE | moderngl.BLEND)
		self.context.gc_mode = 'auto'

		self.clock = pygame.time.Clock()
		self.deltaTime: int = 0
		self.time: int = 0

		self.mouseCaught: bool = True

		self.running = True

		self.onInit()

	def onInit(self) -> None:
		self.player = Player(self)
		self.shaders = Shaders(self)
		self.scene = Scene(self)

	def update(self) -> None:
		pygame.event.set_grab(self.mouseCaught)
		pygame.mouse.set_visible(not self.mouseCaught)

		self.player.update()
		self.shaders.update()
		self.scene.update()

		self.deltaTime = self.clock.tick()
		self.time = pygame.time.get_ticks()*0.001

		pygame.display.set_caption(f"Minecraft Clone - {self.clock.get_fps() :.0f} FPS")

	def render(self) -> None:
		self.context.clear(color=BG_COLOR)

		self.scene.render()

		pygame.display.flip()

	def handleEvents(self) -> None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN:
				self._handleKeydownEvents(event)

	def _handleKeydownEvents(self, event: pygame.event.Event) -> None:
		if event.key == pygame.K_ESCAPE:
			if not self.mouseCaught:
				self.toggleMouseCaught()
			else:
				self.running = False
		elif event.key == pygame.K_t:
			self.toggleMouseCaught()

	def toggleMouseCaught(self) -> None:
		w,h = pygame.display.get_window_size()
		pygame.mouse.set_pos(w/2, h/2)
		pygame.mouse.get_rel()
		self.mouseCaught = not self.mouseCaught


	def run(self) -> None:
		while self.running:
			self.handleEvents()
			self.update()
			self.render()
		
		self.exit()
		
	def exit(self) -> None:
		pygame.quit()
		sys.exit()

if __name__ == '__main__':
	instance = MinecraftClone()
	instance.run()
