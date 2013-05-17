# price.py listing, a Python script
import math

INITIAL_VALUE=1.9934545345

def reversable_iterations(iteration_number):
    test_floating = INITIAL_VALUE
    for i in range(iteration_number):
        test_floating = math.sqrt(test_floating)
    for i in range(iteration_number):
        test_floating = test_floating**2
    return 'with '+str(iteration_number)+' iterations, we get '+str(test_floating)

print 'The intial value is ',INITIAL_VALUE
print reversable_iterations(1)
print reversable_iterations(10)
print reversable_iterations(20)
print reversable_iterations(50)
print reversable_iterations(40)
print reversable_iterations(100)