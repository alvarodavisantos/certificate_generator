import aspose.pdf as pdf
import pandas as pd

def PDFGenerator(name):
    #name = "Álvaro Davi Santos"

    certificatePDF = pdf.Document("./certificado.pdf")

    nameAbsorber = pdf.text.TextFragmentAbsorber("[NOME_ALUNO]")

    certificatePDF.pages.accept(nameAbsorber)

    textFragmentCollection = nameAbsorber.text_fragments

    for txtFragment in textFragmentCollection:
        txtFragment.text = name

    certificatePDF.save("./certificados/"+name+".pdf")

XLSXFile = "./nomes.xlsx"

df = pd.read_excel(XLSXFile)

for name in df["NOMES"]:
    PDFGenerator(name)