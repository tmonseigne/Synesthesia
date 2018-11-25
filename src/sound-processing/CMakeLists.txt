cmake_minimum_required (VERSION 3.10)

project(sound-hello-world)


set(SRC_FILES 

	main.cpp
)

add_executable(${PROJECT_NAME} ${SRC_FILES})
