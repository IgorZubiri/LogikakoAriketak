def kateak(katea):
    kateaGordetzen = []
    for i in range(len(katea)):
        if katea[i] == '}':
            azkenKarakterea = kateaGordetzen.pop()
            if azkenKarakterea != '{':
                return False
        elif katea[i] == ')':
            azkenKarakterea = kateaGordetzen.pop()
            if azkenKarakterea != '(':
                return False
        elif katea[i] == ']':
            azkenKarakterea = kateaGordetzen.pop()
            if azkenKarakterea != '[':
                return False
        else:
            kateaGordetzen.append(katea[i])

    if len(kateaGordetzen) > 0:
        return False
    else:
        return True

katea = input("Sartu ezazu katea: ")
emaitza = kateak(katea)
print(emaitza)
