import {
  Navigate,
  Route,
  Routes,
} from "react-router-dom";

import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Scanner from "../pages/Scanner";
import Portfolio from "../pages/Portfolio";
import Watchlist from "../pages/Watchlist";
import Alerts from "../pages/Alerts";
import Backtest from "../pages/Backtest";
import Settings from "../pages/Settings";
import StockDetail from "../pages/StockDetail";

import DashboardLayout from "../layouts/DashboardLayout";
import ProtectedRoute from "./ProtectedRoute";

export default function AppRoutes() {
  return (
    <Routes>

      {/* Public Route */}
      <Route
        path="/login"
        element={<Login />}
      />

      {/* Protected Application */}
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <DashboardLayout />
          </ProtectedRoute>
        }
      >

        {/* Dashboard */}
        <Route
          index
          element={<Dashboard />}
        />

        <Route
          path="dashboard"
          element={<Dashboard />}
        />

        {/* Scanner */}
        <Route
          path="scanner"
          element={<Scanner />}
        />

        {/* Portfolio */}
        <Route
          path="portfolio"
          element={<Portfolio />}
        />

        {/* Watchlist */}
        <Route
          path="watchlist"
          element={<Watchlist />}
        />

        {/* Alerts */}
        <Route
          path="alerts"
          element={<Alerts />}
        />

        {/* Backtesting */}
        <Route
          path="backtest"
          element={<Backtest />}
        />

        {/* Settings */}
        <Route
          path="settings"
          element={<Settings />}
        />

        {/* Stock Detail */}
        <Route
          path="stock/:symbol"
          element={<StockDetail />}
        />

      </Route>

      {/* Unknown Route */}
      <Route
        path="*"
        element={
          <Navigate
            to="/"
            replace
          />
        }
      />

    </Routes>
  );
}
