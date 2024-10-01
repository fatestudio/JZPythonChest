if __name__ == '__main__':
    from jsonpath_ng import parse

    # Sample JSON data
    data = {
        "employees": [{
            "id": 1,
            "name": "Alice",
            "department": "HR",
            "salary": 5000
        }, {
            "id": 2,
            "name": "Bob",
            "department": "Engineering",
            "salary": 7000
        }, {
            "id": 3,
            "name": "Charlie",
            "department": "Engineering",
            "salary": 6000
        }, {
            "id": 4,
            "name": "Diana",
            "department": "Finance",
            "salary": 8000
        }]
    }

    # JSONPath expression to extract all employee names
    jsonpath_expr = parse('$.employees[*].name')

    # Extract and print employee names
    employee_names = [match.value for match in jsonpath_expr.find(data)]
    print("Employee Names:", employee_names)
