#Estudiante: David Fernando Cruz Martinez
#Correo: david.cruz01@correo.usa.edu.co
#Carrera: Ingenieria de Sistemas y Telecomunicaciones
#Profesor: John Jairo Corredor Franco
#MATERIA: Computacion Paralela y Distribuida
#UNIVERSIDAD SERGIO ARVOLEDA
#FECHA: 11/05/2021

from py_simulador import *


def main():
    sun = Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30
    #sun.pencolor('yellow')

    earth = Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10**24
    earth.px = -1*AU
    earth.vy = 29.783 * 1000            # 29.783 km/sec
    #earth.pencolor('blue')

    # Venus parameters taken from
    # http://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html
    venus = Body()
    venus.name = 'Venus'
    venus.mass = 4.8685 * 10**24
    venus.px = 0.723 * AU
    venus.vy = -35.02 * 1000
    #venus.pencolor('red')

    loop([sun, earth, venus])

if __name__ == '__main__':
    main()    
