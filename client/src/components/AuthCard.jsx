import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "./ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "./ui/card";
import { Eye, EyeOff } from "lucide-react"; // Icons import

export default function AuthCard() {
  const [isLogin, setIsLogin] = useState(true);
  const [showPassword, setShowPassword] = useState(false); // Password visibility state
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
  });

  const navigate = useNavigate();

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.email || !formData.password) {
      alert("Please fill all required fields");
      return;
    }
    if (!isLogin && !formData.name) {
      alert("Please enter your name");
      return;
    }

    navigate("/dashboard");
  };

  return (
    <Card className="w-full max-w-sm bg-white border border-neutral-200 shadow-lg rounded-2xl" style={{ backgroundColor: "var(--accent-bg)" }}>
      <CardHeader className="text-center pb-2">
        <CardTitle className="text-2xl font-bold text-neutral-900">
          {isLogin ? "Welcome Back" : "Create Account"}
        </CardTitle>
        <p className="text-xs text-neutral-500 mt-1">
          {isLogin
            ? "Enter your credentials to access your land records"
            : "Register to digitize and manage records"}
        </p>
      </CardHeader>

      <CardContent className="p-6 pt-2">
        <form onSubmit={handleSubmit} className="flex flex-col gap-3">
          {/* Registration only: Name Field */}
          {!isLogin && (
            <div className="flex flex-col gap-1 text-left">
              <label className="text-xs font-semibold text-neutral-700">Full Name</label>
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleInputChange}
                placeholder="Name"
                className="w-full p-2.5 text-xs border border-neutral-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-neutral-800"
              />
            </div>
          )}

          {/* Email Field */}
          <div className="flex flex-col gap-1 text-left">
            <label className="text-xs font-semibold text-neutral-700">Email Address</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleInputChange}
              placeholder="name@domain.com"
              className="w-full p-2.5 text-xs border border-neutral-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-neutral-800"
            />
          </div>

          {/* Password Field with Eye Toggle */}
          <div className="flex flex-col gap-1 text-left">
            <label className="text-xs font-semibold text-neutral-700">Password</label>
            <div className="relative flex items-center">
              <input
                type={showPassword ? "text" : "password"}
                name="password"
                value={formData.password}
                onChange={handleInputChange}
                placeholder="••••••••"
                className="w-full p-2.5 pr-10 text-xs border border-neutral-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-neutral-800"
              />
              <button
                type="button"
                onClick={() => setShowPassword((prev) => !prev)}
                className="absolute right-3 text-neutral-500 hover:text-neutral-800 focus:outline-none cursor-pointer"
              >
                {showPassword ? (
                  <EyeOff className="w-4 h-4" />
                ) : (
                  <Eye className="w-4 h-4" />
                )}
              </button>
            </div>
          </div>

          {/* Action Button */}
          <Button
            type="submit"
            className="w-full mt-2 font-medium bg-neutral-900 hover:bg-neutral-800 text-white" style={{ backgroundColor: "var(--accent)" }}
          >
            {isLogin ? "Sign In" : "Register"}
          </Button>

          {/* Toggle between Login and Register */}
          <div className="text-center mt-2">
            <button
              type="button"
              onClick={() => setIsLogin(!isLogin)}
              className="text-xs text-neutral-600 hover:text-black underline underline-offset-4 cursor-pointer"
            >
              {isLogin
                ? "Don't have an account? Register here"
                : "Already have an account? Sign In"}
            </button>
          </div>
        </form>
      </CardContent>
    </Card>
  );
}