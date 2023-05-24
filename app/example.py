import charts

data = [
    {
    'name': '',
    'age': 27
    },
    {
    'name': '',
    'age': 88
    },
    {
    'name': '',
    'age': 61
    },
    {
    'name': '',
    'age': 45
    },
    {
    'name': '',
    'age': 19
    },
    {
    'name': '',
    'age': 37
    },
    {
    'name': '',
    'age': 66
    },
    {
    'name': '',
    'age': 47
    },
    {
    'name': '',
    'age': 17
    },
    {
    'name': '',
    'age': 42
    },
    {
    'name': '',
    'age': 24
    },
    {
    'name': '',
    'age': 21
    },
    {
    'name': '',
    'age': 20
    },
    {
    'name': '',
    'age': 31
    },
    {
    'name': '',
    'age': 90
    },
    {
    'name': '',
    'age': 31
    },
    {
    'name': '',
    'age': 86
    },
    {
    'name': '',
    'age': 55
    },
    {
    'name': '',
    'age': 12
    },
    {
    'name': '',
    'age': 19
    },
]

def run():

    def ageGap(data):
        teen = 0
        adult = 0
        oldAdults = 0

        for i in data:
            if i['age'] >= 15 and i['age'] <= 20:
                teen += 1
            elif i['age'] >= 21 and i['age'] <= 40:
                adult += 1
            elif i['age']>= 41 and i['age'] <= 120:
                oldAdults += 1
        return teen, adult, oldAdults

    teen, adult, oldAdults = list(ageGap(data))
    print('Amount of teenagers -->',teen,'Amount of Adults -->', adult,'Amount of Old people -->', oldAdults)
    labels = ['Teens', 'Adults', 'Old adults']
    values = [teen, adult, oldAdults]
    # charts.generate_pie_chart(labels, values)
    charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
    run()