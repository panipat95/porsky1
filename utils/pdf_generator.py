"""
PDF Generator Utility using fpdf2
Allows converting markdown worksheets/reports to PDF files.
"""

import os
from fpdf import FPDF

class PDFWorksheet(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 14)
        self.cell(0, 10, 'Kru Por Learning Ecosystem - Student Care & TPT Studio', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_worksheet_pdf(title: str, content: str, output_path: str) -> str:
    """แปลงเนื้อหาใบงานเป็น PDF"""
    pdf = PDFWorksheet()
    pdf.add_page()
    pdf.set_font('Helvetica', '', 12)
    
    # Title
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, title, 0, 1, 'L')
    pdf.ln(5)
    
    # Body Content
    pdf.set_font('Helvetica', '', 11)
    lines = content.split('\n')
    for line in lines:
        # Simple rendering for Helvetica
        cleaned_line = line.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 8, cleaned_line)
    
    # Make sure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)
    return output_path
