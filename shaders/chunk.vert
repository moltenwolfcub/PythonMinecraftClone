#version 330 core

layout  (location = 0) in ivec3 inPos;
layout  (location = 1) in int inBlockId;
layout  (location = 2) in int inFaceId;

uniform mat4 projection;
uniform mat4 view;
uniform mat4 model;

out vec3 color;

void main() {
	color = vec3(inBlockId,0,1);
	gl_Position = projection * view * model * vec4(inPos, 1.0);
}

// #version 330 core

// layout (location = 0) in ivec3 inPos;
// layout (location = 1) in int inBlockId;
// layout (location = 2) in int inFaceId;

// uniform mat4 projection;
// uniform mat4 view;
// uniform mat4 model;

// void main() {
// 	gl_Position = projection * view * model * vec4(inPos, 1.0);
// }
