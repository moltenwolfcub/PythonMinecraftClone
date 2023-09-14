#version 330 core

layout  (location = 0) in vec3 inPos;
layout  (location = 1) in vec3 inColor;

uniform mat4 projection;
uniform mat4 view;
uniform mat4 model;

out vec3 color;

void main() {
	color =  inColor;
	gl_Position = projection * view * model *vec4(inPos, 1.0);
}
