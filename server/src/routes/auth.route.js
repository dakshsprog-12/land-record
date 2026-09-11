import { Router } from "express";


export const authRouter = Router();
const authController = require("../controllers/auth.controller");

authRouter.post("/register", authController.registerController);
authRouter.post("/login", authController.loginController);
authRouter.post("/logout", authController.logoutController);

