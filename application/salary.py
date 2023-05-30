import random
def calculate_salary(workers):
    for w in workers:
        z = random.randint(5000, 30000)
        if z < 10000:
            zp = f"{z} (ни в чем себе не отказывайте)))"
        else:
            zp = f"{z}"
        print(f"Зарплата для {w} начислена! {zp} руб.")