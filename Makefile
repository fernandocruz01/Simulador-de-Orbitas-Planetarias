#Estudiante: David Fernando Cruz Martinez
#Correo: david.cruz01@correo.usa.edu.co
#Carrera: Ingenieria de Sistemas y Telecomunicaciones
#Profesor: John Jairo Corredor Franco
#MATERIA: Computacion Paralela y Distribuida
#UNIVERSIDAD SERGIO ARVOLEDA
#FECHA: 11/05/2021

all:
		python3 setup.py build_ext --inplace

clean:
		rm -rf build *.so *_simulador.c *html
