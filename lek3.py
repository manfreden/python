print("Välkommen till mitt program där du kan addera")
operator = input("välj räaknesätt(+,-,*): ")
try:
    num1 = int(input("Mata in ett heltal: "))
except:
    print("Du måste skriva in en siffra")
    num1 = 0
try:
    num2 = int(input("Mata in ett till heltal: "))
except:
    print("Du måste skriva in en siffra")
    num2 = 0

if operator == "+":
    total = num1 + num2
elif operator == "-":
    total = num1 - num2
elif operator == "*":
    total = num1 * num2
elif operator == "/":
    total = num1 / num2
else:
    print("FEL")

print("total är:", total)