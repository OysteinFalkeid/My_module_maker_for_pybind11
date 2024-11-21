cmake_minimum_required(VERSION 3.10)

project(my_module)

# Find Python
find_package(Python3 REQUIRED COMPONENTS Development)
find_package(pybind11 REQUIRED)

# Define the module
pybind11_add_module(my_module my_module.cpp)