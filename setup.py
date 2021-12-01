from setuptools import setup, find_packages

setup(
    name='simeng',
    version='0.0.1',
    packages=find_packages(include=['simeng', 'simeng.*']),
    install_requires=[
        'pyglet'
    ]
)