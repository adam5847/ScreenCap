from setuptools import  setup
from setuptools import find_packages
from os import path

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

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
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data = True,
    entry_points={
        'console_scripts': [ 'ScreenCap=ScreenCap.screencap:main']
    }
)