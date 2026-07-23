# MOSFET-Diagnostic-Assistant
A Python project for diagnosing and repairing MOSFET parameters.

## Prototype 1 (12th July 2026)

This project diagnoses basic MOSFET parameters and automatically repairs values that are outside acceptable limits. This simple python based program serves as more of a stepping stone in the bigger journey of making machine learning powered diagnostic tool.

Current checks:
- VGS
- VDS
- Temperature
- Channel Length
- Channel Width

Language:
- Python

- ### Lessons Learned (Prototype 1)
I realized that storing values from a dictionary into separate variables felt repetitive.
I also noticed that writing many if-else statements makes the code harder to maintain.
These limitations motivated me to explore functions, loops over dictionaries, and better program design in future prototypes.

Prototype 2 (16th July 2026)
The limitations from the previous version were well thought upon and worked out using functions which reduced the code and made it much more easier to understand.

- ### Lessons Learned (Prototype 2)
- We still need an error management system so as to prevent the program from crashing when the user does a mistake.
- The project needs a professional layout.

### Transition to Visualization (21st July 2026)
Completed the NumPy phase of the project.
The physics engine can now perform vectorized MOSFET calculations efficiently.
During implementation planning, I realized numerical computation alone isn't enough—engineering tools need clear visualization.
The next milestone is integrating Matplotlib to generate transfer/output characteristic curves (ID–VGS, ID–VDS), allowing users to interpret device behaviour rather than raw numerical outputs.
This shifts the project from being a calculation script toward becoming an actual analysis tool.
The plan for prototype 3 is to move into an actual engneering tool rather than just a simple python based program based on independent inputs which do not effect each other which is not the case for an actual MOSFET.

### Prototype 3 (23rd July, 2026)
With the help of basic matplotlib I was able to plot the drain current and VGS graph further strengthening the project.
Shifting the focus from a python fundamental heavy endeavour to an actual MOSFET physics based engine, which not only takes the values from the user but also establishes the dependence of different factors on one another, for commit 4 we will look to delve more into the physics by sweeping VDS instead of VGS and son and so forth.
Additionally plotting more curves aswell, which will involve more knowledge of MATPLOTLIB essential for actual visualisation of the physics backed python code.

### Lessons learned (Prototype 3)
Some technical lessons like a unicode is not a minus sign as python is a object oriented case sensitive language an eye opener not to forget the basics.
Learnt about the basis of MOSFET based physics.
The next prototype would look better with more graphs to show output characteristics better
