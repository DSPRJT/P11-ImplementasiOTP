def konversiascii(input_string) :
    ascii_values= []
    for char in input_string :
        ascii_value = ord(char)
        ascii_values.append(ascii_value)
    return ascii_values

def konversiasci1(input_key) :
    ascii_values= []
    for char in input_key :
        ascii_value = ord(char)
        ascii_values.append(ascii_value)
    return ascii_values

def konversibiner1(input_string):
    binary_values= []
    for char in input_string:
        binary_value = bin(char)[2:]
        binary_values.append(binary_value)
    return binary_values

def konversibiner2(input_key):
    binary_values= []
    for char in input_key:
        binary_value = bin(char)[2:]
        binary_values.append(binary_value)
    return binary_values

def xor_biner(binerPlainteks, binerKey) :
    num1 = int(binerPlainteks, 2)
    num2 = int(binerKey, 2)
    result = num1 ^ num2
    result_biner = bin(result)[2:]
    return result_biner

def binerDesimal(biner):
    return int(biner, 2)

def kodeAscii(asciiCode):
    return chr(asciiCode)

input_string = input("Masukan Plainteks : ")
input_key = input("Masukan Key : ")
hasil1 = konversiascii(input_string)
hasil2 = konversiasci1(input_key)
print("Nilai Ascii Dari Plainteks : ", hasil1)
print("Nilai Ascii Dari Key : ", hasil2)

biner1= konversibiner1(hasil1)
biner2= konversibiner2(hasil2)

print("Hasil Biner dari Plainteks : ", biner1)
print("Hasil Biner dari Key : ", biner2)

print("########################-PROSES ENCRYPTE-#################################")
# HURUF 1
print("")
print("HURUF 1")
hasilXor = xor_biner(biner1[0], biner2[0])
print( f"Berikut Hasil Perbandiangan Dari {biner1[0]} dan {biner2[0]} adalah :",hasilXor)
hasilDesimal = binerDesimal(hasilXor)
print (f"Berikut Hasil Desimal dari {hasilXor} adalah : ",hasilDesimal)
hasilEncrypte = kodeAscii(hasilDesimal)
print("Hasil Encrypte Dari Huruf ke 1 : ", hasilEncrypte)

# HURUF 2
print("")
print("HURUF 2")
hasilXor1 = xor_biner(biner1[1], biner2[1])
print(f"Berikut Hasil Perbandiangan Dari {biner1[1]} dan {biner2[1]} adalah :", hasilXor1)
hasilDesimal1 = binerDesimal(hasilXor1)
print (f"Berikut Hasil Desimal dari {hasilXor1} adalah : ",hasilDesimal1)
hasilEncrypte1 = kodeAscii(hasilDesimal1)
print("Hasil Encrypte Dari Huruf ke 2 : ", hasilEncrypte1)

# HURUF 3
print("")
print("HURUF 3")
hasilXor2 = xor_biner(biner1[2], biner2[2])
print(f"Berikut Hasil Perbandiangan Dari {biner1[2]} dan {biner2[2]} adalah :",hasilXor2)
hasilDesimal2 = binerDesimal(hasilXor2)
print (f"Berikut Hasil Desimal dari {hasilXor2} adalah : ",hasilDesimal2)
hasilEncrypte2 = kodeAscii(hasilDesimal2)
print("Hasil Encrypte Dari Huruf ke 3 : ", hasilEncrypte2)

# HURUF 4
print("")
print("HURUF 4")
hasilXor3 = xor_biner(biner1[3], biner2[3])
print(f"Berikut Hasil Perbandiangan Dari {biner1[3]} dan {biner2[3]} adalah :",hasilXor3)
hasilDesimal3 = binerDesimal(hasilXor3)
print (f"Berikut Hasil Desimal dari {hasilXor3} adalah : ",hasilDesimal3)
hasilEncrypte3 = kodeAscii(hasilDesimal3)
print("Hasil Encrypte Dari Huruf ke 4 : ",hasilEncrypte3)

# HURUF 5
print("")
print("HURUF 5")
hasilXor4 = xor_biner(biner1[4], biner2[4])
print(f"Berikut Hasil Perbandiangan Dari {biner1[4]} dan {biner2[4]} adalah :",hasilXor4)
hasilDesimal4 = binerDesimal(hasilXor4)
print (f"Berikut Hasil Desimal dari {hasilXor4} adalah : ",hasilDesimal4)
hasilEncrypte4 = kodeAscii(hasilDesimal4)
print("Hasil Encrypte Dari Huruf ke 5 : ",hasilEncrypte4)

print("")   
print ("Berikut Hasil Encryptnya : ", hasilEncrypte + hasilEncrypte1 + hasilEncrypte2 + hasilEncrypte3 + hasilEncrypte4)
