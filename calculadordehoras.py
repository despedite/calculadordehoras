import pyfiglet

banner = pyfiglet.figlet_format("Calculador de Horas")

pagaporhora = 80

print(banner)
print("Introduce la cantidad de rondas:")
cantidaditerable = int(input())
calraw = [None] * cantidaditerable
for x in range(cantidaditerable):
	print("\nIntroduce la hora de entrada. (formato: XX:YY)")
	entrada = input()
	defentrada = entrada.split(':')
	horaentrada = int(defentrada[0])
	minutoentrada = int(defentrada[1])
	print("Introduce la hora de salida. (formato: XX:YY)")
	salida = input()
	defsalida = salida.split(':')
	horasalida = int(defsalida[0])
	minutosalida = int(defsalida[1])
	
	if minutoentrada > minutosalida:
		horasalida = horasalida - 1
		minutosalida = minutosalida + 60
	calhoras = horasalida - horaentrada
	calminutos = minutosalida - minutoentrada
	calraw[x] = (calhoras*60) + calminutos
	if x > 0:
		calacumulado = calraw[x] + calraw[x-1]
		print ("Trabajaste " + str(calhoras) + ":" + str(calminutos) + " (" + str(calraw[x]) + " minutos).")
		print("Eso es un total de "+str(calacumulado)+" minutos!")
	else:
		print ("Trabajaste " + str(calhoras) + ":" + str(calminutos) + " (" + str(calraw[x]) + " minutos).")

pagaporminuto = pagaporhora / 60
cuantaplata = calacumulado * pagaporminuto

horastotales = calacumulado / 60
minutostemp = horastotales % 1
minutostotales = minutostemp * 60

print("\nTrabajaste un gran total de " + str(int(horastotales)) + ":" + str(int(
minutostotales)) +  " (" + str(calacumulado) + " minutos)")
print("¡Eso te da un gran total de " + str(round(cuantaplata)) + "$, a " + str(round(pagaporhora)) + " pesos la hora!")