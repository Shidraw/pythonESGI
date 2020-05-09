def exchangeFromString(s):
    order = s[:2]
    amount = s[3:]
    if order == "EA":
        amount = int(amount) * 4168.79
    else:
        amount = int(amount) * 0.00024
    return amount


content = input('Saisissez votre conversion en suivant la norme "EA 8" ou "AE 8" selon le sens : ')

print(exchangeFromString(content))