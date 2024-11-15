from abc import ABC, abstractmethod

class Documento(ABC):
    @abstractmethod
    def generar(self):
        pass

class PDFDocument(Documento):
    def generar(self):
        return "Generando documento PDF"

class FabricaDocumentos(ABC):
    @abstractmethod
    def exportar(self):
        pass

class FabricaPDF(FabricaDocumentos):
    def exportar(self):
        return PDFDocument()
