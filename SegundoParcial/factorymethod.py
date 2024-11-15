from abc import ABC, abstractmethod

# Producto
class Document(ABC):
    @abstractmethod
    def render(self):
        pass

# Producto concreto 1
class PDFDocument(Document):
    def render(self):
        return "Rendering PDF document"

# Producto concreto 2
class WordDocument(Document):
    def render(self):
        return "Rendering Word document"

# Creador abstracto
class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

# Factory concreta 1
class PDFDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PDFDocument()

# Factory concreta 2
class WordDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return WordDocument()

# Cliente que utiliza la fábrica
def client_code(factory: DocumentFactory):
    document = factory.create_document()
    print(document.render())

# Ejemplo de uso
pdf_factory = PDFDocumentFactory()
word_factory = WordDocumentFactory()

client_code(pdf_factory)  # Output: "Rendering PDF document"
client_code(word_factory)  # Output: "Rendering Word document"
