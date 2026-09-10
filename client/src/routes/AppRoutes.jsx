import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "../pages/HomePage.jsx";
import UploadPage from "../pages/UploadPage.jsx";

const AppRoutes = () => {
  return (
    <BrowserRouter>
    <Routes>
        <Route path='/' element={ <HomePage /> } />
        <Route path='/upload' element={ <UploadPage /> } />
    </Routes>
    </BrowserRouter>
  )
}

export default AppRoutes