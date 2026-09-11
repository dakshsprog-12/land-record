import UploadButton from "@/components/UploadButton";

const UploadPage = () => {
  return (
    <div className="flex h-screen w-full items-center justify-center">
      <div className="w-100 min-h-60 shadow-xl rounded-2xl border overflow-hidden">
        <div className="flex flex-col items-center justify-center w-full h-full gap-6">
          <h1 className="text-xl font-medium tracking-tight text-center">
            Upload your files
          </h1>

          <UploadButton />
        </div>
      </div>
    </div>
  );
};

export default UploadPage;
