# Plan

1. Padaryti dashbordus su filtrais, kur galima bus naudoti bet kuriuos duomenys ir lyginti skellam dist su faktu
2. Atskiras visas skaičiavimo modulis
3. Atskiras vizualizacijos modulis į kurį galima būtų idėti bet kuri data modelį
4. Atskiras koeficientų skaičiavimo modulis (gome adv, elo rating, xG itd...)
Tai yra tik testų ir analitikos modelis skirtas surasti geriausius parametrus ir skaičiavimus. Turi būti dinaminis, kad bet kada galima 
būtų testuoti, pakeisti ir patikrinti kaip savę parodys
5. Padaryti basic simulacinį modelį (Ne monte carlo)

Vizualizacijos:

1. Dashborad
1.1. Skellam, vidurkis ir faktas pagal tiksl rez. (su 0 inflation ir be)
1.2. Skellam, vidurkis ir faktas pagal win, draw, losse, over, under, btts (ateityje ir handicap)
1.3. Skellam, vidurkis ir faktas pagal bendrus kiekius

2. Dashboard
2.1. ELO rating pokytis
2.2. Elo rating koreliacija

3. Dashboard 
3.1. Form įtaka
3.2. Home adv įtaka
3.3. Motivacijos koeficientas (kai teamsas žaidžia dėl iškritimo arba dėl pakilimo)
