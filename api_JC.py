# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 08:57:51 2018

@author: OCAKTAN
"""

#Librairies
import requests
import json
from time import sleep
import webbrowser

#----------------------------Requete API----------------------------#

#A la place de l input utilisateur (Il faut que la premiere lettre soit une majuscule, on forcera ca plus tard)
nom_ville='Valence'

#Faire la demande de l API
response = requests.get("http://api.jcdecaux.com/vls/v1/stations?contract="+nom_ville+"&apiKey=d80a09d7eb939b23cabc2e4645c4c7fc7741d5e7")
#La reponse de la requete
python_obj = json.loads(response.text)

#Parcourir les noms de villes presentes dans la reponse de la requete pour verifier que l input utilisateur correspond a une ville presente dans cette reponse
for i in range(len(python_obj)-1):
    if python_obj[i]['contract_name']==nom_ville:
        print('Jai trouve la ville')
        break
    else
        print('Je ne trouve pas '+nom_ville)

#La position de l utilisateur    
ma_position=[45.900880,6.124524]

#----------------------------Calcul de la distance----------------------------#

#Initialiser la position le plus proche a la premiere position de la liste des stations
position=[python_obj[0]['position']['lat'],python_obj[0]['position']['lng']]
#Calcul de distance en moyennant la longitude et la latitude
distance=(abs(ma_position[0]-position[0])+abs(ma_position[1]-position[1]))/2

#Parcourir la liste des longitude et latitude pour calculer la distance la plus proche de celle fournie par l utilisateur
for i in range(1,len(python_obj)-1):
    #Recuperer chacune des positions fournies par la reponse de la requete
    all_lat=python_obj[i]['position']['lat']
    all_lon=python_obj[i]['position']['lng']
    new_position=[python_obj[i]['position']['lat'],python_obj[i]['position']['lng']]
    #Calculer la distance par rapport a ma position
    new_distance=(abs(ma_position[0]-new_position[0])+abs(ma_position[1]-new_position[1]))/2
    #A la fin de la boucle on obtient la distance la plus petite par rapport a celle fournie par l'utilisateur
    if new_distance<=distance:
        position=new_position
        distance=new_distance

#----------------------------Affichage des resultats----------------------------#
print(position)
#webbrowser.open('https://maps.google.com/?q='+repr(position[0])+','+repr(position[1]))
#Ouvrir un browser qui affiche l itineraire de ma position a cet endroit
webbrowser.open('https://www.google.com/maps/dir/'+repr(ma_position[0])+','+repr(ma_position[1])+'/'+repr(position[0])+','+repr(position[1]))
    
    




