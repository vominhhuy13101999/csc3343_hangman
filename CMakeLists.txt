
cmake_minimum_required(VERSION 3.20)

# set the project name
project(search)

# add the executable
add_executable(search main.cpp)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)

#find_package(PythonLibs REQUIRED)
#include_directories(${PYTHON_INCLUDE_DIRS})
##target_link_libraries(<search> ${PYTHON_LIBRARIES})
#cmake --help-module FindPythonLibs
#cmake --help-command find_package
#cmake --help-command include_directories
#cmake --help-command target_link_libraries