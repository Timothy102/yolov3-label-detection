import fitz

# Open the PDF file
pdf_file_path = "DicksRoutingGuide (1).pdf"
pdf_document = fitz.open(pdf_file_path)

# Get the first page
page_number = 44  # Page numbering starts from 0, so page 45 is index 44
page = pdf_document.load_page(page_number)

# Get images from the page
images = page.get_images(full=True)

# Extract the first image
first_image = None
if images:
    image = images[0]  # Get the first image (assuming only one image per page)
    xref = image[0]
    base_image = pdf_document.extract_image(xref)
    image_bytes = base_image["image"]
    first_image = open("extracted_image.jpg", "wb")
    first_image.write(image_bytes)
    first_image.close()

# Close the PDF file
pdf_document.close()
