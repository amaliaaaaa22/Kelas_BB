# Data panen Maudy Amalia-152023143
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print("Data Hasil Panen Maudy Amalia :\n")
for lokasi, data in data_panen.items():
    print(f"Lokasi : {data['nama_lokasi']}")
    print("Hasil Panen :")
    for tanaman, hasil in data['hasil_panen'].items():
        print(f"{tanaman} : {hasil} kg")
    print()

lokasi2_jagung = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung di lokasi2 : {lokasi2_jagung}\n")

lokasi3_nama = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3 : {lokasi3_nama}\n")

for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    kedelai = data['hasil_panen']['kedelai']
    print(f"Lokasi : {data['nama_lokasi']}")
    print(f"Jumlah Hasil Panen Padi : {padi} kg")
    print(f"Jumlah Hasil Panen Kedelai : {kedelai} kg\n")

total_padi = sum(data['hasil_panen']['padi'] for data in data_panen.values())
total_kedelai = sum(data['hasil_panen']['kedelai'] for data in data_panen.values())
print(f"Total Hasil Panen :")
print(f"Padi : {total_padi} kg")
print(f"Kedelai : {total_kedelai} kg\n")

print("Status Lokasi Panen:")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    
    if padi > 1300 or jagung > 800:
        print(f"Lokasi {data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {data['nama_lokasi']} dalam kondisi baik.")
