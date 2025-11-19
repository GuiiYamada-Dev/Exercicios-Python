medida = float(input("Digite uma distancia em metros: "))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida  / 10
hm = medida / 100
km = medida / 1000
print(f"A media de {medida}m equivale a {dm:.0f}dm, {cm:.0f}cm e {mm:.0f}mm")
print(f"A media de {medida}m equivale a {dam:.0f}dam, {hm:.0f}hm e {km:.0f}km ")