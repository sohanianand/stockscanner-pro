import {
  Box,
  Button,
  Paper,
  Stack,
  TextField,
  Typography,
} from "@mui/material";

import { useState } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

import { login } from "../api/auth";

export default function Login() {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async () => {
    if (!username.trim()) {
      toast.error("Please enter username");
      return;
    }

    if (!password.trim()) {
      toast.error("Please enter password");
      return;
    }

    try {
      setLoading(true);

      const result = await login({
        username: username.trim(),
        password: password,
      });

      localStorage.setItem(
        "token",
        result.access_token
      );

      localStorage.setItem(
        "token_type",
        result.token_type || "bearer"
      );

      toast.success("Login successful");

      navigate("/");

    } catch (error: any) {
      console.error(
        "Login error:",
        error?.response?.data || error
      );

      toast.error(
        error?.response?.data?.detail ||
        "Invalid username or password"
      );

    } finally {
      setLoading(false);
    }
  };

  return (
    <Box
      display="flex"
      justifyContent="center"
      alignItems="center"
      minHeight="100vh"
    >
      <Paper
        elevation={3}
        sx={{
          p: 4,
          width: 400,
          maxWidth: "90%",
        }}
      >
        <Stack spacing={2}>
          <Typography
            variant="h5"
            align="center"
          >
            StockScanner Pro
          </Typography>

          <Typography
            variant="body2"
            color="text.secondary"
            align="center"
          >
            Login to your account
          </Typography>

          <TextField
            label="Username"
            value={username}
            onChange={(e) =>
              setUsername(e.target.value)
            }
            fullWidth
            autoComplete="username"
          />

          <TextField
            label="Password"
            type="password"
            value={password}
            onChange={(e) =>
              setPassword(e.target.value)
            }
            fullWidth
            autoComplete="current-password"
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                submit();
              }
            }}
          />

          <Button
            variant="contained"
            onClick={submit}
            disabled={loading}
            fullWidth
          >
            {loading ? "Logging in..." : "Login"}
          </Button>
        </Stack>
      </Paper>
    </Box>
  );
}
