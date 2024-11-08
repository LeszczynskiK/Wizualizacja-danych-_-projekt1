import pandas as pd
import matplotlib.pyplot as plt
import re

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

#Narysuj fragment przebiegu
def draw_sample_value_plot_cast(data, title, start=None, end=None):
    # Jeśli start i end są określone, pobierz dane z tego zakresu
    if start is not None and end is not None:
        data = data[start:end]
    
    plt.figure()
    plt.plot(data, marker='o')
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
def draw_histogram(data, title, bins=15):
    plt.figure(figsize=(8, 5))
    plt.hist(data.dropna(), bins=bins, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel('Wartość')
    plt.ylabel('Częstość')
    plt.grid(axis='y', alpha=0.75)
    plt.show()
    
    #Wprowadz wartosc srednia w puste miejsca
def fill_with_mean(data):
    mean_value = data.mean()  # Oblicz średnią
    return data.fillna(mean_value)

# Funkcja do usuwania wartości odstających
def remove_outliers(data):
    mean = data.mean()
    std_dev = data.std()
    # Zatrzymujemy tylko te wartości, które są w zakresie n odchyleń standardowych od średniej
    return data[(data >= mean - 5 * std_dev) & (data <= mean + 5 * std_dev)]
