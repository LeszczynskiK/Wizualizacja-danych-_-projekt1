# Importowanie bibliotek
import pandas as pd
import matplotlib.pyplot as plt
from funkcje import clean_data, draw_sample_value_plot, calculate_statistics, match_length, fill_with_last_valid, draw_sample_value_plot_cast

# Odczyt danych z pliku Excel
dataframe1 = pd.read_excel('dane.xlsx', sheet_name='A3')

# Przypisanie danych do zmiennych
T1_proba1 = dataframe1.iloc[:, 2]
T2_proba1 = dataframe1.iloc[:, 3]
T1_proba2 = dataframe1.iloc[:, 9]
T2_proba2 = dataframe1.iloc[:, 10]
T1_proba3 = dataframe1.iloc[:, 16]
T2_proba3 = dataframe1.iloc[:, 17]