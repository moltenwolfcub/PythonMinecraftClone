from typing import TYPE_CHECKING

from chunkManager import Chunk
from meshes import QuadMesh

if TYPE_CHECKING:
	from main import MinecraftClone

class Scene:
	def __init__(self, mc: 'MinecraftClone') -> None:
		self.minecraft: 'MinecraftClone' = mc

		self.chunk: Chunk = Chunk(self.minecraft)
	
	def update(self) -> None:
		pass

	def render(self) -> None:
		self.chunk.render()



if __name__ == '__main__':
	from main import main
	main()
