import string
from random import choice

# first names
first_names =['Bob', 'Rick', "Jon", "Tom", "Dick", "Harry"]

# last names
last_names = ["Johnson", "Andrews", "Harrington", "Smith", "Williams", "Bing" ]

# domain name
domain = ["gmail", "hotmail", "outlook", "icloud", "yahoo"]

# numbers
nums = string.digits

print(f"{'First Name':<10} {'Last Name':<10} {'Email':<30} Phone Number")
i = 0
while i < 10:
    first, last = f"{choice(first_names)}", f"{choice(last_names)}"
    email = f"{first.lower()}.{last.lower()}@{choice(domain)}.com"
    phone = f"{choice(nums)}{choice(nums)}{choice(nums)}-{choice(nums)}{choice(nums)}{choice(nums)}-{choice(nums)}" \
            f"{choice(nums)}{choice(nums)}{choice(nums)}"
    print(f"{first:<10} {last:<10} {email:<30} {phone}")
    i += 1

