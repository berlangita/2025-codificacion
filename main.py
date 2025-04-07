asci = 31
while asci < 255:
    char = chr(asci)
    print(f"{asci} : {char}".ljust(10), end="")
    if (asci - 31) % 5 == 0:
        print()
    asci += 1
print("tabla asci")