from abc import ABC, abstractmethod


# 1. Interface Base Genérica
class Document(ABC):
    @abstractmethod
    def load(self):
        pass


# 2. Interfaces Específicas (ISP) herdando da Base
class DocumentPDF(Document, ABC):
    @abstractmethod
    def view(self):
        pass


class DocumentTXT(Document, ABC):  # ISP
    @abstractmethod
    def format(self): pass


class DocumentEXCEL(Document, ABC):  # ISP
    @abstractmethod
    def calculate(self): pass


# 3. Implementação Concreta (Herda apenas o necessário)
class PDF(DocumentPDF):
    def load(self):
        print("Loading PDF...")

    def view(self):
        print("Viewing PDF content...")


document_1 = PDF()
document_1.load()
document_1.view()