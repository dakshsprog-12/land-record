import { Card, CardContent } from "@/components/ui/card";
import UploadButton from "@/components/UploadButton";

const UploadPage = () => {
  return (
    <div className="flex min-h-screen w-full items-center justify-center">
      <Card
        style={{ backgroundColor: "var(--accent-bg)" }}
        className="w-100 min-h-50 shadow-xl rounded-2xl border bg-red-500"
      >
        <CardContent className="flex flex-col items-center w-full h-full text-red-500 bg-blue-500">
          <div
          style={{height:"100%"}}
           className="w-full h-3/4 bg-red-600 flex-1">
            <h1
              style={{ color: "#000000" }}
              className="text-xl font-medium tracking-tight text-center"
            >
              Bhumi-Setu
            </h1>
            <h2
              style={{ color: "#475569" }}
              className="text-xl font-medium tracking-tight text-center"
            >
              Land Record Digitizer
            </h2>
          </div>
          <UploadButton />
        </CardContent>
      </Card>
    </div>
  );
};

export default UploadPage;
