# Importar librerías necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generar_series_sintetica(n_weeks=104, 
                             start_date='2020-01-01',
                             precio_base=50,
                             demanda_base=200,
                             tendencia_precio_coef=0.1,
                             tendencia_demanda_coef=-0.5,
                             amplitude_estacionalidad_precio=5,
                             amplitude_estacionalidad_demanda=10,
                             sigma_precio=2,
                             sigma_demanda=5,
                             elasticidad=-1.5,
                             periodo_estacional=52,
                             seed=42,
                             plot=True):
    """
    Genera series sintéticas semanales de precios y demanda considerando:
      - Tendencia
      - Estacionalidad
      - Ruido blanco
      - Elasticidad de la demanda respecto del precio

    Parámetros:
      - n_weeks: Número de semanas a generar.
      - start_date: Fecha de inicio para la serie de tiempo.
      - precio_base: Valor base para el precio.
      - demanda_base: Valor base para la demanda.
      - tendencia_precio_coef: Coeficiente de la tendencia lineal para el precio.
      - tendencia_demanda_coef: Coeficiente de la tendencia lineal para la demanda.
      - amplitude_estacionalidad_precio: Amplitud de la componente estacional del precio.
      - amplitude_estacionalidad_demanda: Amplitud de la componente estacional de la demanda.
      - sigma_precio: Desviación estándar del ruido blanco para el precio.
      - sigma_demanda: Desviación estándar del ruido blanco para la demanda.
      - elasticidad: Elasticidad de la demanda respecto del precio.
      - periodo_estacional: Número de periodos (semanas) que conforman un ciclo estacional.
      - seed: Semilla para la generación aleatoria.
      - plot: Booleano que indica si se deben graficar las series.

    Retorna:
      - df: DataFrame con las series de precio y demanda.
    """
    
    # Configuración para reproducibilidad
    np.random.seed(seed)
    
    # Creación del rango de fechas y vector de tiempo
    date_range = pd.date_range(start=start_date, periods=n_weeks, freq='W')
    t = np.arange(n_weeks)
    
    # -------------------------------
    # Generación de la serie de PRECIOS
    # -------------------------------
    # Componente de tendencia
    tendencia_precio = tendencia_precio_coef * t  
    # Componente estacional (senoidal)
    estacionalidad_precio = amplitude_estacionalidad_precio * np.sin(2 * np.pi * t / periodo_estacional)
    # Ruido blanco
    ruido_precio = np.random.normal(0, sigma_precio, size=n_weeks)
    # Serie de precios
    precio = precio_base + tendencia_precio + estacionalidad_precio + ruido_precio
    
    # -------------------------------
    # Generación de la serie de DEMANDA
    # -------------------------------
    # Componente de tendencia
    tendencia_demanda = tendencia_demanda_coef * t  
    # Componente estacional (cosenoidal)
    estacionalidad_demanda = amplitude_estacionalidad_demanda * np.cos(2 * np.pi * t / periodo_estacional)
    # Ruido blanco
    ruido_demanda = np.random.normal(0, sigma_demanda, size=n_weeks)
    # Demanda baseline sin efecto del precio
    demanda_baseline = demanda_base + tendencia_demanda + estacionalidad_demanda
    # Incorporación del efecto del precio mediante elasticidad (modelo multiplicativo)
    demanda = demanda_baseline * (precio / precio_base) ** elasticidad + ruido_demanda
    # Asegurarse que la demanda no sea negativa
    demanda = np.maximum(demanda, 0)
    
    # -------------------------------
    # Organización de los datos en un DataFrame
    # -------------------------------
    df = pd.DataFrame({
        'Fecha': date_range,
        'Precio': precio,
        'Demanda': demanda
    })
    df.set_index('Fecha', inplace=True)
    
    # Graficar las series generadas si se solicita
    if plot:
        plt.figure(figsize=(14, 8))
        
        plt.subplot(2, 1, 1)
        plt.plot(df.index, df['Precio'], marker='o', linestyle='-')
        plt.title('Serie Semanal de Precio')
        plt.ylabel('Precio')
        plt.grid(True)
        
        plt.subplot(2, 1, 2)
        plt.plot(df.index, df['Demanda'], marker='o', linestyle='-', color='orange')
        plt.title('Serie Semanal de Demanda')
        plt.ylabel('Demanda')
        plt.xlabel('Fecha')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()
    
    return df

# Ejemplo de uso:
df_series = generar_series_sintetica(n_weeks=104, seed=123)
print("Primeras filas de la serie generada:")
print(df_series.head())
