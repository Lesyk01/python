from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Report(Document):
    def __init__(self, title: str = "Monthly Report") -> None:
        self.title = title
    
    def render(self) -> str:
        return f"--- ZVIT ({self.title}) ---\nMeta: Data Analysis.\nStatus: Ready to print."

class Invoice(Document):
    def __init__(self, number: int = 1001) -> None:
        self.number = number

    def render(self) -> str:
        return f"--- INVOICE №{self.number} ---\nAmount: 1500.00 UAH\nStatus: Payable."

class Contract(Document):
    def __init__(self, party: str = "LLC 'Partner'") -> None:
        self.party = party

    def render(self) -> str:
    
        return f"--- CONTRACT ---\nParty: {self.party}\nSubject: Service Provision\nSigned."



class DocumentFactory:

    
    _document_types = {
        'report': Report,
        'invoice': Invoice,
        'contract': Contract,
    }

    @staticmethod
    def create(doc_type: str, **kwargs) -> Document:
        doc_type_lower = doc_type.lower()
        
        if doc_type_lower not in DocumentFactory._document_types:
            raise ValueError(f"Unknown document type: '{doc_type}'. Allowed types: {', '.join(DocumentFactory._document_types.keys())}")
        

        DocumentClass = DocumentFactory._document_types[doc_type_lower]
        return DocumentClass(**kwargs)
def process_document(doc_type_str: str, **kwargs) -> None:
    print(f"\nAttempting to create: '{doc_type_str}'")
    try:
  
        document: Document = DocumentFactory.create(doc_type_str, **kwargs)
        
    
        print("--- Document Rendering ---")
        print(document.render())
        print("--------------------------")
        
    except ValueError as e:
        print(f"!!! ERROR: {e}")


process_document('report', title="Quarterly Report Q3")
process_document('invoice', number=452)
process_document('contract', party="Sole Proprietor 'Ivanov'")
process_document('memo')




# Шаблони — це перевірені схеми для вирішення типових проблем,
# які постійно виникають у розробці.
# Це як готові інструкції щоб зрозуміти як правильно організувати код,
# щоб він був зрозумілий, зручний і легко змінювався.



# метод create у DocumentFactory є статичним, тому що для того, щоб створити новий документ,
# вам не потрібно мати екземпляр самої фабрики (DocumentFactory).
# Метод просто бере вхідні дані і повертає результат
# не використовуючи жодних унікальних даних об'єкта DocumentFactory.


# абстрактний клас (використовує ABC — Abstract Base Class).
# Він визначає, що кожен документ мусить мати метод render().


