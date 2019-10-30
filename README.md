# Python_Numerics

Mostly elementary CFD codes in Python and some numerical linear algebra 

list of equations thus far:
  - 2-D advection_diffusion equation using explicit finite difference scheme (from Dr. Barba 12 steps)
      1. vectorized 1 for loop_ integrating time
      2. not vectorized 3 for loops time and spatial
    Future plan: generalize the solver for enable only heat equation, or convection equation with various boundary condition
    
    
  - 2-D Laplace equation
      1. Using Gauss-Seidal/Liebmann method
      2. Jacobi iterative method
     Future plan: make it general for it to be able solve with source term and various boundary conditions.
     
Referenced books & courses:
  -CFD python: 12 steps to Navier Stokes, Barbar
  -Numerical Methods for Engineers, Chapra & Canale
  -Fundamentals of Computational Fluid Dynamics, Lomax&Pulliam& Zingg
  -Computational Fluid Dynamics Hoffmann & Chiang
  -Numerical Fluid Mechanics, MIT opencourseware 
  -NASA Advanced Modeling & Simulation (AMS) Seminar Series, Introduction to Computational Fluid Dynamics
     
