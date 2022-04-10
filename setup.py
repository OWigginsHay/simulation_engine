from setuptools import setup, find_packages

setup(
    name='simeng',
    version='0.0.1',
    description='Simulation Engine for prototyping system behaviour',
    packages=find_packages(include=['simeng', 'simeng.*', 'simeng.data_structs']),
    package_data={"simeng": ['py.typed']},
    install_requires=[
        'pyglet'
    ]
)