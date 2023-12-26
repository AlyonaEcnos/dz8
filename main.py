from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    birthdays_per_week = {}

    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        
        # Создаем новую дату с текущим годом и месяцем/днем из дня рождения
        today = datetime.today().date()
        
        if today > datetime(today.year, birthday.month, birthday.day).date():
            # Если дата рождения уже прошла, меняем год на следующий
            changed_year = datetime(
                today.year + 1, birthday.month, birthday.day
                ).date()
        else:
            # Иначе оставляем текущий год
            changed_year = datetime(
                today.year, birthday.month, birthday.day
                ).date()

        # Переносим на понедельник, если выходной - суббота или воскресенье
        if changed_year.weekday() == 5:  # 5 - суббота
            changed_year += timedelta(days=2)
        elif changed_year.weekday() == 6:  # 6 - воскресенье
            changed_year += timedelta(days=1)

        # Вычисляем разницу во времени до дня рождения
        time_left_until_bd = changed_year - today

        # Получаем количество дней из timedelta
        days_left = time_left_until_bd.days

        if days_left <= 7:
            day_of_week = changed_year.strftime('%A')
            if day_of_week not in birthdays_per_week:
                birthdays_per_week[day_of_week] = [name.split()[0]]
            else:
                birthdays_per_week[day_of_week].append(name.split()[0])
    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Выводим результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
