cmake_minimum_required(VERSION 3.27+)
project(MyPythonModule LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add Pybind11
set(PYBIND11_FINDPYTHON ON)
find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG)

# Add subdirectories
add_subdirectory(src)
add_subdirectory(python)
add_subdirectory(tests)