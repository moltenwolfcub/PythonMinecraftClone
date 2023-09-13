import numpy

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	import moderngl
	from main import MinecraftClone

class BaseMesh:
	def __init__(self) -> None:
		self.context: 'moderngl.Context' = None
		self.shader: 'moderngl.Program' = None
		self.vboFormat: str = None
		self.attributes: tuple[str, ...] = None
		self.vao: 'moderngl.VertexArray' = None

	def getVertexData(self) -> numpy.ndarray: ...

	def getVao(self) -> 'moderngl.VertexArray':
		vertexData = self.getVertexData()
		vbo = self.context.buffer(vertexData)
		vao = self.context.vertex_array(self.shader, [(vbo, self.vboFormat, *self.attributes)], skip_errors=True)
		return vao
	
	def render(self) -> None:
		self.vao.render()


class QuadMesh(BaseMesh):
	def __init__(self, mc: 'MinecraftClone') -> None:
		super().__init__()

		self.minecraft: 'MinecraftClone' = mc
		self.context = self.minecraft.context

		self.shader = self.minecraft.shaders.quad
		self.vboFormat = '3f 3f'
		self.attributes = ('in_position', 'in_color')
		self.vao = self.getVao()

	def getVertexData(self) -> numpy.ndarray:
		verticies = [
			(0.5, 0.5, 0.0), (-0.5, 0.5, 0.0), (-0.5, -0.5, 0.0),
			(0.5, 0.5, 0.0), (-0.5, -0.5, 0.0), (0.5, -0.5, 0.0),
		]
		colors = [
			(0, 1, 0), (1, 0, 0), (1, 1, 0),
			(0, 1, 0), (1, 1, 0), (0, 0, 1),
		]
		return numpy.hstack([verticies, colors], dtype='float32')



if __name__ == '__main__':
	from main import main
	main()
