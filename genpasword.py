import random
keys = ["1","2","3","4","5","6","7","8","9","1"]
a = int((input)("cuantos numeros nesecsita tu contraseña"))
contraseña = []
for i in range(a):
    contraseña.append(random.choice(keys))
contraseña += random.choice(keys)
print("a")
print("contraseña",contraseña)
