# crate project with Visual Studio 17 2022 and Python 3.12

pip install pybind11 pytest python-dev-tools wheel

install cmake on the computer and from the repo project run:

mkdir build
cd ./build

# create cmake folders and files innside cwd. Run from ./build
cmake -S .. -G "Visual Studio 17 2022" -A x64 -D Python3_EXECUTABLE=C:\Users\Username\AppData\Local\Programs\Python\Python312\python.exe 

change Username for your username. 
