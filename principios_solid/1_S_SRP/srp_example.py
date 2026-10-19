class Process:
    def handle(self, username: str, password: str) -> None:
        if self.__verify_input_data(username, password):
            self.__verify_input_in_database(username)
            print("cadastro do usuário realizado com sucesso!")
        else:
            raise self.__raise_error("Dados Invalidos")

    def __verify_input_data(self, username: str, password: str) -> bool:
        if isinstance(username, str) and isinstance(password, str):
            return True

        return False

    def __verify_input_in_database(self, username: str) -> None:
        print("Acessando o banco de dados...")
        print("Verificando existencia do usuário...")

    def __insert_new_user(self, username: str, password: str) -> None:
        print("cadastro do usuário realizado com sucesso!")

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)