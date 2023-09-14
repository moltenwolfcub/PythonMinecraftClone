#version 330 core

layout (location = 0) in ivec3 inPos;
layout (location = 1) in int inBlockId;
layout (location = 2) in int inFaceId;

uniform mat4 projection;
uniform mat4 view;
uniform mat4 model;

void main() {
	gl_Position = projection * view * model * vec4(inPos, 1.0);
}
