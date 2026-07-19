import { Box } from "@mui/material";
import { Outlet } from "react-router-dom";

import Navbar from "../components/Navbar/Navbar";
import Sidebar from "../components/Sidebar/Sidebar";

export default function DashboardLayout() {
  return (
    <Box display="flex">

      <Sidebar />

      <Box flex={1}>

        <Navbar />

        <Box p={3}>
          <Outlet />
        </Box>

      </Box>

    </Box>
  );
}
