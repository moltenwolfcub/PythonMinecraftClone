import glm

from settings import *

class Camera:
	def __init__(self, pos: glm.vec3, yaw: float, pitch: float) -> None:
		self.pos: glm.vec3 = glm.vec3(pos)
		self.yaw: float = glm.radians(yaw)
		self.pitch: float = glm.radians(pitch)

		self.up: glm.vec3 = glm.vec3(0, 1, 0)
		self.right: glm.vec3 = glm.vec3(1, 0, 0)
		self.forwards: glm.vec3 = glm.vec3(0, 0, -1)

		self.projection: glm.mat4x4 = glm.perspective(VERTICAL_FOV, ASPECT_RATIO, NEAR_FRUSTUM, FAR_FRUSTUM)
		self.view: glm.mat4x4 = glm.mat4()

	def update(self) -> None:
		self.updateVectors()
		self.updateViewMatrix()

	def updateViewMatrix(self) -> None:
		self.view = glm.lookAt(self.pos, self.pos +self.forwards, self.up)

	def updateVectors(self) -> None:
		self.forwards.x = glm.cos(self.yaw) * glm.cos(self.pitch)
		self.forwards.y = glm.sin(self.pitch)
		self.forwards.z = glm.sin(self.yaw) * glm.cos(self.pitch)
		self.forwards = glm.normalize(self.forwards)

		self.right = glm.normalize(glm.cross(self.forwards, glm.vec3(0, 1, 0)))

		self.up = glm.normalize(glm.cross(self.right, self.forwards))

	def rotPitch(self, delta_y):
		self.pitch -= delta_y
		self.pitch = glm.clamp(self.pitch, -MAX_PITCH, MAX_PITCH)

	def rotYaw(self, delta_x):
		self.yaw += delta_x

	def moveLeft(self, velocity):
		self.pos -= self.right * velocity

	def moveRight(self, velocity):
		self.pos += self.right * velocity

	def moveUp(self, velocity):
		self.pos += self.up * velocity

	def moveDown(self, velocity):
		self.pos -= self.up * velocity

	def moveForward(self, velocity):
		self.pos += self.forwards * velocity

	def moveBack(self, velocity):
		self.pos -= self.forwards * velocity
