import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
from scipy.stats import norm
import math

def std(series):
    N = len(series) - 1
    mean_v = stat.mean(series)
    std_v = 0.0
    for value in series:
        std_v += ((value - mean_v)**2) / N
    return math.sqrt(std_v)

# Wykresy zależności numeru próbki od wartości próbki
def draw_sample_value_plot(data, title, unit_x = "", unit_y = ""):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data, marker='.', label='Wartości', color="#0504aa")
    plt.title(title)
    plt.xlabel(f'Numer próbki {unit_x}')
    plt.ylabel(f'Wartość próbki {unit_y}')
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

#Narysuj fragment przebiegu
def draw_sample_value_plot_cast(data, title, start=None, end=None):
    # Jeśli start i end są określone, pobierz dane z tego zakresu
    if start is not None and end is not None:
        data = data[start:end]
    
    plt.figure()
    plt.plot(data, marker='o', color="#0504aa")
    plt.title(title)
    plt.xlabel('Numer próbki')
    plt.ylabel('Wartość')
    plt.grid()
    plt.show()
    
# Funkcja do identyfikacji nieliczbowych wartości i przedziałów ich występowania
def check_non_numeric_intervals(data_series, column_name):
    # Lista indeksów pustych pól lub pól zawierających tylko spacje
    empty_indices = data_series[data_series.apply(lambda x: pd.isnull(x) or str(x).isspace())].index.tolist()
    empty_count = len(empty_indices)

    # Funkcja do określania przedziałów
    def get_ranges(indices):
        if not indices:
            return []
        ranges = []
        start = indices[0]
        for i in range(1, len(indices)):
            if indices[i] != indices[i - 1] + 1:
                ranges.append((start, indices[i - 1]))
                start = indices[i]
        ranges.append((start, indices[-1]))
        return ranges

    # Znalezienie przedziałów pustych pól
    empty_ranges = get_ranges(empty_indices)
    print(empty_ranges)
    
    #Funkcja do rysowania histogramu
def draw_histogram(data, raw_data, title, bins=15, unit = ""):
    plt.figure(figsize=(12, 6))
    data = data.dropna()
    plt.hist(data.dropna(), bins=bins, color='#75bbfd', edgecolor='#0504aa', density=True)

    mean, std_v = stat.mean(raw_data), std(raw_data)
    x = np.linspace(min(data), max(data), 1000)
    fitted_pdf = norm.pdf(x, mean, std_v)
    plt.plot(x, fitted_pdf, color='red', linestyle='--', linewidth=2)

    plt.axvline(mean, linestyle="--", color="#0504aa", label="Wartość średnia")
    plt.axvline(mean + 2 * std_v, linestyle="--", color="gray")
    plt.axvline(mean - 2 * std_v, linestyle="--", color="gray", label="Dwa odchylenia standardowe od średniej")

    plt.title(title)
    plt.xlabel(F'Wartość {unit}')
    plt.ylabel('Gęstość [%]')
    plt.grid(axis='y', alpha=0.6)
    plt.legend()
    plt.show()

def draw_envelopes(data, title, unit = ""):
    plt.figure(figsize=(12, 6))
    for i in range(len(data)):
        mean, std_v = stat.mean(data[i]), std(data[i])
        x = np.linspace(min(data[i]), max(data[i]), 1000)
        fitted_pdf = norm.pdf(x, mean, std_v)
        plt.plot(x, fitted_pdf, linestyle='--', linewidth=2, label=f"seria {i//2+1}, pomiar {i%2+1}")
    plt.title(title)
    plt.xlabel(f'Wartość {unit}')
    plt.ylabel('Gęstość [%]')
    plt.grid(axis='y', alpha=0.75)
    plt.legend()
    plt.show()

def draw_bars_for_stat(stats, title, labels, unit = "", colors = []):
    plt.figure(figsize=(12, 6))
    plt.title(title)

    bars = plt.bar(labels, stats, width=0.8, edgecolor="white", linewidth=0.7)

    for i in range(len(stats)):
        plt.text(i, stats[i]/2, "%.2f" % stats[i], ha = 'center')
        if colors != []:
            bars[i].set_color(colors[i])
            bars[i].set_label(labels[i])

    plt.ylabel(f'Wartość {unit}')
    plt.xlabel('Seria')

    # plt.grid(alpha=0.75)
    plt.legend()
    plt.show()

# Funkcja do oczyszczania danych
def clean_data(data):
    # Przekształcenie na numery, błędne wartości zamieniane są na NaN
    cleaned_data = pd.to_numeric(data, errors='coerce')
    return cleaned_data.dropna()  # Usunięcie NaN

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
    
    #Wprowadz wartosc srednia w puste miejsca
def fill_with_mean(data):
    mean_value = data.mean()  # Oblicz średnią
    return data.fillna(mean_value)

# Funkcja do usuwania wartości odstających
def remove_outliers(data, std_mul):
    mean = data.mean()
    std_v = data.std()
    # Zatrzymujemy tylko te wartości, które są w zakresie n odchyleń standardowych od średniej
    clean = data[(data >= mean - std_mul * std_v) & (data <= mean + std_mul * std_v)]
    print(f"Ilość przed czysczeniem {len(data)}, i po czyszczeniu {len(clean)}")
    return clean

