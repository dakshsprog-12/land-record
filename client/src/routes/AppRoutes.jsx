import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "@/pages/HomePage.jsx";
import UploadPage from "@/pages/UploadPage.jsx";
import AuthCard from "@/components/AuthCard";
import UploadCard from "@/components/UploadCard";
import RecordDetails from "@/components/RecordDetails";

const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/upload" element={<UploadPage />} />
        <Route path="/auth" element={<AuthCard />} />
        <Route path="/dashboard" element={<UploadCard />} />
        <Route path="/records" element={<RecordDetails />} />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;
