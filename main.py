#Author: Marc Muñoz Fernandez
#Github: m4rkuus
import time
from sys import stdout
#Colors
def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
despedida = """ 
                                                                                    
                                                                                    
                                                                                    
                                      ▓▓▓▓▓▓  ▓▓▓▓▓▓                                
                                      ▓▓  ░░▓▓▓▓  ▓▓▓▓▓▓                            
                                ▓▓▓▓▓▓▓▓░░  ░░▓▓░░░░▓▓▓▓  ▓▓                        
                              ▒▒▓▓░░  ▓▓░░░░░░░░░░░░▓▓░░░░▓▓                        
                                  ▒▒░░  ░░░░░░░░░░░░░░░░▓▓▓▓▒▒                      
                                  ▓▓░░░░░░░░░░░░░░░░░░░░▓▓░░▓▓                      
                ██████████    ▒▒▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓                      
            ██████      ██████    ▓▓▓▓▓▓▓▓▓▓▓▓▒▒    ▒▒▒▒▒▒▓▓▓▓                      
          ████              ████████▓▓▓▓▓▓▓▓▓▓▒▒    ▒▒  ▒▒▓▓                        
        ████                  ██████░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                          ██████████░░  ░░░░░░██░░░░░░████                          
                    ██████████    ██░░░░░░░░░░▒▒░░░░░░▒▒██                          
              ██████████          ██░░░░░░░░░░░░░░░░░░░░██                          
        ██████████                  ████░░░░░░░░░░░░░░░░██                          
      ██████                          ████░░░░░░▒▒▒▒░░██                            
    ████                              ██▓▓██░░░░░░░░██                              
  ████                          ████████▓▓▓▓████████                                
  ██                          ████▓▓▓▓▓▓████████▓▓██████                            
  ██                        ████▓▓▓▓▓▓▓▓▓▓██████▓▓██▓▓▓▓██                          
                          ▓▓████▓▓▓▓██▓▓▓▓▓▓▓▓██▓▓██▓▓██▓▓▓▓                        
                        ████████▓▓▓▓██▓▓▓▓▓▓▓▓██▓▓██▓▓██▓▓██                        
                      ██▓▓▓▓▓▓▓▓████████████████▓▓██████▓▓██                        
                      ██▓▓██▓▓▓▓████▒▒░░░░  ░░░░▓▓██▒▒██▓▓██                        
                    ██▓▓▓▓██████████▒▒  ░░░░    ▓▓██▒▒██▓▓████                      
                    ██▓▓▓▓▓▓████  ██▒▒░░    ░░░░▓▓██▒▒▒▒██████                      
                  ██▓▓▓▓▓▓▓▓██    ██▒▒░░░░      ▓▓██▒▒▒▒██▓▓██                      
                  ██▓▓▓▓▓▓▓▓██    ██▒▒░░░░░░░░░░░░▓▓██▒▒██▓▓██                      
                ██▓▓▓▓████▓▓██    ████▒▒░░    ░░░░▓▓██▒▒██▓▓▓▓██                    
                ██▓▓██░░░░██        ████████▓▓▓▓▓▓▓▓████████▓▓▓▓████                
                  ██░░░░████        ████████████████████████▓▓████░░████            
                ██░░░░░░░░██        ██▒▒░░░░░░░░░░░░░░░░████▓▓██░░░░░░░░██          
                ██░░░░░░░░░░██      ██░░    ░░░░░░░░░░░░░░░░████░░░░░░░░██          
                ██░░░░░░░░░░██      ██▒▒░░░░    ░░░░██░░░░░░████░░░░░░██            
                ██░░░░░░░░██      ██▒▒  ▒▒▒▒▒▒░░░░░░██░░░░░░░░████████              
                  ████████        ██████    ▒▒▒▒████░░████░░░░██                    
                                  ██    ████▒▒██  ████▒▒▒▒▒▒▒▒░░██                  
                                ██░░░░░░  ▒▒▒▒██    ██▒▒▒▒▒▒▒▒░░░░██                
                                ██░░░░░░▒▒▒▒██        ██▒▒▒▒▒▒▒▒░░██                
                              ██░░░░░░▒▒▒▒▒▒██        ██▒▒▒▒▒▒▒▒░░██                
                            ██░░░░░░░░▒▒▒▒██            ██▒▒▒▒▒▒▒▒░░██              
                            ██░░░░░░▒▒▒▒▒▒██            ██▒▒▒▒▒▒▒▒░░██              
                          ██░░░░░░▒▒▒▒▒▒██              ██▒▒▒▒▒▒░░░░██              
                        ██░░░░░░▒▒▒▒▒▒██                ██▒▒▒▒▒▒▒▒░░██              
                        ██░░░░░░▒▒▒▒▒▒██                ██▒▒▒▒▒▒▒▒░░██              
                          ██░░▒▒▒▒▒▒██                    ████████████              
                        ████████████                        ████████                
                        ██▓▓▓▓████                          ██▓▓▓▓██                
                      ████████████                        ██▓▓██████████            
                    ██▓▓▓▓▓▓▓▓██                          ██▓▓▓▓▓▓▓▓▓▓▓▓████        
                  ██▓▓▓▓▓▓▓▓▓▓██                          ██████▓▓▓▓▓▓░░░░░░██      
                ██▓▓░░░░░░░░████                                ██████████████      
                ██████████████                                                      
                                                                                    

"""


#Empezamos El Script
blue()
print("[+]Autor Marc Muñoz Fernandez[+]")

empezar = input("Quieres Empezar El Test Sobre La Serie Naruto (s/n)?")
if empezar == "s" :
        print("¡[+]El Test Tiene 5 Preguntas Respondelas Bien Todas Para Ganar :P[+]")
        print("[+]¡Empezamos El Test[+]!")
else:
    print("Adios xD :(")
    exit()
print("[+]Bienvenido Al Test De Naruto[+]")
preg1 = input("En que capitulo/episodio Sasuke besa a Naruto: ")
if preg1 == "3":
    print("¡Respuesta Correcta!")
else:
    print("Fallastes La Pregunta :(")
    print("Vuelva A Intentarlo :)")
    exit()
preg2 = input("En Que capitulo/episodio es la ultima pelea de Naruto y Sasuke En Naruto Shippuden?: ")
if preg2 == "477":
    print("¡Respuesta Correcta!")
else:
    print("Volvistes A Fallar")
    exit()

print("Usa La Primera Letra del nombre en mayusculas para no tener errores!")
preg3 = input("Finalmente Quien Se Casa Con Hinata?: ")
if preg3 == "Naruto":
    print("¡Respuesta Correcta!")
else:
    print("Volvistes a Fallar")
    exit()
print("Usa La Primera Letra del nombre en mayusculas para no tener errores!")
preg4 = input("Qual Es la bestia que lleva Naruto dentro de ella?: ")
if preg4 == "Kurama":
    print("¡Respuesta Correcta!")
else:
    print("Volvistes A Fallar! :(")
    exit()
print("Usa La Primera Letra del nombre en mayusculas para no tener errores!")
preg5 = input("Quien se convertio Primero En Chunin?: ")
if preg5 == "Ino":
    print("¡Respuesta Correcta!")
    print(despedida)
    print("Felicidades Acabastes El Test Sobre La Serie De Naruto")
else:
    print("Volvistes a Fallar!")
    exit()