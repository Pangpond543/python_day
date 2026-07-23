print('KPH\tMPH')
print('----------------')

for KPH in range (60, 140, 10):
    MPH = KPH * 0.6214
    print(KPH ,'\t', MPH)

print('-')
print('MPH\tKPH')
print('----------------')

for MPH in range (60, 140, 10):
    KPH = MPH / 0.6214
    print(MPH ,'\t', KPH)