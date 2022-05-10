import random
man = ['John','Maynard','Patrick','Wentworth','Pablo','Lewis','Noble','David','Henry','Alfred','Wayne','Zadok','Lucas','Peter','Matthew','Hilton','Robin','László','Ben','James','Nicolas','Robert','Amir','Charles','Joseph']
woman =['Susan', 'Mary','Josephine','Cynthia','Caroline','Gerthrude','Lilith', 'Diana', 'Sophie','Anne','Loulou','Bernadette', 'Maria','Nora','Rose','Loise','Margarett','Laura','Roxanne','Sandra','Dorothy']
nazwiska = ['Johnson','Rascal','Armitage','McCartney','Ramirez','Oakwood','Armsbridge','Mordeaux','Daniels','Castro','Banks','Mahoney', 'Norwood', 'Sandro', 'Quagmire', 'Goldhill', 'Southman', 'McQueen', 'Lockhart','Palmer','Harper','Monk', 'Patterson','Lockley','Spencer','Ball','Cassetti','Whiteman','Blackman','Johansson','Novak','Kowalsky','Sultan','MacDonald']
plec = (man, woman)
p = random.choice(plec)
if p == man:
  x=man
  print('plec: mezczyzna')
if p == woman:
  x=woman
  print('plec: kobieta')
x = random.choice(p)
man.pop:(x)
woman.pop:(x)
y = random.choice(nazwiska)
nazwiska.pop:(y)
print(x, y)
zawod = ['ksiegowy','akrobata','gwiazda kina', 'robotnik','sportowiec','bogaty hobbysta','profesor','detektyw z agencji','strażak','bibliotekarz','psycholog','pilot','archeolog','hobo','żołnierz','sprzedawca','księgarz','psychiatra']
z = random.choice(zawod)
zawod.pop:(z)
print('zawod: ', z)
w = random.randint(15,99)
wiek = w
wiek.pop:(w)
print('wiek: ', w)
kostka = (1,2,3,4,5,6)
r1 = random.choice(kostka)
r2 = random.choice(kostka)
r3 = random.choice(kostka)
sila = ((r1+r2+r3)*5)
print('sil: ', sila)
r1 = random.choice(kostka)
r2 = random.choice(kostka)
r3 = random.choice(kostka)
kondycja = ((r1+r2+r3)*5)
print('kon: ', kondycja)
r1 = random.choice(kostka)
r2 = random.choice(kostka)
bc = ((r1+r2+6)*5)
print('bdc: ', bc)
r1 = random.choice(kostka)
r2 = random.choice(kostka)
r3 = random.choice(kostka)
zrecznosc = ((r1+r2+r3)*5)
print('zre: ', zrecznosc)
r1 = random.choice(kostka)
r2 = random.choice(kostka)
r3 = random.choice(kostka)
wyg = ((r1+r2+r3)*5)
print('wyg: ', wyg)
r1 = random.choice(kostka)
r2 = random.choice(kostka)
int = ((r1+r2+6)*5)
print('int: ', int)
r1 = random.choice(kostka)
r2 = random.choice(kostka)
r3 = random.choice(kostka)
pow = ((r1+r2+r3)*5)
print('moc: ', pow)
r1 = random.choice(kostka)
r2 = random.choice(kostka)
edu = ((r1+r2+6)*5)
r1 = random.choice(kostka)
r2 = random.choice(kostka)
r3 = random.choice(kostka)
luck = ((r1+r2+r3)*5)
rzut = random.randint(1,100)
roll1 = rzut
roll1.pop:(rzut)
rozwoj = random.randint(1,10)
roll2 = rozwoj
roll2.pop:(rozwoj)
maxedu = (1,99)
if w < 19:
  print('wyk: ', edu)
if w == 19:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 20:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 21:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 22:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 23:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 24:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 25:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 26:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 27:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 28:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 29:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 30:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 31:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 32:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 33:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 34:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 35:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 36:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 37:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 38:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 39:
   if rzut > edu:
     print('wyk: ', rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 40:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 41:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)  
if w == 42:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)  
if w == 43:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)  
if w == 44:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)  
if w == 45:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)  
if w == 46:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)  
if w == 47:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)  
if w == 48:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)  
if w == 49:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 50:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 51:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 52:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 53:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 54:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 55:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 56:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 57:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 58:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 59:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 60:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 61:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 62:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 63:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 64:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 65:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 66:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 67:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 68:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 69:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu) 
if w == 70:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 71:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 72:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 73:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 74:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 75:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 76:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 77:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 78:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 79:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 80:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 81:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 82:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 83:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 84:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 85:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 86:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 87:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 88:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 89:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 90:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 91:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 92:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 93:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 94:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 95:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 96:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 97:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 98:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w == 99:
   if rzut > edu:
     print('wyk: ', rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+rozwoj+edu)
   elif rzut <= edu:
     print('wyk: ', edu)
if w >= 19:
  print('szczescie: ', luck)
elif w < 19:
  if rzut > luck:
    print('szczescie: ', rozwoj+luck)
  elif rzut < luck:
    print('szczescie: ', luck)      
speed1 = (7)
speed2 = (8)
speed3 = (9)
speed4 = (6)
speed5 = (5)
speed6 = (4)
speed7 = (3)
speed8 = (2)
speed9 = (1)
if w == 15:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 16:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 17:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 18:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 19:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 20:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 21:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 22:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 23:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 24:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 25:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 26:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 27:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 28:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 29:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 30:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',peed3)
if w == 31:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 32:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)
if w == 33:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3) 
if w == 34:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)    
if w == 35:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)   
if w == 36:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)    
if w == 37:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3) 
if w == 38:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)    
if w == 39:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed1)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed2)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed3)    
if w == 40:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed4)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed1)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed2)
if w == 41:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed4)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed1)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed2)
if w == 42:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed4)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed1)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed2)  
if w == 43:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed4)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed1)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed2)   
if w == 44:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed4)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed1)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed2)
if w == 45:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed4)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed1)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed2)  
if w == 46:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed4)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed1)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed2)   
if w == 47:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed4)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed1)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed2)   
if w == 48:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed4)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed1)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed2)  
if w == 49:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed4)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed1)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed2) 
if w == 50:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed5)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed4)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed1) 
if w == 51:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed5)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed4)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed1) 
if w == 52:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed5)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed4)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed1)    
if w == 53:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed5)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed4)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed1)  
if w == 54:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed5)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed4)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed1)
if w == 55:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed5)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed4)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed1)
if w == 56:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed5)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed4)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed1)  
if w == 57:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed5)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed4)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed1) 
if w == 58:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed5)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed4)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed1) 
if w == 59:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed5)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed4)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed1)   
if w == 60:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed6)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed5)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed4)   
if w == 61:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed6)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed5)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed4)  
if w == 62:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed6)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed5)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed4)
if w == 63:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed6)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed5)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed4)  
if w == 64:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed6)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed5)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed4)      
if w == 65:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed6)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed5)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed4)  
if w == 66:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed6)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed5)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed4)  
if w == 67:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed6)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed5)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed4)   
if w == 68:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed6)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed5)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed4)  
if w == 69:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed6)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed5)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed4)      
if w == 70:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed7)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed5)   
if w == 71:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed7)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed5)
if w == 72:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed7)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed5)
if w == 73:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed7)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed5)   
if w == 74:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed7)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed5)
if w == 75:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed7)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed5)
if w == 76:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed7)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed5)
if w == 77:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed7)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed5)
if w == 78:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed7)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed5)
if w == 79:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed7)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed5)
if w == 80:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed8)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed7)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed6)
if w == 81:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed8)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed7)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed6)
if w == 82:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed8)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed7)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed6)
if w == 83:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed8)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed7)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed6)
if w == 84:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed8)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed7)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed6)
if w == 85:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed8)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed7)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed6)
if w == 86:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed8)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed7)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed6)
if w == 87:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed8)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed7)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed6)   
if w == 88:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed8)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed7)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed6)
if w == 89:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed8)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed7)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed6)
if w == 90:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed9)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed7)
if w == 91:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed9)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed7)
if w == 92:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed9)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed7)
if w == 93:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed9)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed7)
if w == 94:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed9)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed7)
if w == 95:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed9)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed7)
if w == 96:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed9)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed7)
if w == 97:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed9)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed7)
if w == 98:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed9)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed7)
if w == 99:
  if sila and zrecznosc < bc:
    print('szybkosc: ',speed9)
  elif sila or zrecznosc == bc:
    print('szybkosc: ',speed6)
  elif sila and zrecznosc > bc:
    print('szybkosc: ',speed7)        
sanity = pow
print('poczytalnosc: ', sanity)