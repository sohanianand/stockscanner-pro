import {
  AppBar,
  Toolbar,
  Typography,
  Box,
  Button,
} from "@mui/material";

import { useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");

    navigate("/login", {
      replace: true,
    });
  };

  return (
    <AppBar
      position="sticky"
      elevation={1}
    >
      <Toolbar>
        <Typography
          variant="h6"
          sx={{
            fontWeight: 600,
          }}
        >
          StockScanner Pro
        </Typography>

        <Box sx={{ flexGrow: 1 }} />

        <Button
          color="inherit"
          onClick={logout}
        >
          Logout
        </Button>
      </Toolbar>
    </AppBar>
  );
}
