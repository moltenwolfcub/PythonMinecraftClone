import numpy

from settings import *


def buildChunkMesh(chunkBlocks: 'numpy.ndarray', formatSize: int) -> 'numpy.ndarray':
	vertexData: numpy.ndarray = numpy.empty(CHUNK_VOLUME * 18 * formatSize, dtype="uint8")
	index: int = 0

	for x in range(CHUNK_SIZE):
		for y in range(CHUNK_SIZE):
			for z in range(CHUNK_SIZE):
				blockId = chunkBlocks[x + CHUNK_SIZE*z + CHUNK_SIZE*CHUNK_SIZE*y]
				if blockId == 0:
					continue

				if isVoid((x,y+1,z), chunkBlocks):
					v0 = (x, y+1, z, blockId, 0)
					v1 = (x+1, y+1, z, blockId, 0)
					v2 = (x, y+1, z+1, blockId, 0)
					v3 = (x+1, y+1, z+1, blockId, 0)

					index = addVertexData(vertexData, index, v0, v2, v3, v0, v3, v1)

				if isVoid((x,y-1,z), chunkBlocks):
					v0 = (x, y, z, blockId, 1)
					v1 = (x+1, y, z, blockId, 1)
					v2 = (x, y, z+1, blockId, 1)
					v3 = (x+1, y, z+1, blockId, 1)

					index = addVertexData(vertexData, index, v0, v3, v2, v0, v1, v3)

				if isVoid((x+1,y,z), chunkBlocks):
					v0 = (x+1, y, z, blockId, 2)
					v1 = (x+1, y+1, z, blockId, 2)
					v2 = (x+1, y, z+1, blockId, 2)
					v3 = (x+1, y+1, z+1, blockId, 2)

					index = addVertexData(vertexData, index, v0, v1, v3, v0, v3, v2)

				if isVoid((x-1,y,z), chunkBlocks):
					v0 = (x, y, z, blockId, 3)
					v1 = (x, y+1, z, blockId, 3)
					v2 = (x, y, z+1, blockId, 3)
					v3 = (x, y+1, z+1, blockId, 3)

					index = addVertexData(vertexData, index, v0, v3, v1, v0, v2, v3)

				if isVoid((x,y,z-1), chunkBlocks):
					v0 = (x, y, z, blockId, 4)
					v1 = (x+1, y, z, blockId, 4)
					v2 = (x, y+1, z, blockId, 4)
					v3 = (x+1, y+1, z, blockId, 4)

					index = addVertexData(vertexData, index, v0, v2, v3, v0, v3, v1)

				if isVoid((x,y,z+1), chunkBlocks):
					v0 = (x, y, z+1, blockId, 5)
					v1 = (x+1, y, z+1, blockId, 5)
					v2 = (x, y+1, z+1, blockId, 5)
					v3 = (x+1, y+1, z+1, blockId, 5)

					index = addVertexData(vertexData, index, v0, v3, v2, v0, v1, v3)
	return vertexData[:index+1]

def isVoid(blockPos: tuple[int, int, int], chunkBlocks: 'numpy.ndarray') -> bool:
	x, y, z = blockPos
	if 0 <= x < CHUNK_SIZE and 0 <= y < CHUNK_SIZE and 0 <= z < CHUNK_SIZE:
		if chunkBlocks[x + CHUNK_SIZE*z + CHUNK_SIZE*CHUNK_SIZE*y] != 0:
			return False
	return True

def addVertexData(vertexData: numpy.ndarray, index: int, *vertices: tuple[int, int, int, int, int]) -> int:
	for vertex in vertices:
		for attribute in vertex:
			vertexData[index] = attribute
			index+=1
	return index



if __name__ == '__main__':
	from main import main
	main()
