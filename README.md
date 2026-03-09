# Bethe-Bloch Energy Loss Simulation

This project simulates the energy loss of charged particles passing through matter using the Bethe-Bloch formula.

The simulation computes the stopping power (dE/dx) as a function of particle velocity and visualizes the characteristic Bethe-Bloch curve.

## Physics Background

Charged particles lose energy when passing through matter due to ionization and excitation of atoms.

The mean energy loss is described by the Bethe-Bloch formula:

dE/dx ∝ (z²/β²) [ ln(2me β²γ² / I) − β² ]

where

- β = v/c
- γ = Lorentz factor
- z = particle charge
- I = mean excitation potential

## Output

The program produces the Bethe-Bloch curve showing energy loss as a function of βγ.

## Run
Install dependencies:

pip install numpy matplotlib

Run the simulation:

python simulation.py

Install dependencies:
### Dependencies

The simulation requires the following Python libraries:

- numpy
- matplotlib
- ## Applications

This simulation is relevant for:

- particle detector physics
- high energy physics experiments
- radiation energy loss studies
- detector design and particle tracking
