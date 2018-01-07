from preprocessing.DataSet import DataSet

if __name__ == "__main__":
    print("Did the thing")
    x = DataSet("Hello", "World")
    print(type(x))
    print(x.__dict__)
