# OBSERVATIONS

dia = float(input("dia of mould = "))
ht = float(input("height of mould = "))
wt_m = float(input("weight of mould = "))
pie = 22/7
vol = (pie/4)*ht*(dia**2)
print("%.2f"%vol)

# WET MOULD WITH SOIL

x = 0
wet_wt = []
for i in range(1,7):
  wet =float(input(f"enter {x+1} weight= "))
  print(wet)
  wet_wt.append(wet)
  x=x+1
print(wet_wt)
# WEIGHT OF WET COMPACTED SOIL

wet_cs = []
for i in wet_wt:
  cs_wt = i-wt_m
  wet_cs.append("%.3f"%cs_wt)

print(wet_cs)
# BULK DENSITIES

bulk_den=[]
for i in wet_cs:
  bulk = (float(i)/vol)*1000
  bulk_den.append("%.3f"%bulk)

print(bulk_den)
# WEIGHT OF CUP

y = 0
wt_cup = []
for i in range(1,7):
  cup_wt =float(input(f"enter {y+1} cup weight= "))
  print(cup_wt)
  wt_cup.append(cup_wt)
  y=y+1
print(wt_cup) 
# WEIGHT OF WET CUP

p = 0
wet_cup =[]
for i in range(1,7):
  cup_wet = float(input(f"enter {p+1} wet cup weight= "))
  print(cup_wet)
  wet_cup.append(cup_wet)
  p = p+1
print(wet_cup)
# WEIGHT OF CUP WITH DRY SOIL
q = 0
dry_cup =[]
for i in range(1,7):
  cup_dry = float(input(f"enter {q+1} dry weight of cup= "))
  print(cup_dry)
  dry_cup.append(cup_dry)
  q=q+1

print(dry_cup)
# WATER CONTENT

water = []
for i in range(0,6):
  wat = ((float(wet_cup[i])-float(dry_cup[i]))/(float(dry_cup[i])-float(wt_cup[i])))*100
  i=i+1
  water.append(float("%.3f"%wat))

print(water)
# DRY DENSITIES

dry_den=[]
for i in range(0,6):
  dry = float(bulk_den[i])/(1+(float(water[i])/100))
  i=i+1
  dry_den.append(float("%.3f"%dry))

print(dry_den)