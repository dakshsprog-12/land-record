import { useNavigate } from "react-router-dom";
import { Button } from "./ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "./ui/card";

export default function RecordDetails() {
  const navigate = useNavigate();

  return (
    <Card className="w-full max-w-lg bg-white border border-neutral-200 shadow-md rounded-xl">
      <CardHeader className="text-center pb-3">
        <CardTitle className="text-2xl font-bold text-neutral-800">
          Digitized Land Record
        </CardTitle>
        <p className="text-xs text-neutral-500">
          Extracted details from uploaded document
        </p>
      </CardHeader>

      <CardContent className="flex flex-col gap-4 p-6">
        <div className="flex flex-col gap-2 border border-neutral-200 rounded-lg p-3 bg-neutral-50 text-xs">
          <div className="flex justify-between py-1 border-b border-neutral-200">
            <span className="font-semibold text-neutral-600">Owner Name:</span>
            <span className="text-neutral-800">Sample Owner</span>
          </div>
          <div className="flex justify-between py-1">
            <span className="font-semibold text-neutral-600">Document Type:</span>
            <span className="text-neutral-800">Khatiyan</span>
          </div>
        </div>

        <Button
          type="button"
          onClick={() => navigate("/dashboard")}
          className="w-full text-xs font-semibold"
        >
          Back to Dashboard
        </Button>
      </CardContent>
    </Card>
  );
}