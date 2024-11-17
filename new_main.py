# Importowanie bibliotek
from enum import Enum
import math
import matplotlib.pyplot as plt
import pandas as pd
import statistics as stat

from funkcje import * 

def div():
    print("\n======================================================\n")

class Main(Enum):
    M1 = 1
    M2 = 2
    M3 = 3

main = Main.M2

# Odczyt danych z pliku Excel
dataframe = pd.read_excel('dane.xlsx', sheet_name='A3')

series = [
    dataframe.iloc[:, 2],
    dataframe.iloc[:, 3],
    dataframe.iloc[:, 9],
    dataframe.iloc[:, 10],
    dataframe.iloc[:, 16],
    dataframe.iloc[:, 17]
]

if main == Main.M1:
    # Naprawiam braki w liczbach
    print("Usuwam znaki typu NaN")
    for i in range(6):
        series[i] = clean_data(series[i])
elif main == Main.M2:
    # Zastosowanie funkcji do każdej zmiennej - uzupelnij braki ostatnia liczba Valid
    for i in range(6):
        series[i] = fill_with_last_valid(series[i])
elif main == Main.M3:
    #Naprawiam braki w liczbach
    for i in range(6):
        series[i] = fill_with_mean(series[i])

# Usuwanie wartości odstających dla każdej próbk
for i in range(6):    
    series[i] = remove_outliers(series[i])

stats = []
# Obliczanie statystyk dla każdej zmiennej
for item in series:
    stats.append(calculate_statistics(item))

lengths = []
#Test poprawnosci dzialania na uzupelnianiu brakow danych - po usuwaniu NaN
for item in series:
    lengths.append(len(item))

div()
for i in range(6):
    print(f"Rozmiar seria {i//2+1}, proba {i%2+1}: {lengths[i]}")

# Wyświetlenie wyników
div()
print("Wyniki po usunieciu NaN")
stat_names = ["Średnia", "Rozstęp", "Kurtosis", "Mediana", "Skewness", "Wartość modalna"]
for i in range(6):
    print(f"Statystyki dla seria{i//2+1}, proba{i%2+1}\n")
    for name, value in zip(stat_names, stats[i]):
        print(f"{name}: {value.values if isinstance(value, pd.Series) else value}")
    div()

# Wykresy dla wartosci T   
for i in range(6):
    draw_sample_value_plot(series[i], f"Zależność seria {i//2+1}, proba {i%2+1} od numeru próbki - usuwamy Nan")

# Rysowanie wykresów dla każdej próbki
plt.figure(figsize=(12, 6))

# Wykres 1
colors = ["blue", "orange", "green"]
for i in range(0, 6, 2):
    plt.subplot(1, 3, i//2+1)  # 1 wiersz, 3 kolumny, 1. wykres
    series_match1, series_match2 = match_length(clean_data(series[i]), clean_data(series[i+1]))
    plt.plot(series_match1, series_match2, marker='o', label=f"Seria {i//2+1}", color=colors[i//2])
    plt.title(f"Seria {i//2+1} proba 1 vs proba 2")
    plt.xlabel('Proba 1')
    plt.ylabel('Proba 2')
    plt.legend()
    plt.grid()

plt.tight_layout()
plt.show()

# #Wykresy dla wartosci T - wybrany przedzial 
# #draw_sample_value_plot_cast((T1_proba1), 'Zależność T1_proba1 od numeru próbki - usuwamy Nan - Fragment',20,100)
# #draw_sample_value_plot_cast((T2_proba1), 'Zależność T2_proba1 od numeru próbki - usuwamy Nan - Fragment',9800,9999)
# #draw_sample_value_plot_cast((T1_proba2), 'Zależność T1_proba2 od numeru próbki - usuwamy Nan - Fragment',20,100)
# draw_sample_value_plot_cast((T2_proba2), 'Zależność T2_proba2 od numeru próbki - usuwamy Nan - Fragment',9800,9999)
# #draw_sample_value_plot_cast((T1_proba3), 'Zależność T1_proba3 od numeru próbki - usuwamy Nan - Fragment',20,100)
# #draw_sample_value_plot_cast((T2_proba3), 'Zależność T2_proba3 od numeru próbki - usuwamy Nan - Fragment',20,100)

#Rysowanie histogramow
for i in range(6):
    draw_histogram(series[i], f'Histogram seria {i//2+1}, proba {i%2+1}')

def std(series):
    N = len(series)
    mean_v = stat.mean(series)
    std_v = 0.0
    for value in series:
        std_v += ((value - mean_v)**2) / N
    return math.sqrt(std_v)

for i in range(6):
    print(f"Odchylenie standardowe seria {i//2+1}, proba {i%2+1}: {std(series[i])}")