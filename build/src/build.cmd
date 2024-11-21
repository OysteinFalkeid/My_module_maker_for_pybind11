cd ./build
cmake --build . --config Release
cd ./Release
stubgen -m my_module -o . --include-docstrings