# monogram.py
# hw 3.1

# First name? Alfred
# Middle name? Edward
# Last name? Neuman

# The customer Alfred Edward Neuman has ordered a sweater with the monogram AEN.

firstName = input("First name? ")
middleName = input("Middle name? ")
lastName = input("Last name? ")

print("\nThe customer %s %s %s has ordered a sweater with the monogram %s%s%s."
      % (firstName, middleName, lastName,
         firstName[0], middleName[0], lastName[0]))
