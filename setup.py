from setuptools import setup, find_packages

setup(
    name="area_calc",
    version="1.0",
    description="SENG 560 reusable arithmatic library application.",
    packages=["area_calc", "ArithmeticLibrary"],
    package_dir={"area_calc": "src/area_calc", "ArithmeticLibrary": "src/ArithmeticLibrary"},
    setup_requires=["setuptools>=56.0"],
    python_requires=">= 3.8"
)