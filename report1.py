from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import re

def generate_report(info):
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f"report_{current_date}.pdf"
    
    # Create PDF report using ReportLab
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Add title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "Official Report")
    
    # Add report date
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, f"Report Date: {current_date}")
    
    # Add report content
    write_multiline_text(c, info, 100, height - 130)
    
    # Save the PDF
    c.save()
    
    print(f"Report saved as {filename}")
    return filename

def write_multiline_text(canvas, text, x, y):
    """Writes multiple lines of text to the PDF."""
    text_object = canvas.beginText(x, y)
    text_object.setFont("Helvetica", 12)
    lines = text.split('\n')
    for line in lines:
        text_object.textLine(line)
    canvas.drawText(text_object)

def correct_spelling(text):
    """Allows user to manually correct spelling mistakes in the input."""
    print("Detected text:")
    print(text)
    corrections = {}
    
    words = set(re.findall(r'\b\w+\b', text))
    for word in words:
        corrected_word = input(f"If '{word}' is incorrect, enter the correct spelling (or press Enter to keep it): ")
        if corrected_word.strip():
            corrections[word] = corrected_word.strip()
    
    for wrong, correct in corrections.items():
        text = text.replace(wrong, correct)
    
    return text

def get_corrected_input():
    """Allows user to enter text and correct spelling mistakes."""
    print("Enter the information for the report (type 'END' on a new line to finish):")
    info_lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == "END":
                break
            info_lines.append(line)
        except KeyboardInterrupt:
            print("\nInput interrupted. Finalizing report.")
            break
    
    info = "\n".join(info_lines)
    return correct_spelling(info)

# Example usage
info = get_corrected_input()
file_name = generate_report(info)
print(f"Download your report: {file_name}")