
with open('chicken.txt', 'r', encoding="utf-8") as f:
    daily_charge = [charge.strip() for charge in f]
    avarage = 0
    for i in daily_charge:
        avarage += int(i[-6:])
    print(avarage / len(daily_charge))