import os
import pdfkit
from bs4 import BeautifulSoup
import datetime

def combine_html_reports():
    # Create reports directory if it doesn't exist
    if not os.path.exists('reports/combined'):
        os.makedirs('reports/combined')

    # Get all HTML reports
    report_paths = [
        'reports/authentication/report.html',
        'reports/ecommerce/report.html',
        'reports/drag_and_drop/report.html'
    ]

    # Combine all HTML content
    combined_html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Combined Test Report</title>
        <style>
            body { font-family: Arial, sans-serif; }
            .report-section { margin-bottom: 30px; border-bottom: 2px solid #ccc; padding-bottom: 20px; }
            h1 { color: #333; text-align: center; }
            .summary { background-color: #f5f5f5; padding: 15px; margin: 10px 0; }
            .timestamp { text-align: right; color: #666; }
        </style>
    </head>
    <body>
        <h1>Combined Test Report</h1>
        <div class="timestamp">Generated on: ''' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '''</div>
    '''

    total_tests = 0
    total_passed = 0
    total_failed = 0

    for report_path in report_paths:
        if os.path.exists(report_path):
            with open(report_path, 'r', encoding='utf-8') as file:
                content = file.read()
                soup = BeautifulSoup(content, 'html.parser')
                
                # Extract the test results
                section_name = os.path.basename(os.path.dirname(report_path)).capitalize()
                results = soup.find('p', class_='heading').get_text() if soup.find('p', class_='heading') else "Results not found"
                
                # Add section to combined HTML
                combined_html += f'''
                <div class="report-section">
                    <h2>{section_name} Tests</h2>
                    <div class="summary">{results}</div>
                    {str(soup.find('div', id='results-table'))}
                </div>
                '''

    combined_html += '''
    </body>
    </html>
    '''

    # Save combined HTML
    combined_html_path = 'reports/combined/combined_report.html'
    with open(combined_html_path, 'w', encoding='utf-8') as f:
        f.write(combined_html)

    # Convert to PDF
    try:
        config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
        pdfkit.from_file(combined_html_path, 'reports/combined/combined_report.pdf', configuration=config)
        print(f"PDF report generated successfully at reports/combined/combined_report.pdf")
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")
        print("Please ensure wkhtmltopdf is installed on your system.")

if __name__ == "__main__":
    combine_html_reports()