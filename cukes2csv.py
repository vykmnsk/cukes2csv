import json
import csv

def extract_tests(cukes):
    tests = []
    for cuke in cukes:
        steps = []
        for el in cuke['elements']:
            if el['type'] == 'background':
                for step in el['steps']:
                    steps.append(f"{step['keyword']} {step['name']}")
            if el['type'] == 'scenario':
                test = {}
                test[('Summary', 1)] = f"{el['name']}"
                test[('Issue Type', 1)] = 'Test'
                test[('Automate', 1)] = 'Required'
                test[('Labels', 1)] = 'Automated'
                test[('Labels', 2)] = 'Sun_Deadheat_Testcase'

                for step in el['steps']:
                    steps.append(f"{step['keyword']} {step['name']}")
                test[('Description', 1)] = '\n'.join(steps)
                tests.append(test)
                steps = []
    return tests

def write_csv(filename, dicts, delimiter=','):
    with open(filename, 'w') as f:
        w = csv.writer(f, delimiter=delimiter)
        w.writerow(header(dicts))
        for d in dicts:
            w.writerow(d.values())

def header(dicts):
    assert len(dicts) > 0
    headers = [ key[0] for key in dicts[0].keys()]
    return headers

def print_csv(dicts, delimiter=','):
    print(delimiter.join(header(dicts)))
    print('\n') 
    for d in dicts:
        print(delimiter.join(d.values()))
        print('\n') 

def main():
    with open('cucumber.json') as json_data:
        cukes = json.load(json_data)

    tests = extract_tests(cukes) 
    print_csv(tests, ';')
    filename = 'tests.csv'
    write_csv(filename, tests, ';')

    print('Done!')
    print('open ./' + filename)

main()