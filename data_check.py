# Importowanie bibliotek
import pandas as pd
import matplotlib.pyplot as plt
from funkcje import check_non_numeric_intervals
# Odczyt danych z pliku Excel
dataframe1 = pd.read_excel('dane.xlsx', sheet_name='A3')

# Przypisanie danych do zmiennych
T1_proba1 = dataframe1.iloc[:, 2]
T2_proba1 = dataframe1.iloc[:, 3]
T1_proba2 = dataframe1.iloc[:, 9]
T2_proba2 = dataframe1.iloc[:, 10]
T1_proba3 = dataframe1.iloc[:, 16]
T2_proba3 = dataframe1.iloc[:, 17]

# Sprawdzenie brakujących i nieliczbowych wartości dla każdej zmiennej
check_non_numeric_intervals(T1_proba1, 'T1_proba1')
check_non_numeric_intervals(T2_proba1, 'T2_proba1')
check_non_numeric_intervals(T1_proba2, 'T1_proba2')
check_non_numeric_intervals(T2_proba2, 'T2_proba2')
check_non_numeric_intervals(T1_proba3, 'T1_proba3')
check_non_numeric_intervals(T2_proba3, 'T2_proba3')


