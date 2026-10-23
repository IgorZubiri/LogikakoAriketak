katea = input("Sartu ezazu katea: ")
irakurritakoKatea = []
kontagailua = 0
kontagailuaAux = 0

for i in range(len(katea)):
    for j in range(len(irakurritakoKatea)):
        if irakurritakoKatea[j] == katea[i]:
            kontagailua = 0
            irakurritakoKatea = []
            break
    irakurritakoKatea.append(katea[i])
    kontagailua += 1
    if kontagailua >= kontagailuaAux:
        kontagailuaAux = kontagailua
        
print(kontagailuaAux)