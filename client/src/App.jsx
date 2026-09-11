import { BrowserRouter } from "react-router-dom";
import AppRoutes from "./routes/AppRoutes.jsx";

export default function App() {
  return (
    <BrowserRouter>
      <main 
        style={{ backgroundColor: "var(--bg-body, #ffffff)" }} 
        className="min-h-screen w-full flex items-center justify-center p-4 border"
      >
        <AppRoutes />
      </main>
    </BrowserRouter>
  );
}