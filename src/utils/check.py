import math


def check(amount: int = 7, interval: int = 5):
    allowed_amount = math.ceil(59 / (interval + 1))

    if amount > allowed_amount:
        print('хуй тоби')
        # измените кол-во уведомлений в час или установите другой период между ними
    else:
        pass
