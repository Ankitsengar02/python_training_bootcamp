# Decimal to binary conversion
dec = int(input("Enter the decimal number: "))
binary = ""

while dec != 0:
    remainder = dec % 2
    binary = str(remainder) + binary  
    dec = dec // 2     #floor division //
print(binary)

#Decimal to Octal conversion
decimal_number = int(input("Enter a decimal number: "))
octal_num = ""
while decimal_number > 0:
        remainder = decimal_number % 8
        octal_num = str(remainder) + octal_num
        decimal_number //= 8

print("The octal representation is:", octal_num)

#Decimal to HexaDecimal conversion
decimal_number = int(input("Enter a decimal number: "))
HexaDecimal_num = ""
while decimal_number > 0:
        remainder = decimal_number % 16
        HexaDecimal_num = str(remainder) + HexaDecimal_num
        decimal_number //= 16  

print("The HexaDecimal representation is:", HexaDecimal_num)
