class MyClass:
    def method_1(self) -> None:
        print("Method 1")
        self.__method_2()

    def __method_2(self) -> None:
        print("Method 2")

    def registry(self) -> None:
        print("Start process")
        self.__verify()
        self.__verify_registry()
        self.__insert_data()

    def __verify(self) -> None:
        print("Verifying data")

    def __verify_registry(self) -> None:
        print("Verifying registry")

    def __insert_data(self) -> None:
        print("Inserting in DB")


obj = MyClass()
obj.method_1()
print("\n\n\n")
obj.registry()