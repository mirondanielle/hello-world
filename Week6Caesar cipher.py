plaintext = input("Enter a word or character: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plaintext:
             code += chr(ord(ch) + distance)
print("\n" + code)
               
