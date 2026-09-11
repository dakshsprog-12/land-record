import { loginHandler, registerHandler } from "@/api/auth.api";

const useAuth = () => {
  const handleLogin = async ({ email, password }) => {
    if (!email || !password) return;
    const data = await loginHandler({ email, password });
    console.log(data)
  };
  const handleRegister = async ({ name, email, password }) => {
    if (!name || !email || !password) return;
    const data = await registerHandler({ name, email, password });
    console.log(data)
  };

  return { handleRegister, handleLogin };
};

export default useAuth;
