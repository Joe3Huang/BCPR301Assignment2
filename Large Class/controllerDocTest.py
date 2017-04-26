
def test():
    import doctest
    doctest.testfile("methodPrintAllDataTest.txt", verbose=1)
    doctest.testfile("methodLoadFileTest.txt", verbose=1)
    doctest.testfile("save_file_test.txt", verbose=1)
    doctest.testfile("convert_dict_test.txt", verbose=1)
    doctest.testfile("serialise_object_test.txt", verbose=1)
    doctest.testfile("pickle_load_test.txt", verbose=1)
    doctest.testfile("display_bar_test.txt", verbose=1)
    doctest.testfile("db_save_test.txt", verbose=1)
    doctest.testfile("db_load_test.txt", verbose=1)
    doctest.testfile("input_age_test.txt", verbose=1)
    doctest.testfile("input_employee_id_test.txt", verbose=1)
    doctest.testfile("input_sales_test.txt", verbose=1)
    doctest.testfile("input_BMI.txt", verbose=1)
    doctest.testfile("input_salary_test.txt", verbose=1)
    doctest.testfile("input_birthday_test.txt", verbose=1)
if __name__ == "__main__":
    test()
