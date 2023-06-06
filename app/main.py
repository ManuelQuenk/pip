import utils
import readcsv
import charts
#! revisar clases de map y lambda


def run():
    data = readcsv.read_csv('data.csv')
    data = list(filter(lambda i: i['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)
    
    country = input('Ingrese el país -> ')
    country = country.title()
    
    
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)
    


if __name__ == '__main__':
    run()