from app.pdf.processor import convert_pdf_to_images


pdf_path = "bhumi_rasid.pdf"
output_dir = "pdf_pages"

pages = convert_pdf_to_images(
    pdf_path,
    output_dir
)

print("Pages converted:")

for page in pages:
    print(page)