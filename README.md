# json-search

## Requirements for running
  1. Running application on Mac or Linux
  2. Python3 
  3. json files named with .json as extension

## Output
  * Results are displaying in human readable json format (ie pretty json)

## Assumptions
  * First will search current directory.  If no json files found will prompt user for path to json files
  * Assumes blank value searches are for "null" json values
  * Assumes boolean json fields are compared ignoring case
  * Assumes json list values are searched individually (ie search for key tags and value '1' on 'tags': ['1', '2'] will match as comparisons search value against '1' and then '2')

## Run Instructions
  ```bash
  python3 search.py
  ```

## Run Examples
  ```bash
  python3 search.py
  Welcome to Zendesk Search
  Type 'quit' to exit at any time. Press Enter to continue...

  Select search options:
    1) Search Zendesk
    2) View a list of searchable fields
    Type 'quit' to exit

  1
  Unable to find json files.  Please enter path to json files. Type 'quit' to exit.
  nonexistant_dir
  Unable to find json files.  Please enter path to json files. Type 'quit' to exit.
  temp
  Select from below options:
    1) Organizations
    2) Users
    3) Tickets

  1
  Searching file: temp/organizations.json
  Enter search term:
  _id
  Enter search value:
  126
  Searching Temp/organizations for _id with a value of 126
  {
    "_id": 126,
    "url": "http://initech.zendesk.com/api/v2/organizations/126.json",
    "external_id": "7cd6b8d4-2999-4ff2-8cfd-44d05aabb44e",
    "name": "RetaLive",
    "domain_names": [
      "trollery.com",
      "datagen.com",
      "bluegrain.com",
      "dadabase.com"
    ],
    "created_at": "2016-04-07T08:21:44 -10:00",
    "details": null,
    "shared_tickets": false,
    "tags": [
      "Cherry",
      "Collier",
      "Fuentes",
      "Trevino"
    ]
  }
  ```

## Unit Test Run Instructions
  ```bash
  python3 test_search.py
  ```
### Unit Test Example
 ```bash
  python3 test_search.py
  .......
  ----------------------------------------------------------------------
  Ran 7 tests in 0.001s
  ```