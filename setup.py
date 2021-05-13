#Estudiante: David Fernando Cruz Martinez
#Correo: david.cruz01@correo.usa.edu.co
#Carrera: Ingenieria de Sistemas y Telecomunicaciones
#Profesor: John Jairo Corredor Franco
#MATERIA: Computacion Paralela y Distribuida
#UNIVERSIDAD SERGIO ARVOLEDA
#FECHA: 11/05/2021

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext


ext_modules = [
    Extension('CySimulador',
              ['CySimulador.pyx'],
              libraries=['m'],
              extra_compile_args=['-ffast-math',
                                  '-fopenmp', '-march=native'],
              extra_link_args=['-fopenmp']
              )]

setup(
    name='CySimulador',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
)
