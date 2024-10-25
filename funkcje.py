import pandas as pd
import matplotlib.pyplot as plt

# Funkcja do oczyszczania danych
def clean_data(data):
    # Przekształcenie na numery, błędne wartości zamieniane są na NaN
    cleaned_data = pd.to_numeric(data, errors='coerce')
    return cleaned_data.dropna()  # Usunięcie NaN


# Wykresy zależności numeru próbki od wartości próbki
def draw_sample_value_plot(data, title):
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data, marker='o', label='Wartości')
    plt.title(title)
    plt.xlabel('Numer próbki')
    plt.ylabel('Wartość próbki')
    plt.legend()
    plt.grid()
    plt.show()
    
# Funkcja do obliczania statystyk
def calculate_statistics(data):
    mean = data.mean()
    data_range = data.max() - data.min()
    kurtosis = data.kurtosis()
    median = data.median()
    skewness = data.skew()
    mode = data.mode()
    
    return mean, data_range, kurtosis, median, skewness, mode


# Upewnij się, że długości T1 i T2 są zgodne
def match_length(T1, T2):
    min_length = min(len(T1), len(T2))
    return T1[:min_length], T2[:min_length]

# Funkcja do zastępowania wartości nie-numerycznych
def fill_with_last_valid(data):
    # Zastąpienie wartości NaN ostatnią ważną wartością
    last_valid = None
    for i in range(len(data)):
        if pd.isnull(data[i]):  # Sprawdzenie, czy wartość jest NaN
            data[i] = last_valid  # Ustaw wartość na ostatnią nie będącą NaN
        else:
            last_valid = data[i]  # Zaktualizuj ostatnią ważną wartość
    return data
