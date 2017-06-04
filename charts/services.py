from nutrition.models import Nutrients
from django.utils import timezone
from datetime import timedelta


def chart_service(date, user):
    nutrients = Nutrients.objects.filter(date=date, user_id=user).values(
        'protein', 'carbs', 'fat', 'sugar', 'fiber', 'amount'
    )

    protein_list = []
    carbs_list = []
    fat_list = []
    sugar_list = []
    fiber_list = []

    for item in nutrients:
        p = item['protein']
        c = item['carbs']
        f = item['fat']
        s = item['sugar']
        fi = item['fiber']
        a = item['amount']

        p_amount = (p / 100) * a
        protein_list.append(p_amount)
        c_amount = (c / 100) * a
        carbs_list.append(c_amount)
        f_amount = (f / 100) * a
        fat_list.append(f_amount)
        s_amount = (s / 100) * a
        sugar_list.append(s_amount)
        fi_amount = (fi / 100) * a
        fiber_list.append(fi_amount)

    protein = float("%.2f" % sum(protein_list))
    carbs = float("%.2f" % sum(carbs_list))
    fat = float("%.2f" % sum(fat_list))
    sugar = float("%.2f" % sum(sugar_list))
    fiber = float("%.2f" % sum(fiber_list))

    items = [protein, carbs, fat, sugar, fiber]

    return items


def energy_service(user):

    energy_week_list = []

    days = 6

    while days >= 0:
        day_list = []
        date = timezone.now() - timedelta(days=days)
        energy = Nutrients.objects.filter(date=date, user_id=user).values('energy_kcal')
        p = len(energy) - 1
        while p >= 0:
            t = energy[p]['energy_kcal']
            day_list.append(t)
            p -= 1
            if p == -1:
                energy_week_list.append(sum(day_list))
        days -= 1

    return energy_week_list

