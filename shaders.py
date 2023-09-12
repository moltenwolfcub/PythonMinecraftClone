from typing import TYPE_CHECKING
from os.path import dirname

if TYPE_CHECKING:
	import moderngl
	from main import MinecraftClone

class Shaders:

	def __init__(self, mc: 'MinecraftClone') -> None:
		self.minecraft: 'MinecraftClone' = mc

		self.quad: 'moderngl.Program' = self.getShader(name="quad")
		
		self.setUniforms()

	def setUniforms(self):
		pass

	def update(self):
		pass

	def getShader(self, name: str) -> 'moderngl.Program':
		with open(f"{dirname(__file__)}/shaders/{name}.vert") as f:
			vertex = f.read()

		with open(f"{dirname(__file__)}/shaders/{name}.frag") as f:
			fragment = f.read()
		
		return self.minecraft.context.program(vertex_shader=vertex,fragment_shader=fragment)
