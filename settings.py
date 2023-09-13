import glm

WINDOW_WIDTH: int = 1600
WINDOW_HEIGHT: int = 900

BG_COLOR: glm.vec3 = glm.vec3(0.1,0.15,0.25)

ASPECT_RATIO: float = WINDOW_WIDTH / WINDOW_HEIGHT
FOV: float = 50
VERTICAL_FOV: float = glm.radians(FOV)
HORIZONTAL_FOV: float = 2 * glm.atan(glm.tan(VERTICAL_FOV / 2) * ASPECT_RATIO)
NEAR_FRUSTUM: float = 0.1
FAR_FRUSTUM: float = 2000.0
MAX_PITCH: float =  glm.radians(89)

MOVEMENT_SPEED: float = 0.005
ROATATION_SPEED: float = 0.003
SENSITIVITY: float = 0.005



if __name__ == '__main__':
	from main import main
	main()
