# 120213_Demonstration.py
# In class exercises
# <Chad Hobbs>

# Formatting

# Fixed number of decimal places

# <width>.<# of decimals>f ( f = fixed)
# 11.3f
# 0.2f would be just to fix decimals. 0 = any number of
# precede with > to right justify, < left, or ^ center
# The command must be surrounded by {} and be followed by .format to execute

print("The balance is {0:0.2f}. You deposited {1:0.2}".format(2.123,2.123))

print("The balance is {1:0.2f}. You deposited {0:0.2}".format(2.123,2.123))

print("The balance is {0:<20.2f}. You deposited {1:^10.2}".format(2.123,2.123))
