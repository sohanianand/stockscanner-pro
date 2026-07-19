import { CssBaseline } from "@mui/material";
import { Toaster } from "react-hot-toast";
import AppRoutes from "./routes/AppRoutes";

function App() {
  return (
    <>
      <CssBaseline />
      <AppRoutes />
      <Toaster position="top-right" />
    </>
  );
}

export default App;
