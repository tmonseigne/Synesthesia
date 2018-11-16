# CMakeList.txt : fichier projet CMake de niveau supérieur, effectuez une configuration globale
# et incluez les sous-projets ici.
#
cmake_minimum_required (VERSION 3.10)

project (Synesthesia)
set(VERSION 0.1)

# Incluez les dépendances.
add_subdirectory ("dependencies/wxWidgets")

# Paramètres CMAKE
set(CMAKE_CXX_STANDARD 17)		# Standard de Codage
set(CMAKE_BUILD_TYPE Release)	# Build par défaut
SET(CMAKE_INSTALL_PREFIX "${CMAKE_SOURCE_DIR}/build")

message(STATUS "
\tProject Name : ${PROJECT_NAME} ${VERSION}
\tCmake Version : ${CMAKE_VERSION}
\tStandard : ${CMAKE_CXX_STANDARD}
\tBuild Type: ${CMAKE_BUILD_TYPE}
\tBuild Directory: ${CMAKE_INSTALL_PREFIX}")

# Incluez les sous-projets.
#add_subdirectory ("src/gui")			# Aucun Cmake c'est un Qt maintenant
add_subdirectory ("src/sound-processing")
#add_subdirectory ("src/visualization")
#add_subdirectory ("src/tests")
