from setuptools import setup, find_packages

setup(
    name="MiPaqueteEjemplo",       # Nombre del paquete
    version="0.1",
    packages=find_packages(),      # Busca automáticamente todos los submódulos
    py_modules=['my_functions'],   # Como nuestro archivo no está dentro de una carpeta, lo especificamos aquí
    install_requires=[
        # Lista de dependencias, por ejemplo: 'numpy', 'pandas', ...
    ],
    description="Un paquete de ejemplo con una función simple.",
    author="Tu Nombre",
    author_email="tu_email@example.com",
)
