# Get input from user
sisi1 = input("Masukkan sisi 1: ")
sisi2 = input("Masukkan sisi 2: ")
sisi3 = input("Masukkan sisi 3: ")

# Try to convert inputs to integers
try:
    sisi1 = int(sisi1)
    sisi2 = int(sisi2)
    sisi3 = int(sisi3)
except ValueError:
    print("Error: Input harus berupa bilangan bulat!")
    exit()

# Check if all sides are equal
if sisi1 == sisi2 == sisi3:
    print("3 sisi sama")
# Check if two sides are equal
elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
    print("2 sisi sama")
# If none of the above conditions are true, print "Tidak ada yang sama"
else:
    print("Tidak ada yang sama")