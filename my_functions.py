import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

def generar_datos_sinteticos(n_years=5, elasticity=-1.5, Q0=200, random_seed=42):
    """
    Genera datos sintéticos de ventas y precios para un producto durante n_years años de datos semanales.
    """
    # Configurar semilla para reproducibilidad
    np.random.seed(random_seed)

    # Número total de semanas
    n_weeks = n_years * 52
    time = np.arange(n_weeks)

    # Generar precios fluctuantes
    prices = 50 + 5 * np.sin(2 * np.pi * time / 52) + np.random.normal(scale=2, size=n_weeks)

    # Precio base y demanda base
    P0 = np.mean(prices)

    # Generar demanda utilizando la elasticidad
    sales = Q0 * (prices / P0) ** elasticity

    # Agregar tendencia, estacionalidad y ruido aleatorio
    trend = 0.5 * time
    seasonality = 10 * np.sin(2 * np.pi * time / 52)
    random_noise = np.random.normal(scale=5, size=n_weeks)
    sales += trend + seasonality + random_noise

    # Crear DataFrame con fechas semanales
    df = pd.DataFrame({
        'week': pd.date_range(start='2018-01-01', periods=n_weeks, freq='W'),
        'sales': sales,
        'price': prices
    })

    return df  # <-- Esta línea debe estar indentada dentro de la función
