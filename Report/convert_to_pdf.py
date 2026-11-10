import os
import win32com.client

def convert_docx_to_pdf(docx_path, pdf_path):
    abs_docx = os.path.abspath(docx_path)
    abs_pdf = os.path.abspath(pdf_path)

    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    try:
        doc = word.Documents.Open(abs_docx)
        # wdFormatPDF = 17
        doc.SaveAs(abs_pdf, FileFormat=17)
        doc.Close()
        print(f"Successfully converted {docx_path} -> {pdf_path}")
    finally:
        word.Quit()

if __name__ == "__main__":
    convert_docx_to_pdf("Submission/Group_AI_28_Report.docx", "Submission/Group_AI_28_Report.pdf")
    convert_docx_to_pdf("Submission/Group_AI_28_Report.docx", "Report/Group_AI_28_Report.pdf")
