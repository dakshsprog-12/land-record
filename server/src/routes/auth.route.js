import { Router } from "express";
import {
  registerController,
  loginController,
  logoutController,
} from "../controllers/auth.conroller.js";

const authRouter = Router();

authRouter.post("/register", registerController);
authRouter.post("/login", loginController);
authRouter.post("/logout", logoutController);

export default authRouter;
