import {
  Drawer,
  List,
  ListItemButton,
  ListItemText,
  Toolbar,
} from "@mui/material";

import { useNavigate } from "react-router-dom";

const menu = [

  {
    title: "Dashboard",
    path: "/",
  },

  {
    title: "Scanner",
    path: "/scanner",
  },

  {
    title: "Portfolio",
    path: "/portfolio",
  },

  {
    title: "Watchlist",
    path: "/watchlist",
  },

  {
    title: "Backtest",
    path: "/backtest",
  },

  {
    title: "Alerts",
    path: "/alerts",
  },

  {
    title: "Settings",
    path: "/settings",
  },

];

export default function Sidebar() {

  const navigate = useNavigate();

  return (

    <Drawer
      variant="permanent"
    >

      <Toolbar />

      <List>

        {

          menu.map((item) => (

            <ListItemButton
              key={item.path}
              onClick={() =>
                navigate(item.path)
              }
            >

              <ListItemText
                primary={item.title}
              />

            </ListItemButton>

          ))

        }

      </List>

    </Drawer>

  );

}
