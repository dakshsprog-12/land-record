import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "@/pages/HomePage.jsx";
import UploadPage from "@/pages/UploadPage.jsx";
import Login from "@/components/auth/Login";
import RecordDetails from "@/components/RecordDetails";
import Register from "@/components/auth/Register";

const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/upload" element={<UploadPage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        {/* <Route path="/dashboard" element={<UploadCard />} /> */}
        <Route path="/records" element={<RecordDetails />} />
      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;
