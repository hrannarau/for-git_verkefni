#Git Verkefni   Dags. 24.1.2017
#Hrannar Helgi Auðunsson

#Dæmi 1
print("Dæmi 1")
tala1 = int(input("Sláðu inn eina tölu "))
tala2 = int(input("Sláðu inn aðra tölu "))
margf = tala1*tala2
lagdar = tala1+tala2
print("Tölurnar lagðar saman:",lagdar)
print("Tölurnar margfaldaðar saman:",margf)

#Dæmi 2
print("Dæmi 2")
fornafn = input("Sláðu inn fornafnið þitt ")
eftirnafn = input("Sláðu inn eftirnafnið þitt ")
print("Halló",fornafn,eftirnafn)

#Dæmi 3
print("Dæmi 3")
texti = input("Sláðu inn einn streng ")
hastafir = 0
lagstafir = 0
lagHa = 0
for i in range(len(texti)):
    if texti[i].isupper():
        hastafir = hastafir+1
        if texti[i + 1].islower():
            lagHa = lagHa + 1
    elif texti[i].islower():
        lagstafir = lagstafir+1
print(hastafir,"hástafir,",lagstafir,"lágstafir,",lagHa,"lágstafir koma beint eftir hástaf")
