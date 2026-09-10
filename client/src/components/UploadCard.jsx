import { Card, CardContent } from "./ui/card";
import Title from "./title";
import UploadButton from "./UploadButton";

export default function UploadCard() {
  return (
    <Card 
  style={{ backgroundColor: "var(--accent-bg)" }} 
  className="w-full max-w-sm shadow-xl rounded-2xl border border-slate-200"
>
  <CardContent className="flex flex-col items-center gap-6 p-6">
    <Title />
    <UploadButton />
  </CardContent>
</Card>
  );
}