# My Inventory Allocator (Deliverr)
My submission to Deliverr's recruiting exercise for their "inventory allocator" question. [Link to question](https://github.com/deliverr/recruiting-exercises/tree/master/inventory-allocator)
## Geting Started
### Prerequisites
- python3
## Running the tests
- Tests are located in /test_cases_txt
- To run the tests, run the testcase_runner.py in the command line by entering: ```$ python3 testcase_runner.py```
- Answers to the test cases are put into the created directory /test_case_outputs in .txt format
### Assumptions and Limitations
- The algorithm assumes the first input always exists, but can be empty ```{}```, and that second input has at least this: ```[{ name:"", inventory: {} }]```
- Assumes that there is a whitespace between first and second inputs ```{}, [{name"", inventory:{}}]```
- If ANY part of the order cannot be satisfied, then the order is invalid and an empty bracket is returned
- The code cannot handle items with names only consisting of numbers. It is due to the way the testcase_runner.py parses the input, and converts it into a JSON  format - it has trouble putting the name of the item in quotes if the key name has digits only.
-
## Authors
- Vergil Hsu (AerialKebab)
