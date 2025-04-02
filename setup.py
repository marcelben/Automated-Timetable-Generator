from setuptools import setup, find_packages

setup(
    name="timetable-generator",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'PyQt5>=5.15.0',
        'numpy>=1.19.0',
        'setuptools>=45.0.0',
    ],
    python_requires='>=3.7',
) 