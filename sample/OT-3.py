# import the library pulp as p
import pulp as p
  
# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMaximize) 
  
# Create problem Variables 
x = p.LpVariable("M1", lowBound = 50)   # Create a variable x >= 0
y = p.LpVariable("M2", lowBound = 150)   # Create a variable y >= 0
z = p.LpVariable("M3", lowBound = 100)   # Create a variable z >= 0

# Objective Function
Lp_prob += 200 * x + 450 * y + 650 * z
  
# Constraints:
Lp_prob += 4 * x + 3 * y + 6 * z <= 130, "Manufacturing"
Lp_prob += 3 * x + 4 * y + 9 * z <= 180, "Assembling"
Lp_prob += 2 * x + 2 * y + 5 * z <= 55, "Packaging"
  
# Display the problem
print(Lp_prob)
  
status = Lp_prob.solve()   # Solver
print(p.LpStatus[status])   # The solution status
  
# Printing the final solution
print("M1 = ",p.value(x))
print("M2 = ", p.value(y))
print("M3 = ", p.value(z))
print("Optimal value = ", p.value(Lp_prob.objective)) 