#include <pybind11/pybind11.h>

namespace py = pybind11;

int add(int a, int b) {
    return a + b + 2;
}

PYBIND11_MODULE(my_module, m) {
    m.doc() = "Example module created with pybind11";
    m.def("add", &add, "A function that adds two numbers",
        py::arg("i"), py::arg("j"));
}
