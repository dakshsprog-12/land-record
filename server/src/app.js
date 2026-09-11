import express from "express";
import cookieParser from "cookie-parser";
// import authRouter from "./routes/auth.route.js";
// import postRouter from "./routes/post.route.js";
// import userRouter from "./routes/user.route.js";
import cors from "cors";
export const app = express();

app.use(cors({
    origin: "https://x-clone67.netlify.app",
    credentials: true
}));
app.use(express.json())
app.use(cookieParser())

app.get("/",(req,res)=>{
    res.send("Hello from backend")
});
// app.use("/api/auth",authRouter);
// app.use("/api/posts",postRouter);
// app.use("/api/user",userRouter);

