import {
  Drawer,
  List,
  ListItemButton,
  ListItemText,
  Toolbar,
  Box,
} from "@mui/material";

import {
  Dashboard,
  Search,
  AccountBalance,
  WatchLater,
  Notifications,
  Assessment,
  Settings,
} from "@mui/icons-material";

import { useLocation, useNavigate } from "react-router-dom";

const DRAWER_WIDTH = 240;

const menu = [
  {
    title: "Dashboard",
    path: "/",
    icon: <Dashboard />,
  },
  {
    title: "Scanner",
    path: "/scanner",
    icon: <Search />,
  },
  {
    title: "Portfolio",
    path: "/portfolio",
    icon: <AccountBalance />,
  },
  {
    title: "Watchlist",
    path: "/watchlist",
    icon: <WatchLater />,
  },
  {
    title: "Backtest",
    path: "/backtest",
    icon: <Assessment />,
  },
  {
    title: "Alerts",
    path: "/alerts",
    icon: <Notifications />,
  },
  {
    title: "Settings",
    path: "/settings",
    icon: <Settings />,
  },
];

export default function Sidebar() {
  const navigate = useNavigate();

  const location = useLocation();

  return (
    <Drawer
      variant="permanent"
      sx={{
        width: DRAWER_WIDTH,
        flexShrink: 0,

        "& .MuiDrawer-paper": {
          width: DRAWER_WIDTH,
          boxSizing: "border-box",

          display: "flex",
          flexDirection: "column",

          overflowY: "auto",
          overflowX: "hidden",
        },
      }}
    >
      {/* Space for Navbar */}
      <Toolbar />

      {/* Menu */}
      <Box
        sx={{
          flexGrow: 1,
          overflowY: "auto",
        }}
      >
        <List>
          {menu.map((item) => {
            const isActive =
              location.pathname === item.path ||
              (
                item.path !== "/" &&
                location.pathname.startsWith(
                  item.path
                )
              );

            return (
              <ListItemButton
                key={item.path}
                selected={isActive}
                onClick={() =>
                  navigate(item.path)
                }
                sx={{
                  minHeight: 48,
                  px: 2.5,
                }}
              >
                {item.icon}

                <ListItemText
                  primary={item.title}
                  sx={{
                    ml: 2,
                  }}
                />
              </ListItemButton>
            );
          })}
        </List>
      </Box>
    </Drawer>
  );
}
