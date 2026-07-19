import React from "react";
import ReactDOM from "react-dom/client";

import { BrowserRouter } from "react-router-dom";

import { QueryClient } from "@tanstack/react-query";

import { QueryClientProvider } from "@tanstack/react-query";

import { Provider } from "react-redux";

import { ThemeProvider } from "@mui/material/styles";

import theme from "./theme/theme";

import App from "./App";

import { store } from "./store/store";

const queryClient = new QueryClient();

ReactDOM.createRoot(
    document.getElementById("root")!
).render(

    <Provider store={store}>

        <QueryClientProvider client={queryClient}>

            <ThemeProvider theme={theme}>

                <BrowserRouter>

                    <App />

                </BrowserRouter>

            </ThemeProvider>

        </QueryClientProvider>

    </Provider>

);
