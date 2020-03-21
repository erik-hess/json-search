import sys
import glob
import json
import ntpath

def search_zendesk():
    filelist = get_filelist()

    # Display list of json files found in file list and prompt user to select one of them
    input_value = None
    while True:
        try:
            print("Select from below options:")
            for file in filelist:
                index = filelist.index(file) + 1
                print("\t" + str(index) + ") " + (ntpath.basename(file)).capitalize().replace(".json", ""))
    
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

    search_results = search_json(jdata, search_term, search_value)

    if (len(search_results) == 0):
        print("No results found")
    else:
        for entry in search_results:
            print_json_results(entry)

def search_json(json_data, term, value):
    results = []
    for entry in json_data:
        if (term in entry):
            # Need to handle special cases as python json alters boolean values (true/falase) to (True/False)
            if (type(entry[term]) == bool):
                if (str(value).lower() == str(entry[term]).lower()):
                    results.append(entry)
            elif (str(value) == str(entry[term])):
                results.append(entry)
            # Need to handle special cases as python json alters null values None
            # Handle blank search values as well as searches for null value
            elif (not value or value == "null"):
                if ("None" == str(entry[term])):
                    results.append(entry)
            elif (type(entry[term]) == list):
                if (str(value) in entry[term]):
                    results.append(entry)
    
    return results

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
    # Return list of all json files in current directory if not found prompt user for path. 
    # Either absolute or relative will work
    filelist = glob.glob("*.json")
    while (len(filelist) == 0):
        filepath = get_input("Unable to find json files.  Please enter path to json files. Type 'quit' to exit.")
        if (not filepath.endswith('/')):
            filepath = filepath + '/'
        filelist = glob.glob(filepath + "*.json")
    
    return filelist
    
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