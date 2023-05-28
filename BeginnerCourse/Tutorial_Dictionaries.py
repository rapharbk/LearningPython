#Dictionarie

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# I can use numbers to determinate, as long they are unique 
numMonthConversions = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

#How to Use
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print("")

#using numbers
print(numMonthConversions[11])
print(numMonthConversions.get(12))
print("")

print(monthConversions.get("Luv", "Not a valid Key"))