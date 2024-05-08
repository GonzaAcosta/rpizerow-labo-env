from gpiozero import LED
from time import sleep

ledVERDE = LED(13)
ledROJO = LED(19)
ledAZUL = LED(26)

while True:
	sleep(0.25)
	ledVERDE.on()
#enciende el led verde por 25 milisegundos.
	sleep(0.25)
	ledVERDE.off()
	ledAZUL.on()
# después de 50 milisegundos, se enciende el led azul.
	sleep(0.25)
	ledVERDE.on()
	sleep(0.25)
	ledVERDE.off()
	ledAZUL.off()
	ledROJO.on()
#luego de pasar 1 segundo, se apagan los 2 led´s anteriores y se enciende el rojo 
	sleep(0.25)
	ledVERDE.on()
	sleep(0.25)
	ledVERDE.off()
	ledAZUL.on()
	sleep(0.25)
	ledVERDE.on()
	sleep(0.25)
#pasan 2 segundos y se apagan todos los led´s
	ledVERDE.off()
	ledAZUL.off()
	ledROJO.off() 
