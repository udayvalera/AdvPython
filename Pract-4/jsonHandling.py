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
        country_name = country['country']
        total_confirmed_cases = 0
        total_deaths = 0
        total_recovered = 0
        for i in range(0, len(country['data'])):
            total_confirmed_cases += country['data'][i]['confirmed_cases']['total']
            total_deaths += country['data'][i]['deaths']['total']
            total_recovered += country['data'][i]['recovered']['total']
        
        
        country_stats.append({
            'country': country_name,
            'confirmed_cases': total_confirmed_cases,
            'deaths': total_deaths,
            'recovered': total_recovered,
            'active_cases': total_confirmed_cases - total_deaths - total_recovered
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
    top5, bottom5 = countries_ranking(stats)
    summary_report(datadir)
    print("Top 5 Countries:")
    for i in top5:
        print(f"  {i['country']} - {i['confirmed_cases']} cases")
    print("Bottom 5 Countries:")
    for i in bottom5:
        print(f"  {i['country']} - {i['confirmed_cases']} cases")

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
            # print(f"  Max Cases: {country_stat['max_cases']} on {country_stat['max_date']}")
        else:
            print("Country not found. Please try again.")