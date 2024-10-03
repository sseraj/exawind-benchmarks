

# Airfoil verification and validation 1: NASA NLF(1)-0416

A grid sensitivity study was performed for NASA NLF(1)-0416 airfoil using Nalu-Wind with the 1-eq gamma transition model.
Six different mesh resolutions were tested, and the results were compared to those from NASA’s flow solvers, OVERFLOW and FUN3D, using the same turbulence and transition models, CFD meshes, and inflow conditiions.

## Simulation Conditions

- Test airfoil: NASA NLF(1)-0416 airfoil
- Flow Condition: M=0.1, Re=4million, Tu=0.15%, Angle of attack=5deg
- CFD meshes with six different resoltuions provided by [AIAA CFD Transition Modeeling DG](https://transitionmodeling.larc.nasa.gov/)
- Turbulence / Transition model: SST-2003 with 1-eq Gamma transition model, mut/mu=1
- Nalu-Wind version: [6155b17fa6b8914a819a492230c96f7990a97b78](https://github.com/Exawind/nalu-wind/commit/6155b17fa6b8914a819a492230c96f7990a97b78)

## Results
