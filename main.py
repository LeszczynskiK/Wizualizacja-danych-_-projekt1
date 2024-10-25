# import pandas lib as pd
import pandas as pd

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('dane.xlsx')

#przypisanie danych do zmiennych
T1_proba1 = dataframe1.iloc[:, 2] 
T2_proba1 = dataframe1.iloc[:, 3] 

T1_proba2 = dataframe1.iloc[:, 9] 
T2_proba2 = dataframe1.iloc[:, 10] 

T1_proba3 = dataframe1.iloc[:, 16] 
T2_proba3 = dataframe1.iloc[:, 17] 

print("T1_proba1")
print(T1_proba1)
print("\nT2_proba1")
print(T2_proba1)


print("\nT1_proba2")
print(T1_proba2)
print("T\n2_proba2")
print(T2_proba2)


print("\nT1_proba3")
print(T1_proba3)

print("\nT2_proba3")
print(T2_proba3)

print("\nStatystyki danych - dla nienumerycznych zastap ostatnia cyfra:\n")
## Funkcja do zastępowania wartości nie-numerycznych
def fill_with_last_valid(data):
    last_valid = None
    for i in range(len(data)):
        if pd.isnull(data[i]) or not isinstance(data[i], (int, float)):
            data[i] = last_valid  # Ustaw wartość na ostatnią ważną
        else:
            last_valid = data[i]  # Zaktualizuj ostatnią ważną wartość
    return data

# Zastosowanie funkcji do każdej zmiennej
T1_proba1 = fill_with_last_valid(T1_proba1.copy())
T2_proba1 = fill_with_last_valid(T2_proba1.copy())
T1_proba2 = fill_with_last_valid(T1_proba2.copy())
T2_proba2 = fill_with_last_valid(T2_proba2.copy())
T1_proba3 = fill_with_last_valid(T1_proba3.copy())
T2_proba3 = fill_with_last_valid(T2_proba3.copy())

# Funkcja do obliczania statystyk
def calculate_statistics(data):
    mean = data.mean()
    data_range = data.max() - data.min()
    kurtosis = data.kurtosis()
    median = data.median()
    skewness = data.skew()
    #mode = data.mode()
    
    return mean, data_range, kurtosis, median, skewness, #mode

# Obliczanie statystyk dla każdej zmiennej
stats_T1_proba1 = calculate_statistics(T1_proba1)
stats_T2_proba1 = calculate_statistics(T2_proba1)
stats_T1_proba2 = calculate_statistics(T1_proba2)
stats_T2_proba2 = calculate_statistics(T2_proba2)
stats_T1_proba3 = calculate_statistics(T1_proba3)
stats_T2_proba3 = calculate_statistics(T2_proba3)

# Wyświetlenie wyników
stat_names = ["Średnia", "Rozstęp", "Kurtosis", "Mediana", "Skewness", "Wartość modalna", "Posortowane"]
for i, stats in enumerate([stats_T1_proba1, stats_T2_proba1, stats_T1_proba2, stats_T2_proba2, stats_T1_proba3, stats_T2_proba3]):
    print(f"\nStatystyki dla zmiennej {'T1_proba1' if i % 2 == 0 else 'T2_proba1' if i == 1 else 'T1_proba2' if i == 2 else 'T2_proba2' if i == 3 else 'T1_proba3' if i == 4 else 'T2_proba3'}:")
    for name, value in zip(stat_names, stats):
        print(f"{name}: {value.values if isinstance(value, pd.Series) else value}")