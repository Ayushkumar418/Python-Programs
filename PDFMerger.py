from pypdf import PdfMerger

def marge_pdf(PDFs,output):
    marger = PdfMerger()
    for pdf in PDFs:
        marger.append(pdf)
    with open(output, 'wb') as f:
        marger.write(f)
    
def main():
    PDFs = input("Enter the name of PDFs with path(Space seprates): ").split()
    output = input("Enter the name of output file with path: ")

    marge_pdf(PDFs,output)

if __name__ == "__main__":
    main()
    print("Complete")
