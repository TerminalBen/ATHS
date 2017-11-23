
import random

total_Draws =0
attempts = 100000

for i in range (attempts):
    test_sum =0
    test_count =0
    while(test_sum<1):
        random_number = random.uniform(0,1)
        test_sum = random_number+test_sum
        test_count+=1
    total_Draws+=test_count

print (total_Draws/float(attempts))
