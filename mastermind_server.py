import socket

# ip freebox publique : 82.253.127.251

new_socket = socket.socket()
my_host_name = socket.gethostname()
my_ip = socket.gethostbyname(my_host_name)
port = 8080

print(my_ip)

new_socket.bind((my_host_name,port))

mon_nom = input("Votre nom:")

new_socket.listen(1)

connection,add = new_socket.accept()


utilisateur = (connection.recv(1000).decode())
print(utilisateur,"c'est connecté")
connection.send(mon_nom.encode())


import random

joueur = str(input("""Quel joueur choisis le mot a trouver? "1" ou "2" ? : """))

connection.send(joueur.encode())

fin = False
solution = []
solutionsupprime = []
reponse = []
reponsesansdouble = []
reponsepasliste = 0
nombredetours = 0
essais = 0

def checkage():
	nombrebons = 0
	nombresressembles = 0
	global fin
	global cases
	global reponse
	global solution
	solutionsupprime = []

	for x in range(len(solution)):
		solutionsupprime.append(solution[x])
	#print(solutionsupprime)

	for i in range(cases):
		if reponse[i] == solution[i]:
			nombrebons += 1
			solutionsupprime[i] = "pris"

	for i in range(cases):
		for x in range(len(reponse)):
			if solutionsupprime[i] == reponse[x]:
				nombresressembles+=1
				solutionsupprime[i] = "pris"

	if nombrebons == cases:
		fin = True
	print("Vous avez",nombrebons,"chiffres à la bonne place")
	#print(nombresressembles,nombrebons)
	print("Vous avez",nombresressembles,"chiffres de meme valeurs (sans compter ceux qui sont correctements placés).")





print("Bienvenu dans ce jeu de master mind")

if joueur == "1":
	print("combien de couleurs voulez vous? Indiquer avec des chiffres (0 est exclu des chiffres possibles).")
	possibilites = int(input())
	connection.send(str(possibilites).encode())
else :
	possibilites = connection.recv(1000)
	possibilites = str(possibilites.decode())


print("Il y a ",possibilites,"couleurs")

if joueur == "1":
	print("Combien de cases voulez vous?")
	cases = int(input())
	connection.send(str(cases).encode())
else :
	cases = connection.recv(1000)
	cases = str(possibilites.decode())

print("Il y a ",cases," cases.")

for i in range(cases):
	valeurtemporaire = random.randint(1,possibilites)
	solution.append(valeurtemporaire)

while not fin:
	reponse = []

	nombredetours += 1

	if joueur == "2":
		print("Choisissez un ensemble de valeurs que vous pensez être la solution, elles doivent être séparées d'un espace")
		for i in range(cases):
			print("Choisissez le",i+1,"nombre")
			valeurtemporaire = input()
			reponse.append(int(valeurtemporaire))
			connection.send(str(valeurtemporaire).encode())
	else : 
		valeurtemporaire = connection.recv(1000)
		valeurtemporaire = int(valeurtemporaire.decode())
		reponse.append(int(valeurtemporaire))


	print(reponse)

	checkage()
	essais += 1

print("Bravo vous avez trouver!! Et vous avez faits",essais,"essais.")
