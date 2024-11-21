#include <pybind11/pybind11.h> 

namespace py = pybind11;

float add(float a, float b) {
    return a + b + 2;
}

int fib(int n) {

    // If n is 1 or 0, then return n, works for 0th
      // and 1st terms
    if (n <= 1)
        return n;

    // Recurrence relation to find the rest of the
      // terms
    return fib(n - 1) + fib(n - 2);
}

PYBIND11_MODULE(my_module, m) {
    m.doc() = "Example module created with pybind11";
    m.def("add", &add, 
        "A function that adds two numbers \n"
        "\n"
        "Args:\n"
        "   a (float): first number\n"
        "   b (float): scound number\n"
        "\n"
        "Examples:\n"
        "   >>> add(2.0, 3.0)\n"
        "   5.0",
        py::arg("a"), py::arg("b"));
    m.def("fib", &fib, "returns fibonachi number n for n innput",
        py::arg("n"));
}
