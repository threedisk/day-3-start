print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print ("Anda bisa naik ke roller coaster")

  age = int(input("Usia Anda berapa ?"))
  if age < 12:
    bill += 5
  elif age < 18:
    bill += 7
  elif (age >= 45 and age<=55):
    bill = 0
    print ("Anda bisa naik secara Gratis")  
  else:
    bill += 12
  
    
  
  wants_photos = input("Pengen difoto tidak?")
  if wants_photos == "Y":
    bill += 3
    print (f"Total tagihan adalah: {bill}")
  else: 
    print (f"Tagihan Anda ${bill}")
#Else Untuk Tidak Naik karena tinggi
else:
  print ("Tinggi Anda masih kurang, minum Booneto lagi untuk tambah tinggi")