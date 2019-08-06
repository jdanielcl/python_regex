import re
import random

chain = "We'll learn regex in Python in the easiest way. Python is amazing!"

# look for a coincidente in a string
coincidence = re.search("Python",chain)
print(coincidence)
print(coincidence.start())
print(coincidence.end())
print(coincidence.span())
print(re.search("leart",chain))

# look for multiple coincidences
m_coincidence = re.findall("Python",chain)
print(m_coincidence)

name_list = [
    'Daniel Felipe',
    'Ana Maria',
    'Andrea Ana',
    'Camilo Andrés',
    'Xiomara hupespedes',
    'Estefanía Cepeda',
    'Yeisson Fernandez',
    'Marcela Pérez'
]

print("--- all coincidences with ----")

for e in name_list:
    if re.search("An",e):
        print(e)


print("--- start with ----")
for e in name_list:
    if re.search("^An",e):
        print(e)

print("--- Finish with a ----")
for e in name_list:
    if re.search("a$",e):
        print(e)

print("--- Coincidence 'n' surrounded by vowels----")
for e in name_list:
    if re.search("[aeiou]n[aeiou]",e.lower()):
        print(e)

print("--- Coincidence by range last letter ----")
for e in name_list:
    if re.search("[a-l]$",e.lower()):
        print(e)

print("--- Coincidence by two ranges range fist letter ----")
for e in name_list:
    if re.search("^[a-lx-z]",e.lower()):
        print(e)

print("--- Coincidence by range with numbers ----")
# with numbers range
number_list = [random.randint(5000,9999) for _ in range(100)]
result = []
for e in number_list:
    if re.search("[3-6]$",str(e)):
        result.append(e)

print("--- Coincidence by negated rage ----")
# with numbers
result = []
for e in number_list:
    if re.search("[^1-9]$",str(e)):
        result.append(e)

print(result)

print("---- Wildcard in the first letter ----")
print("---- Second letter consonant ----")
for e in name_list:
    if re.search("^.[^aeiou]",e.lower()):
        print(e)