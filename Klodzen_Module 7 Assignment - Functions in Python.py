#start#
#function#
def grThan(a, b):
    if a > b:
        return "The statement " + str(a) + " is greater than " + str(b) + " is true."
    else:
        return "The statement " + str(a) + " is greater than " + str(b) + " is false."

#body#
result=(grThan(10, 6))
print(result)
