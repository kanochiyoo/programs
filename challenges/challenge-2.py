"""
Perhatikan kode di bawah ini:
Terdapat dua variabel yaitu adalah job dan age, tugasmu adalah membuat sebuah variabel baru
yang bernama isEligible dengan kondisi pekerjaan harus Student dan umur lebih besar dari 21.
"""

job = "Student"
age = 25
isEligible = job == "Student" and age > 21
print(isEligible)