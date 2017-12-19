####################################################################
#                                                                  #
#       Python 3.5.2                                               #
#                                                                  #
#       Ce programme permet de jouer des notes avec le 3dRudder    #
#       et faire traviller sa mémoire                              #
#                                                                  #
####################################################################



##########################################################
#Importation des librairies
##########################################################
import sys
import time
import platform
import random
import sqlite3
import os





##########################################################
#Joue les notes de musique
##########################################################
def music () :
        print ("------------------------------------")
        tempo=int(input("Entrer le nb de battements par minutes : "))
        print ("------------------------------------")
        print ("Faire Ctrl + C pour arréter")
        while True :

                sdk.GetAxis(0,NormalizedValue,axis)
                
                if axis.m_aX>0.5:
                        sdk.PlaySndEx(0,"f5(100,0)")
                        print ("Fa")
                elif axis.m_aX<-0.5:
                        sdk.PlaySndEx(0,"e5(100,0)")
                        print("Mi")
                
                        
                elif axis.m_aY>0.5:
                        print ("Re")
                        sdk.PlaySndEx(0,"d5(100,0)")
                elif axis.m_aY<-0.5:
                        print("Do")
                        sdk.PlaySndEx(0,"c5(100,0)")
                
                        
                elif axis.m_aZ>0.5:
                        sdk.PlaySndEx(0,"c6(100,0)")
                        print ("Do")
                elif axis.m_aZ<-0.5:
                        sdk.PlaySndEx(0,"b5(100,0)")
                        print("Si")
                
                        
                elif axis.m_rZ>0.5:
                        sdk.PlaySndEx(0,"g5(100,0)")
                        print ("Sol")
                elif axis.m_rZ<-0.5:
                        sdk.PlaySndEx(0,"a5(100,0)")
                        print("La")
                
                        
                print ()
                        
                time.sleep (60/tempo)
        
##########################################################
#Demarrage du programme
##########################################################      
def debut ():   
        print ()
        print ("-------3dMusic-------")
        print ()
        print("Découvrir les positions des notes : 1")
        print("Jouer de la musique : 2")
        print ("Jeu de memoire : 3")
        print ("Scores au jeu : 4")
        print ()
        


##########################################################
#Presentation des positions des notes
##########################################################      
def note():
        print ()
        print ("Arriere: Do             Avant  :Re")
        print ("Gauche : Mi             Droite :Fa ")
        print ("Rdroite: Sol            Rgauche:La")
        print ("Bas    : Si             Haut   :Do")
        print ()
        b=int(input("Retourner au menu ? (0/1) : "))
        if b==1:
                debut()
        elif b==0:
                note()
        else :
                print("Le choix n'est pas reconnu")
                note()
##########################################################

        
##########################################################
#Jeu de mémoire
##########################################################      
def jeu():

        ####################################
        #Base de donnée pour les scores
        ####################################
        db=sqlite3.connect('score.db')
        
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS 
        users(id INTEGER PRIMARY KEY, name TEXT,level INTEGER,score INTERGER)""")
        db.commit()

        #######################################
        
        print ()
        print ("--------------------")
        print ()
        print("La partie se deroule en 5 manche ")
        print ("ou vous allez devoir reconnaitre la note jouee" )
        print ("et ensuite la reproduire sur le 3dRudder")
        print ()
        print ("--------------------")
        try:
                d=int(input("Entrez la difficulte de 1 (difficile) a 5 (facile) : "))
        except ValueError as e :
                print ("La valeur entrée n'est pas correcte")
                d=5
        if 1<=d<=5:
                s=0
                for j in range (0,5):
                        try :
                                #Phase d'écoute
                                print ("Ecoutez !")
                                notes = ["c5(500,0)","d5(500,0)","e5(500,0)","f5(500,0)","g5(500,0)","a5(500,0)","b5(500,0)","c6(500,0)",]
                                nom =["Do","Re","Mi","Fa","Sol","La","Si","Do"]
                                r=random.randint (0,7)
                                sdk.PlaySndEx(0,notes[r])
                                time.sleep(1)
                                print ("Vous avez ",d,"sec pour vous positionner")
                                time.sleep (d)
                                print ("--------------------")
                                #Phase de jeu
                                print("Refaites !")
                                sdk.GetAxis(0,NormalizedValue,axis)
                                        
                                if axis.m_aX>0.5:
                                        sdk.PlaySndEx(0,"f5(250,0)")
                                        n="Fa"
                                elif axis.m_aX<-0.5:
                                        sdk.PlaySndEx(0,"e5(250,0)")
                                        n="Mi"
                                
                                        
                                elif axis.m_aY>0.5:
                                        n="Re"
                                        sdk.PlaySndEx(0,"d5(250,0)")
                                elif axis.m_aY<-0.5:
                                        n="Do"
                                        sdk.PlaySndEx(0,"c5(250,0)")
                                
                                        
                                elif axis.m_aZ>0.5:
                                        sdk.PlaySndEx(0,"c6(250,0)")
                                        n="Do"
                                elif axis.m_aZ<-0.5:
                                        sdk.PlaySndEx(0,"b5(250,0)")
                                        n="Si"
                                
                                        
                                elif axis.m_rZ>0.5:
                                        sdk.PlaySndEx(0,"g5(250,0)")
                                        n="Sol"
                                elif axis.m_rZ<-0.5:
                                        sdk.PlaySndEx(0,"a5(250,0)")
                                        n="La"
                                
                                time.sleep (1)
                                #réponse
                                print ()
                                print ("Note entendue : ",nom[r])
                                print ("Note jouee : ",n)
                                if nom[r]==n:
                                        print ("C'est gagne !")
                                        s=s+1
                                else :
                                        print ("C'est perdu !")
                                print ()
                                time.sleep (1)

                        except UnboundLocalError as e :
                                print ("Vérifier l'état du 3dRudder")
                                time.sleep (4)
                        

                print ("---------------------------------------")
                print ("|Fin de la partie:                    |")
                print ("|Vous avez marque ",s ,"point(s) sur 5   |")
                if s<3:
                        print ("|Vous devez encore progresser !       |")
                elif 2<s<5:
                        print ("|Vous avez un bon niveau !            |")
                else :
                        print ("|Felicitations !                      |")
                        if d==1:
                                print ("|Vous avez surmonté le plus difficile|")
                        else:
                                print ("|Augmentez maintenant la difficulte   |")
                print ("---------------------------------------")
                print ()
                try :
                        g=int(input("Voulez-vous enregistrer ce score (0/1) ? : "))
                except ValueError as f:
                        print ("Le choix n'a pas été reconnu")
                        g=0
                db=sqlite3.connect('score.db')
                cursor=db.cursor()
                if g==1:
                    nom=input("Entrer votre nom : ")
                    cursor.execute("INSERT INTO users(name, level, score) VALUES(?, ?, ?)", (nom, d,s))
                    db.commit ()
                    db.close ()
        else :
                print ("La valeure entrée n'est pas correcte")

##########################################################

##########################################################
#Affichage des scores
##########################################################
def score ():
        if os.path.isfile("score.db") == True:
                db=sqlite3.connect('score.db')
                cursor = db.cursor()
                cursor.execute("""SELECT score, level, name FROM users""")
                rows = cursor.fetchall()
                print ()
                print ("Les résultats sont écrits de la forme : ")
                print ("(score, niveau , nom du joueur)")
                print ()
                for point in rows:
                        print (point)
                print ()
                db.close ()
        else:
                print ()
                print ("jouer au jeu et enregistrer le score auparavant")
                print ()
        
##########################################################
        
        
##########################################################              
##########################################################
# Main
##########################################################              
##########################################################              


# 32 or 64 bit
val_max=platform.architecture()


if (val_max[0]=='32bit') : 
        from win32.ns3DRudder import * #import SDk 3dRudder
else:
        from x64.Python352.ns3DRudder import * #import SDk 3dRudder


# Init du SDK 3dRudder  
#------------
sdk=GetSDK() 
sdk.Init() 

axis=Axis() 
nPortNumber=0
p=1
                

##########################################################              
##########################################################
#####################Programme############################
##########################################################              
##########################################################      

while p==1:
        try:            
                debut ()

                choix =int(input("Entrer le numéro du mode choisi : "))

                options ={1:note,
                                2:music,
                                3:jeu,
                                4:score,
                                }
                                
                options[choix]()

        except KeyboardInterrupt as e:
                debut()
                
        
        try :   
                a=int(input("Voulez-vous quitter (0) ou retourner au menu principal (1) ?  : "))
                if a==0:
                        print ()
                        print ("------Au revoir------")
                        print ()
                        p=0
                elif a==1:
                        print()
                else:
                        print ("Le choix n'est pas correcte")
                
        except ValueError as err:
                print ("Erreur")
        

db=sqlite3.connect('score.db')
db.close()   #Fermeture de la base de données

        
