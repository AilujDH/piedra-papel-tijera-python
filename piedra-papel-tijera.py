nombre1= input ("Hola Jugador 1! Cual es tu nombre?: ")
nombre2= input ("Hola Jugador 2! Cual es tu nombre?: ")

jugador1= input ("Hola (nombre1) Que eliges? piedra, papel o tijera?: ")
jugador2= input ("Hola (nombre2): Que eliges? piedra, papel o tijera?: ")

if jugador1 == jugador2:
    print ("Empate!")
elif (jugador1 == "piedra" and jugador2== "tijera") or (jugador1== "papel" and jugador2== "piedra") or (jugador1== "tijera" and jugador2== "papel"):
 print ("Ha ganado", nombre1)
else:
   print ("Ha ganado", nombre2)
