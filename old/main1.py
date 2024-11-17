# Importowanie bibliotek
import pandas as pd
import matplotlib.pyplot as plt
from funkcje import * 
# Odczyt danych z pliku Excel
dataframe1 = pd.read_excel('dane.xlsx', sheet_name='A3')

# Przypisanie danych do zmiennych
T1_proba1 = dataframe1.iloc[:, 2]
T2_proba1 = dataframe1.iloc[:, 3]
T1_proba2 = dataframe1.iloc[:, 9]
T2_proba2 = dataframe1.iloc[:, 10]
T1_proba3 = dataframe1.iloc[:, 16]
T2_proba3 = dataframe1.iloc[:, 17]

#Naprawiam braki w liczbach
T1_proba1=clean_data(T1_proba1)
T2_proba1=clean_data(T2_proba1)
T1_proba2=clean_data(T1_proba2)
T2_proba2=clean_data(T2_proba2)
T1_proba3=clean_data(T1_proba3)
T2_proba3=clean_data(T2_proba3)

# Usuwanie wartości odstających dla każdej próbki
T1_proba1 = remove_outliers(T1_proba1)
T2_proba1 = remove_outliers(T2_proba1)
T1_proba2 = remove_outliers(T1_proba2)
T2_proba2 = remove_outliers(T2_proba2)
T1_proba3 = remove_outliers(T1_proba3)
T2_proba3 = remove_outliers(T2_proba3)

# Obliczanie statystyk dla każdej zmiennej
stats_T1_proba1 = calculate_statistics(T1_proba1)
stats_T2_proba1 = calculate_statistics(T2_proba1)
stats_T1_proba2 = calculate_statistics(T1_proba2)
stats_T2_proba2 = calculate_statistics(T2_proba2)
stats_T1_proba3 = calculate_statistics(T1_proba3)
stats_T2_proba3 = calculate_statistics(T2_proba3)

#Test poprawnosci dzialania na uzupelnianiu brakow danych - po usuwaniu NaN
print("Usuwam znaki typu NaN")
T1_proba1_rozmiar = len(T1_proba1)
T2_proba1_rozmiar = len(T2_proba1)
T1_proba2_rozmiar = len(T1_proba2)
T2_proba2_rozmiar = len(T2_proba2)
T1_proba3_rozmiar = len(T1_proba3)
T2_proba3_rozmiar = len(T2_proba3)
print(f"Rozmiary: T1_proba1: {T1_proba1_rozmiar}, T2_proba1: {T2_proba1_rozmiar}, T1_proba2: {T1_proba2_rozmiar}, T2_proba2: {T2_proba2_rozmiar}, T1_proba3: {T1_proba3_rozmiar}, T2_proba3: {T2_proba3_rozmiar}")

# Wyświetlenie wyników
print("Wyniki po usunieciu NaN")
stat_names = ["Średnia", "Rozstęp", "Kurtosis", "Mediana", "Skewness", "Wartość modalna"]
for i, stats in enumerate([stats_T1_proba1, stats_T2_proba1, stats_T1_proba2, stats_T2_proba2, stats_T1_proba3, stats_T2_proba3]):
    print(f"\nStatystyki dla zmiennej {'T1_proba1' if i % 2 == 0 else 'T2_proba1' if i == 1 else 'T1_proba2' if i == 2 else 'T2_proba2' if i == 3 else 'T1_proba3' if i == 4 else 'T2_proba3'}:")
    for name, value in zip(stat_names, stats):
        print(f"{name}: {value.values if isinstance(value, pd.Series) else value}")
     
#Wykresy dla wartosci T   
draw_sample_value_plot((T1_proba1), 'Zależność T1_proba1 od numeru próbki - usuwamy Nan')
draw_sample_value_plot((T2_proba1), 'Zależność T2_proba1 od numeru próbki - usuwamy Nan')
draw_sample_value_plot((T1_proba2), 'Zależność T1_proba2 od numeru próbki - usuwamy Nan')
draw_sample_value_plot((T2_proba2), 'Zależność T2_proba2 od numeru próbki - usuwamy Nan')
draw_sample_value_plot((T1_proba3), 'Zależność T1_proba3 od numeru próbki - usuwamy Nan')
draw_sample_value_plot((T2_proba3), 'Zależność T2_proba3 od numeru próbki - usuwamy Nan')

# Rysowanie wykresów dla każdej próbki
plt.figure(figsize=(12, 6))

# Wykres 1
plt.subplot(1, 3, 1)  # 1 wiersz, 3 kolumny, 1. wykres
T1_matched1, T2_matched1 = match_length(clean_data(T1_proba1), clean_data(T2_proba1))
plt.plot(T1_matched1, T2_matched1, marker='o', label='Proba 1')
plt.title('Wykres T1 vs T2 Proba 1 -  usuwamy Nan')
plt.xlabel('T1_proba1')
plt.ylabel('T2_proba1')
plt.legend()
plt.grid()

# Wykres 2
plt.subplot(1, 3, 2)  # 1 wiersz, 3 kolumny, 2. wykres
T1_matched2, T2_matched2 = match_length(clean_data(T1_proba2), clean_data(T2_proba2))
plt.plot(T1_matched2, T2_matched2, marker='o', color='orange', label='Proba 2')
plt.title('Wykres T1 vs T2 Proba 2 -  usuwamy Nan')
plt.xlabel('T1_proba2')
plt.ylabel('T2_proba2')
plt.legend()
plt.grid()

# Wykres 3
plt.subplot(1, 3, 3)  # 1 wiersz, 3 kolumny, 3. wykres
T1_matched3, T2_matched3 = match_length(clean_data(T1_proba3), clean_data(T2_proba3))
plt.plot(T1_matched3, T2_matched3, marker='o', color='green', label='Proba 3')
plt.title('Wykres T1 vs T2 Proba 3 -  usuwamy Nan')
plt.xlabel('T1_proba3')
plt.ylabel('T2_proba3')
plt.legend()
plt.grid()

plt.tight_layout()  # Dostosowanie układu wykresów
plt.show()

#Wykresy dla wartosci T - wybrany przedzial 
#draw_sample_value_plot_cast((T1_proba1), 'Zależność T1_proba1 od numeru próbki - usuwamy Nan - Fragment',20,100)
#draw_sample_value_plot_cast((T2_proba1), 'Zależność T2_proba1 od numeru próbki - usuwamy Nan - Fragment',9800,9999)
#draw_sample_value_plot_cast((T1_proba2), 'Zależność T1_proba2 od numeru próbki - usuwamy Nan - Fragment',20,100)
draw_sample_value_plot_cast((T2_proba2), 'Zależność T2_proba2 od numeru próbki - usuwamy Nan - Fragment',9800,9999)
#draw_sample_value_plot_cast((T1_proba3), 'Zależność T1_proba3 od numeru próbki - usuwamy Nan - Fragment',20,100)
#draw_sample_value_plot_cast((T2_proba3), 'Zależność T2_proba3 od numeru próbki - usuwamy Nan - Fragment',20,100)

#Rysowanie histogramow
draw_histogram(T1_proba1, 'Histogram T1_proba1')
draw_histogram(T2_proba1, 'Histogram T2_proba1')
draw_histogram(T1_proba2, 'Histogram T1_proba2')
draw_histogram(T2_proba2, 'Histogram T2_proba2')
draw_histogram(T1_proba3, 'Histogram T1_proba3')
draw_histogram(T2_proba3, 'Histogram T2_proba3')

# Obliczanie odchylenia standardowego dla każdej zmiennej
std_T1_proba1 = T1_proba1.std()
std_T2_proba1 = T2_proba1.std()
std_T1_proba2 = T1_proba2.std()
std_T2_proba2 = T2_proba2.std()
std_T1_proba3 = T1_proba3.std()
std_T2_proba3 = T2_proba3.std()

# Wyświetlenie odchyleń standardowych
print(f"Odchylenie standardowe dla T1_proba1: {std_T1_proba1}")
print(f"Odchylenie standardowe dla T2_proba1: {std_T2_proba1}")
print(f"Odchylenie standardowe dla T1_proba2: {std_T1_proba2}")
print(f"Odchylenie standardowe dla T2_proba2: {std_T2_proba2}")
print(f"Odchylenie standardowe dla T1_proba3: {std_T1_proba3}")
print(f"Odchylenie standardowe dla T2_proba3: {std_T2_proba3}")