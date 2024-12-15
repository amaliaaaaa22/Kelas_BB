import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None) 
pd.set_option('display.width', 1000) 

data_sampah_jabar = pd.read_csv('data_sampah_jabar.csv')
filtered_data_sampah = pd.DataFrame(data_sampah_jabar.iloc[:, 1:8])  
print(filtered_data_sampah)
print("----------------------------------------------------------------")

total_sampah_tahun_2018 = 0
for index, row in data_sampah_jabar.iterrows():
    if row['Tahun'] == 2018:
        total_sampah_tahun_2018 += row['Jumlah Produksi Sampah']
print(f"Total Sampah Produksi Tahun 2018 : {total_sampah_tahun_2018}")
print("----------------------------------------------------------------")

total_per_tahun = {}
for index, row in data_sampah_jabar.iterrows():
    tahun = row['Tahun']
    jumlah_produksi_sampah = row['Jumlah Produksi Sampah']
    if tahun in total_per_tahun:
        total_per_tahun[tahun] += jumlah_produksi_sampah
    else:
        total_per_tahun[tahun] = jumlah_produksi_sampah
print("Jumlah Data per Tahun:")
for tahun, jumlah in total_per_tahun.items():
    print(f"Tahun {tahun}: {jumlah}")
print("----------------------------------------------------------------")


total_data_per_kota = {}
for index, row in data_sampah_jabar.iterrows():
    kota = row['Nama Kabupaten/Kota']
    total_data_per_kota[kota] = total_data_per_kota.get(kota, 0) + row['Jumlah Produksi Sampah']

print("Jumlah Data per Kabupaten/Kota :")
print(f"{'Kabupaten/Kota':<30} {'Jumlah Produksi Sampah (Ton)'}") 
for kota, jumlah in sorted(total_data_per_kota.items()):
    print(f"{kota:<30} {jumlah:>17.2f}")

filtered_data_sampah.to_csv('datasampahjabar_152023143.csv', index=False)
filtered_data_sampah.to_excel('datasampahjabar_152023143.xlsx', index=False)

