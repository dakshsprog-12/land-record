from app.preprocessing.image import upscale_image


input_path = "img2.png"
output_path = "upscaled.jpg"

upscale_image(
    input_path,
    output_path,
    scale=2
)

print("Upscaled image saved to:", output_path)