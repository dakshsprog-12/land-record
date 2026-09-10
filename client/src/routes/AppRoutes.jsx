import { Routes, Route } from "react-router-dom";
import UploadCard from "../components/UploadCard.jsx";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<UploadCard />} />
    </Routes>
  );
}