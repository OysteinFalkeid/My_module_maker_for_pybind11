from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext
import subprocess

subprocess.check_call([
    "cmake",
    "--build", "./build",
    "--config", "Release"
])

subprocess.check_call([
    "./build/tests/Release/test_cpp.exe"
])

class CustomBuildExt(build_ext):
    def run(self):
        # Build the extension first
        super().run()
        
        # After building, generate stubs
        module_name = "my_python_module"
        output_dir = "."
        try:
            subprocess.check_call([
                "stubgen",
                "-m", module_name,
                "-o", output_dir,
                "--include-docstrings"
            ])
            print(f"Type stubs generated for {module_name} in {output_dir}")
        except FileNotFoundError:
            print("Error: stubgen is not installed. Install it with 'pip install mypy'.")
        except subprocess.CalledProcessError as e:
            print(f"stubgen failed with error: {e}")
            
ext_modules = [
    Pybind11Extension(
        "my_python_module",
        ["python/bindings.cpp", "src/my_module.cpp"],
        include_dirs=["include"],
    ),
]

setup(
    name="my_python_module",
    version="0.1.0",
    ext_modules=ext_modules,
    cmdclass={"build_ext": CustomBuildExt},
)
