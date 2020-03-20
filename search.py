import sys
import glob
import json
from pprint import pprint
# json_data=open('bookmarks.json')
# jdata = json.load(json_data)
# pprint (jdata)
# json_data.close()


# jdata = json.load('{"uri": "http:", "foo", "bar"}')
# >>> 'uri' in jdata       # Check if 'uri' is in jdata's keys
# True
# >>> jdata['uri']

def search_zendesk():
    filelist = get_filelist()

    input_value = None
    while True:
        try:
            print("Select from below options:")
            for file in filelist:
                index = filelist.index(file) + 1
                print("\t" + str(index) + ") " + file.capitalize().replace(".json", ""))
    
            input_value = int(get_input(""))
            if (input_value > 0 and input_value <= len(filelist)):
                break
            else:
                print("Invalid selection.  Please try again.")
        except ValueError:
            print("Invalid selection.  Please try again.")

    file_index = input_value - 1
    print("Searching file: " + filelist[file_index])

    json_data=open(filelist[file_index])
    jdata = json.load(json_data)

    search_term = get_input("Enter search term:")
    search_value = get_input("Enter search value:")

    print("Searching " + filelist[file_index].capitalize().replace(".json", "") + " for " + search_term + " with a value of " + search_value)

    search_json(jdata, search_term, search_value)

def search_json(json_data, term, value):
    found_results = False
    for entry in json_data:
        if (term in entry):
            if (str(value) == str(entry[term])):
                print_json_results(entry)
                found_results = True
            elif (not value):
                if ("None" == str(entry[term])):
                    print_json_results(entry)
                    found_results = True
        else:
            print("Invalid key entered.  Please select a valid key value.")
            sys.exit()
    
    if (not found_results):
        print("No results found")

def view_searchable_fields():
    filelist = get_filelist()
    for file in filelist:
        print("-----------------------------------")
        print("Search "+ file.capitalize().replace(".json", "") + " with")
        list_json_keys(file)
        print()

def list_json_keys(filename):
    json_data=open(filename)
    jdata = json.load(json_data)

    unique_list = [] 
    for entry in jdata:
        # traverse all json elements 
        for x in entry.keys(): 
            # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x) 
    
    # print unique list 
    for x in unique_list: 
        print(x)

def get_filelist():
    # Return list of all json files in current directory
    return glob.glob("*.json")

def main_options():
    print("Select search options:")
    print("\t1) Search Zendesk")
    print("\t2) View a list of searchable fields")
    print("\tType 'quit' to exit")
    return int(get_input(""))    

def print_json_results(entry):
    json_formatted_str = json.dumps(entry, indent=2)
    print(json_formatted_str)

def get_input(msg):
    # Standardized method for getting user input and checking for exit condition
    value=input(msg + "\n")

    if (value.lower() == "quit"):
        sys.exit()

    return value.strip()

def main():
    print("Welcome to Zendesk Search")
    get_input("Type 'quit' to exit at any time. Press Enter to continue...")

    # Prompt user for application options
    val = None
    while True:
        try:
            val = main_options()
            if (val == 1 or val == 2):
                break
            else:
                print("Invalid selection.  Please try again.")
        except ValueError:
            print("Invalid selection.  Please try again.")

    if (val == 1):
        search_zendesk()
    elif (val == 2):
        view_searchable_fields()

if __name__ == '__main__':
    main()