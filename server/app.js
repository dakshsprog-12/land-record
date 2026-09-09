import express from "express";
import { createWorker } from "tesseract.js";
import sharp from "sharp";
import fs from "fs";
import Tesseract from "tesseract.js";

const app = express();

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.use(express.json());

const extractTextFromImage = async (imagePath) => {
  try {
    const worker = await createWorker("eng");
    const { data } = await worker.recognize(imagePath);
    console.log(data);
    await worker.terminate();
    return data.text;
  } catch (error) {
    console.error("Error extracting text from image:", error);
    return "";
  }
};

async function processHandwriting(imagePath) {
  const processedImagePath = "optimized_handwriting.png";

  try {
    console.log("✏️  Pre-processing the handwriting sample...");

    // 1. Image Pre-processing with Sharp (Crucial for handwriting)
    await sharp(imagePath)
      .resize({ width: 2000 }) // Upscale image so pixels are distinct
      .greyscale() // Remove color data noise
      .linear(1.5, -0.2) // Boost contrast to isolate strokes
      .threshold(140) // Convert to clean binary black and white
      .toFile(processedImagePath);

    console.log("🔍 Running Tesseract.js OCR...");

    // 2. Instantiate Tesseract Worker with specialized parameters
    const worker = await createWorker("eng");

    // Set Page Segmentation Mode (PSM)
    // PSM 7 treats the image as a single text line, PSM 6 treats it as a single uniform block of text.
    await worker.setParameters({
      tessedit_pageseg_mode: Tesseract.PSM.SINGLE_BLOCK,
    });

    // 3. Perform text recognition
    const {
      data: { text, confidence },
    } = await worker.recognize(processedImagePath);

    console.log("\n================ Extracted Text ================");
    console.log(text);
    console.log("================================================");
    console.log(`Confidence Score: ${confidence}%`);

    // Clean up worker and temporary image
    await worker.terminate();
    fs.unlinkSync(processedImagePath);
    return text;
  } catch (error) {
    console.error("An error occurred during processing:", error);
  }
}

app.get("/api/upload", async (req, res) => {
  const imagePath = "./assets/img4.jpeg";
  let extractedText = "";

//   extractedText = await extractTextFromImage(imagePath);
  extractedText = await processHandwriting(imagePath);

  // Process the uploaded file
  res
    .status(200)
    .json({ message: "File uploaded successfully", extractedText });
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
