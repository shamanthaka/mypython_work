temps = [("Berlin", 29), ("Cairo", 36), ("Bueno Airs", 19), ("Los Angeles", 26),
         ("Tokyo", 27), ("New York", 28), ("London", 22), ("Delhi",34)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

temp_in_f = list(map(c_to_f, temps))

print(temp_in_f)