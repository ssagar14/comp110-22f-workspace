"""An example of a while loop statement"""

counter: int = 0
maximum: int = int(input("Count up to, but not including what?"))

while counter < 10:
    counter_squared: int = counter ** 2
    print ("The square of the " + str(counter) + " is " + str(counter_squared))
    counter = counter + 1

print("Done!")