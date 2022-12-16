# Import all classes of PuLP module
from pulp import *

# Create the problem variable to contain the problem data
model = LpProblem("Music Company Profit Problem", LpMaximize)

# Create 3 variables tables, chairs, and bookcases
x1 = LpVariable("ModelM1", 0, None, LpInteger)
x2 = LpVariable("ModelM2", 0, None, LpInteger)
x3 = LpVariable("ModelM3", 0, None, LpInteger)

# Create maximize objective function
model += 20 * x1 + 10 * x2 + 15 * x3

# Create three constraints
model += 3 * x1 + 2 * x2 + 5 * x3 <= 55, "Manufacturing"
model += 2 * x1 + 1 * x2 + 1 * x3 <= 26, "Assembling"
model += 1 * x1 + 1 * x2 + 3 * x3 <= 30, "Packaging"
model += 5 * x1 + 2 * x2 + 4 * x3 <= 57, "Distributing"
model += x1 >= 0, "ModelM1"
model += x2 >= 0, "ModelM2"
model += x3 >= 0, "ModelM3"

# The problem is solved using PuLP's choice of Solver
model.solve()

# Each of the variables is printed with it's resolved optimum value
for v in model.variables():
    print(v.name, "=", v.varValue)
