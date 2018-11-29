cmake_minimum_required (VERSION 3.12)

project (Synesthesia
		VERSION 1.0
		DESCRIPTION "Synesthesia"
		LANGUAGES CXX)

# CMAKE Parameters
set(CMAKE_CXX_STANDARD 17)		# Standard
set(CMAKE_BUILD_TYPE Release)	# Default Build
set(CMAKE_INSTALL_PREFIX "${CMAKE_SOURCE_DIR}/build")
set(BUILD_TESTS  TRUE)
set(BUILD_DOC TRUE)

# Dependencies List
FILE(GLOB children RELATIVE ${CMAKE_SOURCE_DIR}/dependencies/ ${CMAKE_SOURCE_DIR}/dependencies/*)
SET(DEPENDENCIES_LIST "")
FOREACH(child ${children})
	IF(IS_DIRECTORY ${CMAKE_SOURCE_DIR}/dependencies/${child})
		LIST(APPEND DEPENDENCIES_LIST ${child})
	ENDIF()
ENDFOREACH()

message(STATUS "
\tProject Name : ${PROJECT_NAME} ${VERSION}
\tCmake Version : ${CMAKE_VERSION}
\tStandard : ${CMAKE_CXX_STANDARD}
\tBuild Type: ${CMAKE_BUILD_TYPE}
\tBuild Directory: ${CMAKE_INSTALL_PREFIX}
\tDependencies list : ${DEPENDENCIES_LIST}
\tBuild Docs: ${BUILD_DOC}
\tBuild Tests: ${BUILD_TESTS}")


#add_subdirectory ("src/gui")			# No CMake yet only Qmake
add_subdirectory ("src/sound-processing")
#add_subdirectory ("src/visualization")

#Build Test
if(BUILD_TESTS)
	add_subdirectory("tests")
endif(BUILD_TESTS)

#Build Documentation
if(BUILD_DOC)
	find_package(Doxygen)
	if(DOXYGEN_FOUND)
		set(BUILD_DOC_DIR ${CMAKE_SOURCE_DIR}/build/docs)
		if(NOT EXISTS ${BUILD_DOC_DIR})
		file(MAKE_DIRECTORY ${BUILD_DOC_DIR})
		endif()
		set(DOXYFILE ${CMAKE_CURRENT_SOURCE_DIR}/docs/Doxyfile)
		message("Doxygen build started")
		add_custom_target(Doxygen ALL
				COMMAND ${DOXYGEN_EXECUTABLE} ${DOXYFILE}
				WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/docs/
				COMMENT "Generating API documentation with Doxygen"
				VERBATIM)
	else(DOXYGEN_FOUND)
		message("Doxygen needs to be installed to generate the documentation.")
	endif(DOXYGEN_FOUND)
endif(BUILD_DOC)
