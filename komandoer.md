# python install location
C:\Users\Oyste\AppData\Local\Programs\Python\Python312\python.exe 

# create cmake folders and files innside cwd. skal kjøres fra ./build for å oprette filer
cmake -S ./src -G "Visual Studio 17 2022" -A x64 -DPython3_EXECUTABLE=C:\Users\Oyste\AppData\Local\Programs\Python\Python312\python.exe 

# build the cwd. skal kjøres fra ./build for å oprette filer
cmake --build . --config Release

# Create a file for the vs code intelisence. skal kjøres fra ./build/Release for å oprette filer
stubgen -m my_module -o .

# Buyilds the module and creates a .ipy file for intelisence
./build/src/build.cmd