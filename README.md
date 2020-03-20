# json-search

## Requirements for running
  1. Python3 
  2. json files in directory execting out of

## Run Instructions
  ```bash
  python3 search.py
  ```
## Unit Test Run Instructions
  ```bash
  python3 test_search.py
  ```

## Notes
  * Assumes blank value searches are for "null" json values
  * Assumes boolean json values are compared ignoring case
  * Assumes json list values are searched individually (ie search for tags on 'tags': ['1', '2'] will compare search value against '1' and then '2')