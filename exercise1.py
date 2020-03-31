# Exercise 1, Print, Variable and Datatype
import math

# TASK 1: Print out a place you want to go most.
print("Definitely Bankok!!!!!")

# TASK 2: Calculate area of rectangle, Print it out.
width = 100
height = 20

print(width * height)

## TASK 3: Calculate Area for a circle
radius = 7

print(math.pi * radius * radius)

# Or....
print(math.pi * math.pow(radius, 2))

# TASK 3: Challenging one, and memorable one for us. And here is the description
# for this question

# There're tons of Chinese rap singers rising because of the Chinese TV-show "The Rap Of China".
# Hence they call 2017 "The Hip-Hop Year".
# Lots of fans imitate these remarkable rappers like PG One and GAI.
"""
PG One always wears 3 gold chains with 4 silver rings.

GAI always wears 2 gold chains with 3 silver rings.
"""
# Please calculate the fans number supporting each singer (PG One and GAI) by 
# the above information and the formatted input like the following example.

gold_chain = 625
silver_rings = 875
pg_one_fans = -1        # U need to calculate it.
gai_fans = -1           # need to calculate it too.

# Your code here...
# 3x + 2y = 625
# 4x + 3y = 875
gai_fans = 3 * silver_rings - 4 * gold_chain
pg_one_fans = 3 * gold_chain - 2 * silver_rings

print(f"Pg One have {pg_one_fans} fans.")
print(f"GAI have {gai_fans} fans.")

# Original Problem: https://acm.cs.nthu.edu.tw/problem/11542/