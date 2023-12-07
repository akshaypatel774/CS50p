months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def get_date():
    while True:
        try:
            date = input('Date: ')
            new_date = date.replace('/', ' ').replace(',', ' ')
            m, d, y = new_date.split()
            if m.capitalize() in months and 0<int(d)<=31 and '/' not in date and ',' in date:
                return months.index(m)+1, d, y
            elif 0<int(m)<=12 and 0<int(d)<=31 and ',' not in date:
                return m, d, y
            else:
                continue
        except (KeyError,ValueError):
            continue

m,d,y = get_date()
print(f'{y:04}-{int(m):02}-{int(d):02}')