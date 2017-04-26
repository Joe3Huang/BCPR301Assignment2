
def test():
    import doctest
    doctest.testfile("methodPrintAllDataTest.txt", verbose=1)
    doctest.testfile("methodLoadFileTest.txt", verbose=1)
    doctest.testfile("save_file_test.txt", verbose=1)
    doctest.testfile("convert_dict_test.txt", verbose=1)
    doctest.testfile("serialise_object_test.txt", verbose=1)

if __name__ == "__main__":
    test()
