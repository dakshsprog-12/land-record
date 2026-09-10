import { Routes, Route } from "react-router-dom";
import AuthCard from "../components/AuthCard.jsx";
import UploadCard from "../components/UploadCard.jsx";
import RecordDetails from "../components/RecordDetails.jsx";

export default function AppRoutes() {
  return (
    <Routes>
      {/* 1. Default Route: Login / Register screen */}
      <Route path="/" element={<AuthCard />} />

      {/* 2. Dashboard Route: Upload land records */}
      <Route path="/dashboard" element={<UploadCard />} />

      {/* 3. Output Route: Extracted land data */}
      <Route path="/records" element={<RecordDetails />} />
    </Routes>
  );
}