# Importowanie bibliotek
from enum import Enum
import matplotlib.pyplot as plt
import pandas as pd

from funkcje import * 

class Main(Enum):
    DELETE_MISSING = 1
    FILL_WITH_LAST_VALID = 2
    FILL_WITH_MEAN = 3

main = Main.DELETE_MISSING

def div():
    print("\n======================================================\n")

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

# Surowe dane 
for i in range(6):
    draw_sample_value_plot(series[i], 
                           f"Surowe dane seria {i//2+1}, pomiar {i%2+1} w zależności od numeru próbki",
                           "", "[℃]")

for i in range(6):
    if main == Main.DELETE_MISSING:
        series[i] = clean_data(series[i])
    elif main == Main.FILL_WITH_LAST_VALID:
        series[i] = fill_with_last_valid(series[i])
    elif main == Main.FILL_WITH_MEAN:
       series[i] = fill_with_mean(series[i])

# Usuwanie wartości odstających dla każdej próbk
for i in range(6):    
    series[i] = remove_outliers(series[i], 4)

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
    print(f"Rozmiar seria {i//2+1}, pomiar {i%2+1}: {lengths[i]}")

# Wyświetlenie wyników
div()
print("Wyniki po usunieciu NaN")
stat_names = ["Średnia", "Rozstęp", "Kurtoza", "Mediana", "Skośność", "Wartość modalna"]
units =      ["℃",      "℃",      "",        "℃",      "",         "℃"]
for i in range(6):
    print(f"Statystyki dla seria {i//2+1}, pomiar {i%2+1}\n")
    for name, value, unit in zip(stat_names, stats[i], units):
        print(f"{name}: {value.values if isinstance(value, pd.Series) else value} {unit}")
    div()


for k in range(len(stat_names) - 1):
    draw_bars_for_stat([stats[s][k] for s in range(6)],
                       f"{stat_names[k]} dla wszystkich serii",
                       [f"seria {i//2+1}, pomiar {i%2+1}" for i in range(6)],
                       units[k],
                       colors=["#bf77f6", "#9a0eea",
                               "#d5b60a", "#fac205",
                               "#137e6d", "#7af9ab"])

# Wykresy dla wartosci T   
for i in range(6):
    draw_sample_value_plot(series[i], 
                           f"Zależność seria {i//2+1}, pomiar {i%2+1} od numeru próbki",
                           "", "[℃]")

# Rysowanie wykresów dla każdej próbki
plt.figure(figsize=(12, 6))

# Wykres 1
# colors = ["#f5634280", "#5142f580", "#14821580"]
colors = ["#bf77f6", "#d5b60a", "#137e6d"]
for i in range(0, 6, 2):
    # plt.subplot(1, 3, i//2+1)  # 1 wiersz, 3 kolumny, 1. wykres
    series_match1, series_match2 = match_length(clean_data(series[i]), clean_data(series[i+1]))
    plt.scatter(series_match1, series_match2, label=f"Seria {i//2+1}", 
                color=colors[i//2])
    plt.title(f"Seria {i//2+1} pomiar 1 vs pomiar 2")
    plt.xlabel('Pomiar 1 [℃]')
    plt.ylabel('Pomiar 2 [℃]')
    plt.axis('equal')
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
    draw_histogram(series[i], f'Histogram seria {i//2+1}, pomiar {i%2+1}',
                   unit="[℃]")

draw_envelopes(series, "Obwiednie rozkładów ze wszystkich serii", "[℃]")

for i in range(6):
    print(f"Odchylenie standardowe seria {i//2+1}, pomiar {i%2+1}: {std(series[i])}")