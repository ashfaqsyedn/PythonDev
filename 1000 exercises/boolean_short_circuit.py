def check_money():
    return money > 100000

def check_salary():
    salary += 1
    return salary >= 1000

while True:
    if check_money() or check_salary():
        print("I can live well")


while True:
    has_good_money = check_money()
    has_good_salary = check_salary()

    if has_good_money or has_good_salary:
        print("I can live well")

if status_code == 401 or 302:
    pass

if status_code == 401 or status_code == 302:
    pass

if status_code in [401, 302]:
    pass


