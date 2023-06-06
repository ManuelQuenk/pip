import utils
import readcsv
import charts
import pandas as pd
#! revisar clases de map y lambda


def run():
    '''

    data = list(filter(lambda i: i['Continent'] == 'South America', data)) #* c
    countries = list(map(lambda x: x['Country/Territory'], data)) #* a
    percentages = list(map(lambda x: x['World Population Percentage'], data)) #* b
    
    '''

    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'Africa'] #* c

    countries = df['Country/Territory'].values #* a
    percentages = df['World Population Percentage'].values #* b

    charts.generate_pie_chart(countries, percentages)

    data = readcsv.read_csv('data.csv')
    country = input('Ingrese el país -> ')
    country = country.title()
    
    
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)
    


if __name__ == '__main__':
    run()
