##############
# Module 8 Homework
##############
import requests
import json


# List the project members
def the_conspirators():
    print('''This project brought to you by: 
    Chris Simiskey
    Varsha Mandadi
    Kristen Sohm    #is here
    ''')

# Function to retrieve data from the API
def get_data():
    print('Retrieving data here')
    request = requests.get('http://api.gbif.org/v1/species')
    json_data = json.loads(request.content)

    # Overwriting the previous file each time this is ran (Not persisting data past a single session)
    with open(r'species.json', 'w', encoding='utf8') as api_file:
        json.dump(json_data, api_file)


# Function to analyze the retrieved data
def inspect_data():
    print('Processing data here')
    with open(r'species.json') as json_file:
        parsed_json_file = json.load(json_file)
        print('Fields of the dataset are:')
        for item in parsed_json_file['results']:
            print(item['kingdom'],
            item['scientificName'], item['canonicalName'])

 # Data size , datatypes,fields
 # Data size- 20 rows
 #
def data_types():
    print('''In the result set of json species these are  the following data types in a single record: 
    
    string-11
    integer-6
    bool-2
    datetime-2
    list-2
    dictionary-1  
    ''')


def data_quality():
    print(''' quality of data is: 
         We think that the data quality is pretty good as per the results and the source
         source:https://www.gbif.org/
        ''')




################
# Run all the things
################

if __name__ == '__main__':
    the_conspirators()
    get_data()
    inspect_data()
    data_types()
    data_quality()
