from datetime import datetime

from application.people import *
from application.salary import *

if __name__ == '__main__':
    print('Добро пожаловать в модуль "Бухгалтерия".')
    print(f'Сегодня {datetime.now().strftime("%m.%d.%Y, %H:%M:%S")}. Давайте рассчитаем зарплату :))')
    workers = get_employees()
    calculate_salary(workers)
