import { useRef, useState } from "react";
import { Button } from "./ui/button";

export default function UploadButton() {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const fileInputRef = useRef(null);

  const handleUploadClick = () => {
    fileInputRef.current?.click();
  };

  // for one or more file selection
  const handleFileChange = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      const newFiles = Array.from(e.target.files);
      setSelectedFiles((prev) => [...prev, ...newFiles]);
    }
  };

  // specific file clear
  const handleRemoveSingle = (indexToRemove) => {
    setSelectedFiles((prev) => prev.filter((_, idx) => idx !== indexToRemove));
  };

  // to clear all
  const handleClearAll = () => {
    setSelectedFiles([]);
    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  // specific preview
  const handlePreview = (file) => {
    const fileUrl = URL.createObjectURL(file);
    window.open(fileUrl, "_blank");
  };

  const handleSubmit = () => {
    if (selectedFiles.length === 0) return;
    alert(`${selectedFiles.length} files submitted!`);
  };

  return (
    <div className="flex flex-col items-center gap-4 w-full">
      <input
        type="file"
        ref={fileInputRef}
        onChange={handleFileChange}
        multiple
        className="hidden"
        accept=".pdf,image/*"
      />

      {/* Choose Files Button */}
      <Button 
        type="button"
        onClick={handleUploadClick} 
        size="lg"
        style={{ 
          backgroundColor: "var(--btn-bg, #4f5a4a)", 
          color: "var(--btn-text, #ffffff)" 
        }}
        className="w-full font-medium"
      >
        {selectedFiles.length > 0 ? "Add More Files" : "Choose Files"}
      </Button>

      {/* Selected Files List View */}
      {selectedFiles.length > 0 && (
        <div className="w-full flex flex-col gap-3 p-3 bg-neutral-100/70 border border-neutral-300 rounded-lg max-h-56 overflow-y-auto">
          <div className="flex items-center justify-between border-b pb-2 border-neutral-300">
            <span className="text-xs font-semibold text-neutral-600">
              Selected ({selectedFiles.length})
            </span>
            <button
              type="button"
              onClick={handleClearAll}
              className="text-[11px] text-red-600 hover:underline font-medium"
            >
              Clear All
            </button>
          </div>

          {/* List of files */}
          <div className="flex flex-col gap-2">
            {selectedFiles.map((file, index) => (
              <div 
                key={index} 
                className="flex items-center justify-between gap-2 p-2 bg-white rounded border border-neutral-200"
              >
                <span className="text-xs font-mono text-neutral-700 truncate max-w-[160px]">
                  {file.name}
                </span>

                <div className="flex items-center gap-1">
                  <Button
                    type="button"
                    variant="outline"
                    size="sm"
                    onClick={() => handlePreview(file)}
                    className="h-7 px-2 text-[11px]"
                  >
                    Preview
                  </Button>
                  <Button
                    type="button"
                    variant="destructive"
                    size="sm"
                    onClick={() => handleRemoveSingle(index)}
                    className="h-7 px-2 text-[11px]"
                  >
                    ✕
                  </Button>
                </div>
              </div>
            ))}
          </div>

          {/* Submit Button */}
          <Button
            type="button"
            size="sm"
            onClick={handleSubmit}
            className="w-full text-xs font-semibold bg-blue-600 hover:bg-blue-700 text-white mt-1"
          >
            Submit All ({selectedFiles.length})
          </Button>
        </div>
      )}
    </div>
  );
}