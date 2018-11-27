cmake_minimum_required (VERSION 3.12)

project(sound-hello-world
	VERSION 1.0
	DESCRIPTION "Hello World sound Project"
	LANGUAGES CXX)

set(SRC_FILES
	main.cpp
)

add_executable(${PROJECT_NAME} ${SRC_FILES})
