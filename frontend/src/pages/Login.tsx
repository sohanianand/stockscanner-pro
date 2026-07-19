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

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const submit = async () => {

    try {

      const result = await login({

        email,

        password,

      });

      localStorage.setItem(

        "token",

        result.access_token

      );

      toast.success(

        "Login successful"

      );

      navigate("/");

    }

    catch {

      toast.error(

        "Invalid credentials"

      );

    }

  };

  return (

    <Box

      display="flex"

      justifyContent="center"

      alignItems="center"

      height="100vh"

    >

      <Paper

        sx={{

          p: 4,

          width: 400,

        }}

      >

        <Stack spacing={2}>

          <Typography variant="h5">

            StockScanner Pro

          </Typography>

          <TextField

            label="Email"

            value={email}

            onChange={(e) =>
              setEmail(e.target.value)
            }

          />

          <TextField

            label="Password"

            type="password"

            value={password}

            onChange={(e) =>
              setPassword(e.target.value)
            }

          />

          <Button

            variant="contained"

            onClick={submit}

          >

            Login

          </Button>

        </Stack>

      </Paper>

    </Box>

  );

}
