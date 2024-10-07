

# NASA NLF(1)-0416

Validation and verification of the transition model were conducted for the NASA NLF(1)-0416 airfoil using Nalu-Wind with the 1-equation gamma transition model. First, a grid sensitivity study was performed using six different mesh resolutions from the AIAA CFD Transition Modeling DG[^1]. The results were compared to those from NASA’s structured flow solver, OVERFLOW[^2], and unstructured flow solver, FUN3D[^3], utilizing the same turbulence and transition models, CFD meshes, and inflow conditions. Based on these findings, a full angle-of-attack sweep was performed, with results compared to experimental data.

## Simulation Conditions

- Test airfoil: NASA NLF(1)-0416 airfoil
- Flow Condition: M=0.1, Re=4million, Tu=0.15%
- CFD meshes with six different resoltuions provided by [AIAA CFD Transition Modeling DG](https://transitionmodeling.larc.nasa.gov/) 
  - 2-D strcutred C-type meshes: Tiny, Coarse, Medium, Fine, Extra, Ultra resolutions[^4]
- Turbulence / Transition model: SST-2003 with the 1-eq Gamma transition model with µt/µ=1
- Nalu-Wind version: [6155b17fa6b8914a819a492230c96f7990a97b78](https://github.com/Exawind/nalu-wind/commit/6155b17fa6b8914a819a492230c96f7990a97b78)

## Results: Grid Sensitivity Study

### Lift coefficient at AoA=5deg: 
<img src="figs/aoa5/nlf0416_aoa5_cl.png" alt="Cf" width="400">

### Drag coefficient at AoA=5deg
<img src="figs/aoa5/nlf0416_aoa5_cd.png" alt="Cf" width="400">

Two different options for the freestream conditions are tested here: 
1) Local turbulence intensity with the sustaining terms (green line): same way as the OVERFLOW and FUN3D simulations
2) Constant turbulence intensity without the sustaining terms (red line)

The grid sensitivitiy results are presented for the lift and drag coefficient. In the above figure, the x axis, h, is the 1/sqrt(total number of nodes), meaning smaller values correspond to finer grids. With the Option 1, Nalu-Wind results show similar trends to the FUN3D results. It is also seen that to achieve  the grid-converged trends, at least the third finest mesh resolution, ("Fine") is required. Overall, both Nalu-Wind and FUN3D show more mesh-dependence than OVERFLOW. This is attributed to the numerical shcemes of the unstructred flow solvers, which have lower aptial accuracy compared to structured flow solvers.

Option 2, which applies a constant turbulence intensity, improves grid convergence, particularly at lower mesh resolutions. For more consistent and accurate results with Nalu-Wind, Option 2 is recommended. However, it should be noted that Option 2 is valid only for single airfoil or single turbine simulations. For internal flow or multi-turbine cases, Option 1 should be used. Option 2 is activated only if fsti is explicitly specified in the Nalu-Wind input with a positive value.

## Results: Angle of Attack Sweep

### Comparison of the lift coefficient
<img src="figs/clcd/nlf0416_al_cl.png" alt="Cf" width="400">

### Comparison of the drag polar 
<img src="figs/clcd/nlf0416_cd_cl.png" alt="Cf" width="400">

Based on the grid sensitivity results, a full sweep of angles of attack was performed using the Fine mesh level. The two figures above compare the lift and drag polar with the experimental measurements[^5]. For the lift, the transition simulation slightly over-predicts the lift coefficient in the linear range of the lift curve, a similar behavior also observed in transition predictions using other transition models. For the drag polar, the transition simulation predicts lower drag across the range of angles of attack than the fully turbulent simulation, capturing the trend of the experimental data very well.

Each case was run on 26 cores of NREL's Kestrel HPC system and took approximately 40 minutes to 10,000 iterations, using 4 Picard iterations per time step.
Note that the number of cores per case is not based on the scalability of Nalu-Wind but rather to fit 4 cases onto a single node of Kestrel.

## References
[^1]: https://transitionmodeling.larc.nasa.gov/
[^2]: Venkatachari, B. S., et al., "Implementation and Assessment of Menter’s Galilean-Invariant 𝛾
Transition Model in OVERFLOW," AIAA AVIATION 2023 Forum, 2023. https://doi.org/10.2514/6.2023-3533
[^3]: Hildebrand, N., et al., "Implementation and Verification of the SST-𝛾 and SA-AFT
Transition Models in FUN3D," AIAA AVIATION 2023 Forum, 2023. https://doi.org/10.2514/6.2023-3530.
[^4]: Coder, J., "Standard Test Cases for Transition Model Verification and Validationin Computational Fluid Dynamics," 56th AIAA Aerospace Sciences Meeting, January, 2018. https://doi.org/https://doi.org/10.2514/6.2018-0029.
[^5]: Somers, D. M., "Design and Experimental Results for a Natural-Laminar-Flow Airfoil for General Aviation Applications," NASA Technical Paper 1861, 1981.
