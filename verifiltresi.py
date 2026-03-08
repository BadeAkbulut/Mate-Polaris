veriler = [
    87,
    "algoritma",
    {"isim": "Alexandros", "yas": 28},
    {"isim": "Beatrice", "yas": 19},
    {"isim": "Anastasia", "yas": 17},
    ("rastgele", 55),
    {"isim": "Maximilian", "yas": 34},
    ["liste", 12],
    {"isim": "Aurelian", "yas": 21},
    {"isim": "Constantine", "yas": 18},
    3.1415,
    {"isim": "Valentina", "yas": 26},
    {"isim": "Aurelius", "yas": 20},
    {"isim": "Isabella", "yas": 31}
]

sonuc = [kisi for kisi in veriler if isinstance(kisi, dict) and (kisi["yas"] > 20 or kisi["isim"].startswith("A"))]

print(sonuc)