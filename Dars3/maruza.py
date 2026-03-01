# first_name = input("Ism kiriting: ")
# last_name = input("Familiya kiriting: ")
# middle_name = input("Sharif kiriting: ")
#
# # Maxsus belgilar: \n - enter, \t - tab,
# full_name = f"Salom\t, {first_name} {last_name}"
#
# print(full_name)
#


# Slicing
# O'zbekiston -> O'zb
# Monday - Mon

davlat = "O'zbekiston"
print(davlat[0:9:2])  # 0 -> start; 9 -> stop; 2 -> step (1)

day = "Monday"
print(day[0:3])

sweet = "Xo'rozqand"
print(sweet[6:])

animal = "Qo'ziqorinchalar"
print(animal[::-1])

print("Elbek"[::-1].title())

print(davlat[7] + davlat[9:])

