from setuptools import setup, find_packages

setup(
    name="MiPaqueteEjemplo",      # Nombre del paquete
    version="0.1",
    packages=find_packages(),
    py_modules=['my_functions'],    # Indicamos el módulo que queremos incluir
    install_requires=[
        'mumpy',
        'pandas',
        "matplotlib",
        "statsmodels",
        "prophet"
    ],
    description="Un paquete de ejemplo con dos funciones: una que multiplica y otra que suma.",
    author="Tu Nombre",
    author_email="tu_email@example.com",
)


