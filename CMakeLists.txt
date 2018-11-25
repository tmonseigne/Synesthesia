# CMakeList.txt : fichier projet CMake de niveau supérieur, effectuez une configuration globale
# et incluez les sous-projets ici.
#
cmake_minimum_required (VERSION 3.12)

project (Synesthesia)
set(VERSION 0.1)

# Incluez les dépendances.

# Paramètres CMAKE
set(CMAKE_CXX_STANDARD 17)		# Standard de Codage
set(CMAKE_BUILD_TYPE Release)	# Build par défaut
set(CMAKE_INSTALL_PREFIX "${CMAKE_SOURCE_DIR}/build")
set(BUILD_DOC TRUE)
set(BUILD_TESTS  TRUE)

message(STATUS "
\tProject Name : ${PROJECT_NAME} ${VERSION}
\tCmake Version : ${CMAKE_VERSION}
\tStandard : ${CMAKE_CXX_STANDARD}
\tBuild Type: ${CMAKE_BUILD_TYPE}
\tBuild Directory: ${CMAKE_INSTALL_PREFIX}
\tBuild Docs: ${BUILD_DOC}
\tBuild Tests: ${BUILD_TESTS}")

# Incluez les sous-projets.
#add_subdirectory ("src/gui")			# Aucun Cmake c'est un Qt maintenant
add_subdirectory ("src/sound-processing")
#add_subdirectory ("src/visualization")
#add_subdirectory("src/tests")

#Build Test
if(BUILD_TESTS)
	message("Tests build started")
else(BUILD_TESTS)
    message("Test is not build.")
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