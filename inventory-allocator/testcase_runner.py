import os
import contextlib
# import json
import re
from inventory_allocator import inventoryAllocator

# getJSONFormFromInput() takes in the input from the corresponding .txt file,
# parses it to get the two inputs, and puts it into a JSON format so that the
# organization and processing of the data can occur.
#
# input: string of both inputs 1 and 2, separated by a comma. Note: THIS FUNCTION
# ASSUMES THAT ALL INPUTS ARE FORMATTED CORRECTLY
#
# output: a list of two elements, inputs 1 and 2. They are formatted correctly
# in JSON format.
def getJSONFormFromInput(content):
    jsonForms = []

    input1 = content.split("}, ",1)[0] + "}" #input 1
    regex = r'\w+'

    needQuotes = list(dict.fromkeys(re.findall(regex,input1))) #find all words/ints in input, then remove duplicates
    for keys in needQuotes: #keys that need to have quotes to be json-parseable
        if not keys.isnumeric(): #if item doesn't only contain digits
            keyRegex = r"\b" + re.escape(keys) + r"\b" #making sure the string isn't part of another substring
            input1 = re.sub(keyRegex,"\"" + keys + "\"",input1)
    jsonForms.append(input1)


    input2 = content.split("}, ",1)[1].replace('\n','')
    needQuotes=needQuotes = list(dict.fromkeys(re.findall(regex,input2)))
    for keys in needQuotes:
        if not keys.isnumeric(): #if item doesn't only contain digits
            keyRegex = r"\b" + re.escape(keys) + r"\b"
            input2 = re.sub(keyRegex,"\"" + keys + "\"",input2)
    jsonForms.append(input2)

    return jsonForms

# main()
# 1. creates path ./test_case_ouputs/ for output redirection
# 2. loops through all files in test_cases, with each iteration:
#       A. opens a file in test_cases
#       B. loads all the JSON content into the variable "data"
#       C. creates the class inventoryAllocator (from inventory_allocator.py)
#          with corresponding data
#       D. processes the data
#       E. runs the algorithm to produce the cheapest shipment
def main():
    if not os.path.exists("./test_case_outputs/"):
        os.mkdir("./test_case_outputs/")
    print("-------------------------------")

    for x in os.listdir("./test_cases_txt/"): #for each test case
        print(">> RUNNING " + x)

        file = open("./test_cases_txt/" + x, "r")
        content = file.read()

        inputs = getJSONFormFromInput(content)

        case = inventoryAllocator(inputs[0], inputs[1])
        case.processInventory()

        # catch stdout of case.produceCheapestShipment and put into corresponding
        # output file in ./test_case_outputs
        with open('./test_case_outputs/' + os.path.splitext(x)[0] + '_output.txt', 'w') as output:
            with contextlib.redirect_stdout(output):
                case.produceCheapestShipment()

        print("-------------------------------")

# execute main
if __name__ == "__main__":
    main()
