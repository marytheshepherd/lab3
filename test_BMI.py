import bmi.idontlikethis as test

def test_bmi_normal_weight():
    weight = 50
    height = 1.64
    bmi =  weight / (height ** 2)

    result = test.classify_bmi(bmi)

    assert (result == 0)

def test_bmi_over_weight():
    weight = 50
    height = 1.64
    bmi =  weight / (height ** 2)

    result = test.classify_bmi(bmi)

    assert (result == 1)

def test_bmi_under_weight():
    weight = 50
    height = 1.64
    bmi =  weight / (height ** 2)

    result = test.classify_bmi(bmi)

    assert (result == 1)
