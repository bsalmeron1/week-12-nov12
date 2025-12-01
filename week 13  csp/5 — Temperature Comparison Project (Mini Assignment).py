# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.
temp=int(input("Whats the temperature today? :"))

if temp > 50 and temp <= 85 :
    print(" the weather is perfect")
elif temp <= 50 and -10 < temp:
        print("its very cold")
elif temp >= 86 and temp <= 109:
    print("Its very hot")
else:
 print("Extreme temp warning")
# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

