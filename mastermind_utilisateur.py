import socket

new_socket = socket.socket()

my_host_name = socket.gethostname()

my_ip = socket.gethostbyname(my_host_name)

port = 8080

print(my_ip)

#new_socket.bind((my_host_name,port))

server_hote = "secret"

mon_nom = input("Entrez votre nom:")

new_socket.connect((server_hote,port))

new_socket.send(mon_nom.encode())

server_user_name = new_socket.recv(1000)

server_user_name = server_user_name.decode()

print(server_user_name,"c'est connecté")


import random

fin = False
solution = []
solutionsupprime = []
reponse = []
reponsesansdouble = []
reponsepasliste = 0
nombredetours = 0
essais = 0

joueur = new_socket.recv(1000)
joueur = joueur.decode()

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



if joueur == "2":
	print("combien de couleurs voulez vous? Indiquer avec des chiffres (0 est exclu des chiffres possibles).")
	possibilites = int(input())
	new_socket.send(str(possibilites).encode())
else :
	possibilites = new_socket.recv(1000)
	possibilites = str(possibilites.decode())


print("Il y a ",possibilites,"couleurs")

if joueur == "2":
	print("Combien de cases voulez vous?")
	cases = int(input())
	new_socket.send(cases.encode())
else :
	cases = new_socket.recv(1000)
	cases = str(possibilites.decode())

print("Il y a ",cases," cases.")

for i in range(cases):
	valeurtemporaire = random.randint(1,possibilites)
	solution.append(valeurtemporaire)

while not fin:
	reponse = []

	nombredetours += 1

	if joueur == "1":
		print("Choisissez un ensemble de valeurs que vous pensez être la solution, elles doivent être séparées d'un espace")
		for i in range(cases):
			print("Choisissez le",i+1,"nombre")
			valeurtemporaire = input()
			reponse.append(int(valeurtemporaire))
			new_socket.send(str(valeurtemporaire).encode())
	else : 
		valeurtemporaire = connection.recv(1000)
		valeurtemporaire = int(valeurtemporaire.decode())
		reponse.append(int(valeurtemporaire))


	print(reponse)

	checkage()
	essais += 1

print("Bravo vous avez trouver!! Et vous avez faits",essais,"essais.")
