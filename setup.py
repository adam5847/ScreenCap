from setuptools import  setup
from setuptools import find_packages

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='ScreenCap',
    version='0.0.1',
    author='Adam Lukavec',
    url='https://github.com/adam5847/ScreenCap',
    author_email='ada.lukavec@gmail.com',
    description='This package includes program ScreenCap, which allows you to take screenshots and recordings of your screen.',
    license="GPL-3.0 License",
    install_requires=REQUIREMENTS,
    packages=find_packages(),
    keywords=['python', 'screenshot', 'ScreenCap', 'screenrecord'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)