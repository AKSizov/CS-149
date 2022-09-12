# cookies.py
# hw 2.4

# Enter the number of cookies: 32
# Enter the number of family members: 5

# Each family member gets 6 cookies, and Rocky gets 2 cookies.

numCookies = int(input("Enter the number of cookies: "))
numFamily = int(input("Enter the number of family members: "))
print()
print("Each family member gets %s cookies, and Rocky gets %s cookies."
      % (numCookies // numFamily, numCookies % numFamily))
