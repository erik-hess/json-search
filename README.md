# json-search

## Requirements for running
  1. Python3 
  2. json files are in the current directory executing out of, and are name with .json as extension
  
## Output
  * Results are displaying in human readable json format (ie pretty json)

## Run Instructions
  ```bash
  python3 search.py
  ```
## Unit Test Run Instructions
  ```bash
  python3 test_search.py
  ```

## Assumptions
  * Assumes blank value searches are for "null" json values
  * Assumes boolean json fields are compared ignoring case
  * Assumes json list values are searched individually (ie search for key tags and value '1' on 'tags': ['1', '2'] will match as comparisons search value against '1' and then '2')
