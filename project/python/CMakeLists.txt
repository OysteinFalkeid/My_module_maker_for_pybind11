# Create a shared library for the Python module
pybind11_add_module(my_python_module bindings.cpp)

target_link_libraries(my_python_module PRIVATE my_core)
