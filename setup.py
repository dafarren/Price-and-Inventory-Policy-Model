from setuptools import setup, find_packages

setup(
    name="MiPaqueteEjemplo",
    version="0.1",
    packages=find_packages(),
    py_modules=['my_functions'],  # Especificamos el archivo que contiene las funciones
    install_requires=[
        # Aquí puedes agregar dependencias si las hubiera, por ejemplo: 'numpy',
    ],
    description="Un paquete de ejemplo con dos funciones: una que multiplica y otra que suma.",
    author="Tu Nombre",
    author_email="tu_email@example.com",
)
