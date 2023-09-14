from typing import TYPE_CHECKING

import numpy

from meshes import ChunkMesh
from settings import *

if TYPE_CHECKING:
	from main import MinecraftClone

class Chunk:
	def __init__(self, mc: 'MinecraftClone') -> None:
		self.minecraft: 'MinecraftClone' = mc
		self.blocks: numpy.ndarray = self.createBlocks()
		self.mesh: ChunkMesh = None
		self.buildMesh()

	def render(self) -> None:
		self.mesh.render()
	
	def createBlocks(self) -> numpy.ndarray:
		blocks: numpy.ndarray = numpy.zeros(CHUNK_VOLUME, dtype='uint8') # uint8 might change to string in the future (mimicking mc 1.12 change of flattening to IDs)

		for x in range(CHUNK_SIZE):
			for y in range(CHUNK_SIZE):
				for z in range(CHUNK_SIZE):
					blocks[x + CHUNK_SIZE*z + CHUNK_SIZE*CHUNK_SIZE*y] = 1
		
		return blocks

	def buildMesh(self) -> None:
		self.mesh = ChunkMesh(self)



if __name__ == '__main__':
	from main import main
	main()
