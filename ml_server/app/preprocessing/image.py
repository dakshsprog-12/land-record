import cv2


def preprocess_image(input_path, output_path):
    image = cv2.imread(input_path)

    if image is None:
        raise ValueError(f"Could not read image: {input_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    denoised = cv2.GaussianBlur(gray, (3, 3), 0)

    processed = cv2.threshold(
        denoised,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    cv2.imwrite(output_path, processed)

    return output_path


def upscale_image(input_path, output_path, scale=2):
    image = cv2.imread(input_path)

    if image is None:
        raise ValueError(f"Could not read image: {input_path}")

    height, width = image.shape[:2]

    upscaled = cv2.resize(
        image,
        (width * scale, height * scale),
        interpolation=cv2.INTER_CUBIC
    )

    cv2.imwrite(output_path, upscaled)

    return output_path