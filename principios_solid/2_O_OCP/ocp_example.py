class Programmer:
    def make(self):
        print("Programmer creating code")


class Seller:
    def make(self):
        print("Seller selling the product")


class HumanResources:
    def make(self):
        print("Human Resources hiring new devs")


class Company:
    def do_work(self, worker: any):
        worker.make()


programmer = Programmer()
seller = Seller()
human_resources = HumanResources()
company = Company()

company.do_work(programmer)
company.do_work(seller)
company.do_work(human_resources)