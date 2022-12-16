# import the library pulp as p
import pulp as p
  
# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMaximize) 
  
# Create problem Variables 
x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0
y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0
z = p.LpVariable("z", lowBound = 0)   # Create a variable z >= 0

# Objective Function
Lp_prob += 3 * x + 2 * y + 5 * z
  
# Constraints:
Lp_prob += 1 * x + 2 * y + 1 * z <= 430
Lp_prob += 3 * x + 2 * z <= 460
Lp_prob += 1 * x + 4 * y <= 420
  
# Display the problem
print(Lp_prob)
  
status = Lp_prob.solve()   # Solver
print(p.LpStatus[status])   # The solution status
  
# Printing the final solution
print("x = ",p.value(x))
print("y = ", p.value(y))
print("z = ", p.value(z))
print("Optimal value = ", p.value(Lp_prob.objective)) 