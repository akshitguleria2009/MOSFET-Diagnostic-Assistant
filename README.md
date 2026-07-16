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
The limitations from the previous version were well thought upon and worked out using functions whixh reduced the code and made it moch more easier to understand 

- ### Lessons Learned (Prototype 2)
- We still need an error management system so as to prevent the program from crashing when the user does a mistake.
- The project needs a professional layout
