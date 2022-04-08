# simulation_engine

The goal of this project is to create a generic platform using pyglet to run simulations.

Create custom classes which:
*describe behaviour
*expose variables to track and display

Create layers which:
*hold different collections of custom classes together
*allow custom classes to interact with each another inside a simulation space

The SimulationEngine will ingest the blueprints defined by you, and manage the graphics and event handling in the background.
