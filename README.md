# create cmake folders and files innside cwd. Run from ./build
cmake -S ./src -G "Visual Studio 17 2022" -A x64 -DPython3_EXECUTABLE=C:\Users\Username\AppData\Local\Programs\Python\Python312\python.exe 

# build the cwd. skal kjøres fra ./build for å oprette filer
cmake --build . --config Release

# Create a file for the vs code intelisence. Run from ./build/Release
stubgen -m my_module -o . --include-docstrings

# Buyilds the module and creates a .ipy file for intelisence
./build/src/build.cmd