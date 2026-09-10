import os
import pypdfium2 as pdfium


def convert_pdf_to_images(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    pdf = pdfium.PdfDocument(pdf_path)

    image_paths = []

    for page_number in range(len(pdf)):
        page = pdf[page_number]

        bitmap = page.render(scale=150 / 72)

        image_path = os.path.join(
            output_dir,
            f"page_{page_number + 1}.png"
        )

        bitmap.to_pil().save(image_path)
        image_paths.append(image_path)

        page.close()

    pdf.close()

    return image_paths