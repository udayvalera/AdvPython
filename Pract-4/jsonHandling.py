import os
import json


def readJson(datadir):
    countries = []
    for root, _, files in os.walk(getcwd):
        for file in files:
            if file.endswith('.json') and file != 'covid19_summary.json':
                with open(os.path.join(root, file), 'r') as f:
                    data = json.load(f)
                    countries.append(data)
    return countries

def statisticsJson(countries):
    country_stats = []
    for country in countries:
        # print(country['country'])
        # print(country['data'][0]['date'])
        # print(country['data'][0]['confirmed_cases']['total'])
        # print(country['data'][0]['deaths']['total'])
        # print(country['data'][0]['recovered']['total'])
        country_name = country['country']
        avg_confirmed_cases = 0
        avg_deaths = 0
        avg_recovered = 0
        max_cases = 0
        for i in range(0, len(country['data'])):
            avg_confirmed_cases += country['data'][i]['confirmed_cases']['total']
            avg_deaths += country['data'][i]['deaths']['total']
            avg_recovered += country['data'][i]['recovered']['total']
            if country['data'][i]['confirmed_cases']['total'] > max_cases:
                max_cases = country['data'][i]['confirmed_cases']['total']
                max_cases_date = country['data'][i]['date']

        avg_confirmed_cases = avg_confirmed_cases / len(country['data'])
        avg_deaths = avg_deaths / len(country['data'])
        avg_recovered = avg_recovered / len(country['data'])
        
        
        country_stats.append({
            'country': country_name,
            'confirmed_cases': avg_confirmed_cases,
            'deaths': avg_deaths,
            'recovered': avg_recovered,
            'max_cases': max_cases,
            'max_date': max_cases_date
        })
    return country_stats

def countries_ranking(country_ranking):
    country_ranking.sort(key=lambda x: x['confirmed_cases'], reverse=True)
    return country_ranking[:5],country_ranking[-5:]

def summary_report(datadir):
    countries = readJson(datadir)
    stats = statisticsJson(countries)
    top5, bottom5 = countries_ranking(stats)

    #Write the report to a summary json file
    with open('covid19_summary.json', 'w') as f:
        json.dump(stats, f, indent=4)


if __name__ == "__main__":
    getcwd = os.getcwd()
    datadir = os.path.join(getcwd, "data")
    stats = statisticsJson(readJson(datadir))

    while True:
        userInput = input("Enter the country name to get the statistics (or type 'exit' to quit): ")
        if userInput.lower() == 'exit':
            break
        country_stat = next((item for item in stats if item['country'].lower() == userInput.lower()), None)
        if country_stat:
            print(f"Statistics for {country_stat['country']}:")
            print(f"  Confirmed Cases: {country_stat['confirmed_cases']}")
            print(f"  Deaths: {country_stat['deaths']}")
            print(f"  Recovered: {country_stat['recovered']}")
            print(f"  Max Cases: {country_stat['max_cases']} on {country_stat['max_date']}")
        else:
            print("Country not found. Please try again.")