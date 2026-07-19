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

    navigate("/login");

  };

  return (

    <AppBar
      position="static"
      elevation={1}
    >

      <Toolbar>

        <Typography
          variant="h6"
        >

          StockScanner Pro

        </Typography>

        <Box flex={1} />

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
