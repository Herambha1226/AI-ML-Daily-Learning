"""   
Tasks:

Generate 5 random numbers using np.random.rand()

Set seed using np.random.seed(42)

Generate again

Explain why both outputs are same
"""

import numpy as np

random_num = np.random.rand(5)
print("random_num : \n",random_num)
seed_num = np.random.seed(42)
print("seed_num : \n",seed_num)
print("random_num : \n",random_num)
