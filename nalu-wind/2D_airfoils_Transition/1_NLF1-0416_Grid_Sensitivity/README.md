

# Airfoil verification and validation 1: NASA NLF(1)-0416

A grid sensitivity study was performed for NASA NLF(1)-0416 airfoil using Nalu-Wind with the 1-eq gamma transition model.
Six different mesh resolutions were tested, and the results were compared to those from NASA’s flow solvers, OVERFLOW and FUN3D, using the same turbulence and transition models, CFD meshes, and inflow conditiions.

## Simulation Conditions

- Test airfoil: NASA NLF(1)-0416 airfoil
- Flow Condition: M=0.1, Re=4million, Tu=0.15%, Angle of attack=5deg
- CFD meshes with six different resoltuions provided by [AIAA CFD Transition Modeeling DG](https://transitionmodeling.larc.nasa.gov/)
-- Tiny, Coarse, Medium, Fine, Extra, Ultra
- Turbulence / Transition model: SST-2003 with 1-eq Gamma transition model with µt/µ=1
- Nalu-Wind version: [6155b17fa6b8914a819a492230c96f7990a97b78](https://github.com/Exawind/nalu-wind/commit/6155b17fa6b8914a819a492230c96f7990a97b78)

## Grid Sensitivity Study Results

### Lift coefficient at AoA=5deg: 
<img src="figs/aoa5/nlf0416_aoa5_cl.png" alt="Cf" width="400">

### Drag coefficient at AoA=5deg
<img src="figs/aoa5/nlf0416_aoa5_cd.png" alt="Cf" width="400">



## References
- OVERFLOW results: Venkatachari, B. S., Gosin, S. A., and Choudhari, M. M., “Implementation and Assessment of Menter’s Galilean-Invariant 𝛾
Transition Model in OVERFLOW,” AIAA AVIATION 2023 Forum, 2023. https://doi.org/10.2514/6.2023-3533
- FUN3D results: Hildebrand, N. J., Choudhari, M. M., and Venkatachari, B. S., “Implementation and Verification of the SST-𝛾 and SA-AFT
Transition Models in FUN3D,” AIAA AVIATION 2023 Forum, 2023. https://doi.org/10.2514/6.2023-3530.

