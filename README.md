# create cmake folders and files innside cwd. Run from ./build
cmake -S ./src -G "Visual Studio 17 2022" -A x64 -DPython3_EXECUTABLE=C:\Users\Username\AppData\Local\Programs\Python\Python312\python.exe 

# build the cwd. skal kjøres fra ./build for å oprette filer
cmake --build . --config Release

# Create a file for the vs code intelisence. Run from ./build/Release
stubgen -m my_module -o . --include-docstrings

# Buyilds the module and creates a .ipy file for intelisence
./build/src/build.cmd

# new code structure supports
cmake .. -G "Visual Studio 17 2022" -A x64



# Add Python tests (e.g., using pytest)
add_custom_target(pytest ALL COMMAND pytest ${CMAKE_CURRENT_SOURCE_DIR})




# Get the location of the built module
set(MODULE_OUTPUT_DIR ${CMAKE_BINARY_DIR}/python/Release)

# Add a custom command for pytest
add_custom_target(pytest
    COMMAND pytest ${CMAKE_CURRENT_SOURCE_DIR}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Running pytest"
    ENVIRONMENT PYTHONPATH=${MODULE_OUTPUT_DIR}
)

# Add a CTest to run pytest
add_test(NAME pytest
    COMMAND ${Python3_EXECUTABLE} -m pytest ${CMAKE_CURRENT_SOURCE_DIR}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    # ENVIRONMENT PYTHONPATH=${MODULE_OUTPUT_DIR}
)
