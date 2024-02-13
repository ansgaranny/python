#arithmetic operators
nambari=int(input("Enter the first number: "))
nambari2=int(input("Enter the second number: "))
nambari=67
nambari2=29
print(nambari+nambari2)
print(nambari-nambari2)
print(nambari*nambari2)
print(nambari/nambari2)
print(nambari%nambari2)
# comparison operators
nambari3=int(input("Enter the  first number: "))
nambari4=int(input("Enter the second number: "))
print(f"{nambari3}is equal to {nambari4} : {nambari3 == nambari4}")
print(f"{nambari3}is not equal to {nambari4} :  {nambari3 != nambari4}")
print(f"{nambari3}is greater than{nambari4} : {nambari3 > nambari4}")
print(f"{nambari3}is less than{nambari4} : {nambari3 < nambari4}")
print(f"{nambari3}is less than or equals to {nambari4} : {nambari3 <= nambari4}")

nambari5=int(input("Bonyeza Nambari: "))
nambari6=int(input("Bonyeza ya pili: "))

print(f"{nambari5} and {nambari6} both are true: {nambari5==nambari6 and nambari5>nambari6}")
print(f"{nambari5} and {nambari6} one is true: {nambari5==nambari6 or nambari5>nambari6}")