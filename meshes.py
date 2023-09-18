from typing import TYPE_CHECKING

import numpy

from chunkMeshBuilder import buildChunkMesh

if TYPE_CHECKING:
	import moderngl

	from chunkManager import Chunk
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
		self.attributes = ('inPos', 'inColor')
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
	
class ChunkMesh(BaseMesh):
	def __init__(self, chunk: 'Chunk') -> None:
		super().__init__()

		self.chunk: 'Chunk' = chunk
		self.minecraft: 'MinecraftClone' = self.chunk.minecraft
		self.shader = self.minecraft.shaders.chunk
		self.context = self.minecraft.context

		self.vboFormat = '3u1 1u1 1u1'
		self.formatSize = sum(int(fmt[:1]) for fmt in self.vboFormat.split())
		self.attributes = ('inPos', 'inBlockId', 'inFaceId')

		self.vao = self.getVao()

	def getVertexData(self) -> numpy.ndarray:
		mesh = buildChunkMesh(
			self.chunk.blocks,
			self.formatSize
		)
		return mesh



if __name__ == '__main__':
	from main import main
	main()
