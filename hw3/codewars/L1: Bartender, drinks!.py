# Write a function getDrinkByProfession/get_drink_by_profession() that receives as input parameter a string,
# and produces outputs according to the following table:
#
# Input	Output
# "Jabroni"	"Patron Tequila"
# "School Counselor"	"Anything with Alcohol"
#  "Programmer"	 "Hipster Craft Beer"
#  "Bike Gang Member"	"Moonshine"
#  "Politician"	"Your tax dollars"
#  "Rapper"	"Cristal"
#  *anything else*	"Beer"
# Note: anything else is the default case: if the input to the function is not any of the values in the table,
# then the return value should be "Beer."
#
# Make sure you cover the cases where certain words do not show up with correct capitalization.
# For example, getDrinkByProfession("pOLitiCIaN") should still return "Your tax dollars".


def get_drink_by_profession(param):
    param = param.title()
    print(param)
    if param == "Jabroni":
        return "Patron Tequila"
    elif param == "School Counselor":
        return "Anything with Alcohol"
    elif param == "Programmer":
        return "Hipster Craft Beer"
    elif param == "Bike Gang Member":
        return "Moonshine"
    elif param == "Politician":
        return "Your tax dollars"
    elif param == "Rapper":
        return "Cristal"
    else:
        return "Beer"

print(get_drink_by_profession("School Counselor"))
