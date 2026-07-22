import { Routes, Route, Navigate } from "react-router-dom";

import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Scanner from "../pages/Scanner";
import Portfolio from "../pages/Portfolio";
import Watchlist from "../pages/Watchlist";
import Alerts from "../pages/Alerts";
import Backtest from "../pages/Backtest";
import Settings from "../pages/Settings";

import DashboardLayout from "../layouts/DashboardLayout";
import ProtectedRoute from "./ProtectedRoute";

export default function AppRoutes() {
  return (
    <Routes>

      <Route path="/login" element={<Login />} />

      <Route
        path="/"
        element={
          <ProtectedRoute>
            <DashboardLayout />
          </ProtectedRoute>
        }
      >
        <Route index element={<Dashboard />} />

        <Route path="scanner" element={<Scanner />} />

        <Route path="portfolio" element={<Portfolio />} />

        <Route path="watchlist" element={<Watchlist />} />

        <Route path="alerts" element={<Alerts />} />

        <Route path="backtest" element={<Backtest />} />

        <Route path="settings" element={<Settings />} />
      </Route>

      <Route path="*" element={<Navigate to="/" replace />} />

    </Routes>
  );
}
