import json
import csv

def extract_tests(cukes):
    tests = []
    for cuke in cukes:
        for el in cuke['elements']:
            if el['type'] == 'scenario':
                test = {}
                test['Summary'] = f"{el['name']}"
                test['Assignee'] = 'Yuri'
                test['Test Type'] = 'Automatic'
                steps = []
                for step in el['steps']:
                    steps.append(f"{step['keyword']} {step['name']}")
                test['Description'] = '\n'.join(steps)
                tests.append(test)
    return tests

def write_csv(dicts, delimiter=','):
    with open('tests.csv', 'w') as f:
        w = csv.writer(f, delimiter=delimiter)
        w.writerow(header(dicts))
        for d in dicts:
            w.writerow(d.values())

def header(dicts):
    assert len(dicts) > 0
    return dicts[0].keys()

def print_csv(dicts, delimiter=','):
    print(delimiter.join(header(dicts)))

    for d in dicts:
        print(delimiter.join(d.values()))
        print('\n') 

def main():
    with open('cucumber.json') as json_data:
        cukes = json.load(json_data)

    tests = extract_tests(cukes) 
    print_csv(tests, ';')
    write_csv(tests, ';')


main()