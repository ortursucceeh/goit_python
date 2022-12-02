from datetime import datetime, timedelta

week_days = {"Monday": [], "Tuesday": [],
             "Wednesday": [], "Thursday": [], "Friday": []}

pattern = "%Y.%m.%d"


def get_birthdays_per_week(users):
    for user in users:
        name, birthday = user["name"], user["birthday"].strftime("%m.%d")
        for date in [(datetime.today() + timedelta(days=i)).strftime(pattern)
                     for i in range(1, 8)]:
            if birthday in date:
                date = datetime.strptime(date, pattern)
                if date.isoweekday() <= 5:
                    week_days[date.strftime("%A")].append(name)
                else:
                    week_days["Monday"].append(name)

    for key, value in week_days.items():
        if value:
            print(f"{key}: {', '.join(value)}")
