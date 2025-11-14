from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)

# Assuming the PDF folder is named 'pdf' in the same directory as this script
PDF_FOLDER = 'pdf'

# Global flag to control PDF display
show_pdf = True

@app.route('/')
def home():
    if not show_pdf:
        return "PDF display is currently disabled"
    
    # Specify the PDF filename here; change 'example.pdf' to your actual PDF file
    pdf_filename = 'wss.pdf'
    
    # Check if the file exists
    pdf_path = os.path.join(PDF_FOLDER, pdf_filename)
    if os.path.exists(pdf_path):
        return send_from_directory(PDF_FOLDER, pdf_filename, as_attachment=False)
    else:
        return f"PDF file '{pdf_filename}' not found in '{PDF_FOLDER}' folder.", 404

@app.route('/sam')
def admin():
    global show_pdf
    # Toggle the flag on each visit to /admin (for simplicity; you can modify to use POST for one-way disable)
    show_pdf = not show_pdf
    status = "enabled" if show_pdf else "disabled"
    return render_template_string("""
    <h1>Admin Control</h1>
    <p>PDF display is now {{ status }}.</p>
    <p>Visit <a href="/">/</a> to check the home route.</p>
    <p>Visit <a href="/admin">/admin</a> again to toggle.</p>
    """, status=status)

if __name__ == '__main__':
    
