import userModel from "../models/user.model.js";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";

export const registerController = async (req, res) => {
  const { name, email, password } = req.body;

  const isUserExists = await userModel.findOne({ email });
  if (isUserExists)
    return res.status(409).json({
      message:
        isUserExists.email == email
          ? "Email is already registered."
          : "Username is already taken.",
    });

  bcrypt.genSalt(10, (err, salt) => {
    if (!err) {
      bcrypt.hash(password, salt, async (err, hash) => {
        if (!err) {
          const user = await userModel.create({
            name,
            email,
            password: hash,
          });
          const token = jwt.sign(
            { userId: user._id },
            process.env.JWT_SECRET_KEY,
          );
          res.cookie("token", token, {
            httpOnly: true,
            secure: true, // required for HTTPS
            sameSite: "none", // required for cross-site cookies
            path: "/",
          });
          res.status(201).json({
            message: "User registered successfully",
            user: {
              username: user.username,
              name: user.name,
              email: user.email,
              bio: user.bio,
              profileImg: user.profileImg,
              _id: user._id,
            },
          });
        } else
          return res.status(400).json({
            message: "User is not created",
          });
      });
    } else
      return res.status(400).json({
        message: "User is not created",
      });
  });
};

export const loginController = async (req, res) => {
  const { email, password } = req.body;

  const user = await userModel.findOne({ email });

  if (!user)
    return res.status(404).json({
      message: "User doesn't exists",
    });

  bcrypt.compare(password, user.password, (err, result) => {
    if (err)
      return res.status(400).json({
        message: "Something went wrong.",
        error: err,
      });
    if (result) {
      const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET_KEY);
      res.cookie("token", token, {
        httpOnly: true,
        secure: true,
        sameSite: "none",
        path: "/",
      });
      return res.status(200).json({
        message: "User loggedIn successfully",
        user: {
          name: user?.name,
          email: user.email,
        },
      });
    } else
      return res.status(400).json({
        message: "Password is wrong.",
      });
  });
};

export const logoutController = async (req, res) => {
  res.clearCookie("token");
  return res.status(200).json({
    message: "User logged out successfully",
  });
};
