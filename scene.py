

from typing import TYPE_CHECKING

from meshes import QuadMesh

if TYPE_CHECKING:
	from main import MinecraftClone

class Scene:
	def __init__(self, mc: 'MinecraftClone') -> None:
		self.minecraft: 'MinecraftClone' = mc

		self.quad: QuadMesh = QuadMesh(self.minecraft)
	
	def update(self) -> None:
		pass

	def render(self) -> None:
		self.quad.render()



if __name__ == '__main__':
	from main import main
	main()
