####################################################################
#                                                                  #
#       Python 3.5.2                                               #
#                                                                  #
#       Play music notes and train your memory with 3dRudder       #
#                                                                  #
####################################################################



##########################################################
#Imports
##########################################################
import sys
import time
import platform
import random
import sqlite3
import os




##########################################################
#Play music
##########################################################
def music () :
        print ("------------------------------------")
        tempo=int(input("Enter beat per minute : "))
        print ("------------------------------------")
        print ("Do Ctrl + C to stop")
        while True :

                sdk.GetAxis(0,NormalizedValue,axis)
                
                if axis.m_aX>0.5:
                        sdk.PlaySndEx(0,"f5(100,0)")
                        print ("F")
                elif axis.m_aX<-0.5:
                        sdk.PlaySndEx(0,"e5(100,0)")
                        print("E")
                
                        
                elif axis.m_aY>0.5:
                        print ("D")
                        sdk.PlaySndEx(0,"d5(100,0)")
                elif axis.m_aY<-0.5:
                        print("C")
                        sdk.PlaySndEx(0,"c5(100,0)")
                
                        
                elif axis.m_aZ>0.5:
                        sdk.PlaySndEx(0,"c6(100,0)")
                        print ("C")
                elif axis.m_aZ<-0.5:
                        sdk.PlaySndEx(0,"b5(100,0)")
                        print("B")
                
                        
                elif axis.m_rZ>0.5:
                        sdk.PlaySndEx(0,"g5(100,0)")
                        print ("G")
                elif axis.m_rZ<-0.5:
                        sdk.PlaySndEx(0,"a5(100,0)")
                        print("A")
                
                        
                print ()
                        
                time.sleep (60/tempo)
        
##########################################################
#Begining
##########################################################      
def begining ():   
        print ()
        print ("-------3dMusic-------")
        print ()
        print("Music notes' position : 1")
        print("Play music : 2")
        print ("Memory game : 3")
        print ("Scores : 4")
        print ()
        


##########################################################
#Music notes' position
##########################################################      
def note():
        print ()
        print ("Back      : C             Front     : D")
        print ("Left      : E             Right     : F ")
        print ("RotateLeft: G             RotateLeft: A")
        print ("Down      : B             Up        : C")
        print ()
        b=input("Return to menu ? (y/n) : ")
        if b=="y":
                begining()
        elif b=="n":
                note()
        else :
                print("Choice not correct")
                note()
##########################################################

        
##########################################################
#Memory game
##########################################################      
def game():

        ####################################
        #Data base for scores
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
        print ("You should hear the music note" )
        print ("and then replay it on ")
        print ("the 3dRudder, 5 times")
        print ()
        print ("--------------------")
        d=int(input("Enter the level (1 -> difficult ; 5 -> easy) : "))
        if 1<=d<=5:
                s=0
                for j in range (0,5):
                        try :
                                print ("Hear !")
                                notes = ["c5(500,0)","d5(500,0)","e5(500,0)","f5(500,0)","g5(500,0)","a5(500,0)","b5(500,0)","c6(500,0)",]
                                nom =["C","D","E","F","G","A","B","C"]
                                r=random.randint (0,7)
                                sdk.PlaySndEx(0,notes[r])
                                time.sleep(1)
                                print ("You have ",d,"sec to position")
                                time.sleep (d)
                                print ("--------------------")
                                print("Replay !")
                                sdk.GetAxis(0,NormalizedValue,axis)
                                        
                                if axis.m_aX>0.5:
                                        sdk.PlaySndEx(0,"f5(250,0)")
                                        n="F"
                                elif axis.m_aX<-0.5:
                                        sdk.PlaySndEx(0,"e5(250,0)")
                                        n="E"
                                
                                        
                                elif axis.m_aY>0.5:
                                        n="D"
                                        sdk.PlaySndEx(0,"d5(250,0)")
                                elif axis.m_aY<-0.5:
                                        n="C"
                                        sdk.PlaySndEx(0,"c5(250,0)")
                                
                                        
                                elif axis.m_aZ>0.5:
                                        sdk.PlaySndEx(0,"c6(250,0)")
                                        n="C"
                                elif axis.m_aZ<-0.5:
                                        sdk.PlaySndEx(0,"b5(250,0)")
                                        n="B"
                                
                                        
                                elif axis.m_rZ>0.5:
                                        sdk.PlaySndEx(0,"g5(250,0)")
                                        n="G"
                                elif axis.m_rZ<-0.5:
                                        sdk.PlaySndEx(0,"a5(250,0)")
                                        n="A"
                                
                                time.sleep (1)

                                print ()
                                print ("Heard : ",nom[r])
                                print ("Played : ",n)
                                if nom[r]==n:
                                        print ("You win !")
                                        s=s+1
                                else :
                                        print ("You lose !")
                                print ()
                                time.sleep (1)

                        except UnboundLocalError as e :
                                print ("Verify sate of 3dRudder")
                                time.sleep (4)

                print ("------------------------------------")
                print ("|End of game:                      |")
                print ("|You have ",s ,"point(s)              |")
                if s<3:
                        print ("| You must play again!             |")
                elif 2<s<5:
                        print ("| Good job !                       |")
                else :
                        print ("|Congratulation !                  |")
                        if d==1:
                                print ("|You have done the most difficult !|")
                        else:
                                print ("|Now you can change the level      |")
                print ("------------------------------------")
                print ()
                g=input("Do you want to save this score (y/n) ? : ")
                db=sqlite3.connect('score.db')
                cursor=db.cursor()
                if g=="y":
                    nom=input("Enter your name : ")
                    cursor.execute("INSERT INTO users(name, level, score) VALUES(?, ?, ?)", (nom, d,s))
                    db.commit ()
                    db.close ()
                elif g=="n":
                    print ("Maybe the next time")
                    print ()
                else:
                    print ("The choice is not correct")
        else :
                print ("It isn't correct")

##########################################################

##########################################################
#Print the scores
##########################################################
def score ():
        if os.path.isfile("score.db") == True:
                db=sqlite3.connect('score.db')
                cursor = db.cursor()
                cursor.execute("""SELECT score, level, name FROM users""")
                rows = cursor.fetchall()
                print ()
                print ("It is written like this : ")
                print ("(score, level , name of player)")
                print ()
                for point in rows:
                        print (point)
                print ()
                db.close ()
        else:
                print ()
                print ("Play at the game and save your score before")
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
        from x64.ns3DRudder import * #import SDk 3dRudder


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
                begining ()

                choix =int(input("Enter the number of the choice : "))

                options ={1:note,
                                2:music,
                                3:game,
                                4:score,
                                }
                                
                options[choix]()

        except KeyboardInterrupt as e:
                begining()
                
        
        try :   
                a=int(input("Do you want to quit (0) or return to main menu (1) ?  : "))
                if a==0:
                        print ()
                        print ("------Bye------")
                        print ()
                        p=0
                elif a==1:
                        print()
                else:
                        print ("The choice isn't corect")
                
        except ValueError as err:
                print ("Error")
        

db=sqlite3.connect('score.db')
db.close()   #Close the data base

        
