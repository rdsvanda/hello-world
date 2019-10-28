fat_number = input('What is your weight?')
lb_or_kg = input('Was that (L)bs or (K)g?')
weight = int(fat_number)

if lb_or_kg.upper == 'L':
    print(weight / 2.205)

elif lb_or_kg.upper() == 'K':
    print(weight * 2.205)

else:
    print('Please enter L or K.')