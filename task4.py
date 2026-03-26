seconds = int(input("put value in second and ENTER: "))

hours = seconds // 3600
rest = seconds % 3600

minutes = rest // 60
seconds_remaining = rest % 60

print(f"{hours} horas, {minutes} minutes e {seconds_remaining} segundos")