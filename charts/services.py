from nutrition.models import Nutrients


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

