oimport secrets
import string
import math

def calcular_entropia(longitud,caracteres_disponibles):
	return longitud *math.log2(len(caracteres_disponibles))

def generar_contrasena(longitud=20):
	caracteres = string.ascii_letters + string.digits + string.punctuation
	contrasena = ' '.join(secrets.choice(caracteres) for _ in range(longitud))
	entropia =calcular_entropia(longitud,caracteres)
	return contrasena, entropia

if __name__ == "__main__":
	print("===*** GENERADOR DE CONTRASEÑAS SEGURAS NIVEL MILITAR *** ===")
	try:
		longitud = int(input("longitud de contraseña (minimo 20 caracteres recomendado): "))
		if longitud < 8: 
			raise valueError("la longitud debe ser de almenos 8 caracteres.")
		contrasena, entropia = generar_contrasena(longitud)
		print(f"\n*** TU CONTRASEÑA SEGURA ES ***:\n{contrasena}")
		print(f"Entropia estimada: {entropia:.2f}bits")
		if entropia >=128:
			print("nivel de seguridad: MILITAR (128+ BITS)")
		elif entropia >= 80:
			print("Nivel de seguridad : ALTO")
		else:
			print("NIvel de seguridad: BAJO")
	except ValueError as e:
		print(f"Error: {e}")




