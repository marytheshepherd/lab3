from employee_info import (
    get_employees_by_age_range,
    calculate_average_salary,
    get_employees_by_dept
)

def test_get_employees_by_age_range():
    result = get_employees_by_age_range(22, 36)
    names = [i["name"] for i in result]
    assert "John" in names
    assert "Chloe" in names
    assert "Peter" not in names 

def test_calculate_average_salary():
    avg_salary = calculate_average_salary()
    expected_avg = round((50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6)
    assert avg_salary == expected_avg

def test_get_employees_by_dept():
    result = get_employees_by_dept("Marketing")
    names = [i["name"] for i in result]
    assert len(result) == 2
    assert names == ["Jane","Mary"]


    result_empty = get_employees_by_dept("Legal")
    assert result_empty == []
