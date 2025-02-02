import numpy as np
import pandas as pd

def generar_datos_sinteticos(
    n_years=5,
    elasticity=-1.5,
    Q0=200,
    random_seed=42,
    trend_coef=0.5,
    seasonality_amplitude=10,
    seasonality_period=52,
    noise_std=5,
    p0=50  # Nuevo parámetro para definir el precio
):
    """
    Genera datos sintéticos de ventas y precios para un producto durante n_years años de datos semanales.
    
    Parámetros:
    - n_years: Número de años que se desean generar (por defecto 5).
    - elasticity: Elasticidad de la demanda respecto al precio (por defecto -1.5).
    - Q0: Demanda base (por defecto 200).
    - random_seed: Semilla para reproducibilidad de los números aleatorios (por defecto 42).
    - trend_coef: Coeficiente de la tendencia lineal (por defecto 0.5).
    - seasonality_amplitude: Amplitud de la estacionalidad (por defecto 10).
    - seasonality_period: Periodo de la estacionalidad (por defecto 52 semanas).
    - noise_std: Desviación estándar del ruido aleatorio (por defecto 5).
    - price: Valor del precio (por defecto 50).
    
    Retorna:
    - df: Un DataFrame de pandas con las columnas:
        * 'week': Fecha correspondiente a cada semana.
        * 'sales': Ventas estimadas.
        * 'price': Precio utilizado para la simulación.
    """
    # Configurar la semilla para la reproducibilidad
    np.random.seed(random_seed)

    # Calcular el número total de semanas
    n_weeks = n_years * 52
    time = np.arange(n_weeks)

    # Generar precios: en este ejemplo se utiliza el precio constante proporcionado por el parámetro
    prices = p0  
    
    # Calcular la demanda base utilizando la elasticidad
    sales = Q0 * (prices / p0) ** elasticity

    # Agregar tendencia, estacionalidad y ruido aleatorio
    trend = trend_coef * time
    seasonality = seasonality_amplitude * np.sin(2 * np.pi * time / seasonality_period)
    random_noise = np.random.normal(scale=noise_std, size=n_weeks)
    sales += trend + seasonality + random_noise

    # Crear DataFrame con fechas semanales
    df = pd.DataFrame({
        'week': pd.date_range(start='2018-01-01', periods=n_weeks, freq='W'),
        'sales': sales,
        'price': prices
    })

    return df

# Ejemplo de uso:
if __name__ == "__main__":
    # Se puede modificar el parámetro 'price' para simular diferentes escenarios
    df_sinteticos = generar_datos_sinteticos(
        n_years=5,
        elasticity=-1.5,
        Q0=200,
        random_seed=42,
        trend_coef=0.5,
        seasonality_amplitude=10,
        seasonality_period=52,
        noise_std=5,
        p0=50  # Precio base definido desde el parámetro
    )
    print(df_sinteticos.head())
