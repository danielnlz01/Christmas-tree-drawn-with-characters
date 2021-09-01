# Pinito de navidad 
print("This program will draw a tree, tell me the height of the tree:")
niveles=int(input())
espacios=niveles-1 #número de espacios que van antes del primer asterisco
asteriscos=1 
contador=0 

while contador<niveles:
 contador+=1
 for x in range (espacios): #espacios antes de los asteriscos
  print(" ",end="") #cantidad de espacios
 for y in range (asteriscos): #cantidad de asteriscos
  print("* ",end="") #espacios o no después del asterisco
 print ("") #salto de línea
 asteriscos+=1 #variable que suma un asterisco para el próximo nivel
 espacios-=1 #variable que quita un asterisco para el próximo nivel"
 