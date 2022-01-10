from solution import calculate_number_of_queen_arrangement as f

import matplotlib.pyplot as plt

# Plot
plt.plot([f(n) for n in range(12)])
plt.xlabel('N')
plt.ylabel('number of queens arrangement')
plt.show()
