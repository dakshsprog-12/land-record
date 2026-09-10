from app.preprocessing.image import preprocess_image


input_path = "img2.png"
output_path = "processed.jpg"

preprocess_image(input_path, output_path)

print(f"Processed image saved to: {output_path}")