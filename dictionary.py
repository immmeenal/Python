people = {"john": 32, "Minal": 19}
# dictionary comes  in key value pair. they are data structures which are used to map arbitory keys to values
print(people["john"])
print(people["Minal"])
#dictionary method (functions)
age = {11: "Minal", 23: "chhatre"}
print(age[23])
print(11 in age)
print(22 in age)

print(age.get(11,"Key not found"))
print(age.get(5,"Key not found"))
print(age.get(5))