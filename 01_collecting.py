import pandas as pd

# Baca file CSV
df = pd.read_csv("data_penduduk.csv")

# Info dataset
print("Jumlah baris:", len(df))
print("Jumlah kolom:", len(df.columns))
print("\nLima baris awal:")
print(df.head())
print("\nInfo dataset:")
print(df.info())

# Simpan ulang sebagai raw_data.csv
df.to_csv("raw_data.csv", index=False)
print("\nFile disimpan sebagai raw_data.csv")
