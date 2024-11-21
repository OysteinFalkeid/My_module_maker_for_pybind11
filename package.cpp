#include <pybind11/pybind11.h>

// Define the function in C++
int squared(int value) {
    return value * value;
}

// Create the Pybind11 module
PYBIND11_MODULE(my_c_library, m) {
    m.def("squared", &squared, "A function that returns the square of a number");
}
