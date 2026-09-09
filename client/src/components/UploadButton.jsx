import { useRef, useState } from "react";
import { Button } from "./ui/button";

export default function UploadButton() {
  const [selectedFile, setSelectedFile] = useState(null);
  const fileInputRef = useRef(null);

  const handleUploadClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setSelectedFile(e.target.files[0]);
    }
  };

  const handleClear = () => {
    setSelectedFile(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  const handlePreview = () => {
    if (!selectedFile) return;
    const fileUrl = URL.createObjectURL(selectedFile);
    window.open(fileUrl, "_blank");
  };

  const handleSubmit = () => {
    if (!selectedFile) return;
    alert(`File "${selectedFile.name}" submitted successfully!`);
  };

  return (
    <div className="flex flex-col items-center gap-4 w-full">
      {/* Hidden browser input */}
      <input
        type="file"
        ref={fileInputRef}
        onChange={handleFileChange}
        className="hidden"
        accept=".pdf,image/*"
      />

      {/* 1. Choose / Change File Button */}
      <Button 
        type="button"
        onClick={handleUploadClick} 
        size="lg"
        className="w-full font-semibold bg-accent text-white hover:bg-neutral-800"
      >
        {selectedFile ? "Change Selected File" : "Choose File"}
      </Button>

      {/* 2. File select hone ke baad yeh preview/clear card dikhega */}
      {selectedFile && (
        <div className="w-full flex flex-col gap-3 p-3 bg-neutral-100 border border-neutral-300 rounded-lg">
          <p className="text-xs text-neutral-800 font-mono truncate text-center font-bold">
            {selectedFile.name}
          </p>

          <div className="flex items-center gap-2">
            {/* Preview Button */}
            <Button
              type="button"
              variant="outline"
              size="sm"
              onClick={handlePreview}
              className="flex-1 text-xs border-neutral-300 text-black hover:bg-white"
            >
              Preview
            </Button>

            {/* Cancel/Clear Button */}
            <Button
              type="button"
              variant="destructive"
              size="sm"
              onClick={handleClear}
              className="flex-1 text-xs bg-red-600 hover:bg-red-700 text-white"
            >
              Clear
            </Button>
          </div>

          {/* Final Submit Button */}
          <Button
            type="button"
            size="sm"
            onClick={handleSubmit}
            className="w-full text-xs font-semibold bg-blue-600 hover:bg-blue-700 text-white mt-1"
          >
            Submit File
          </Button>
        </div>
      )}
    </div>
  );
}