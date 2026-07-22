import {
  Box,
  CircularProgress,
  Typography,
  Button,
} from "@mui/material";

import {
  useQuery,
} from "@tanstack/react-query";

import {
  useNavigate,
  useParams,
} from "react-router-dom";

import {
  getStockDetail,
} from "../api/stocks";

import StockChart
  from "../components/Charts/StockChart";

import IndicatorCards
  from "../components/Charts/IndicatorCards";

export default function StockDetail() {

  const { symbol } =
    useParams<{
      symbol: string;
    }>();

  const navigate =
    useNavigate();

  const {
    data,
    isLoading,
    isError,
  } = useQuery({

    queryKey: [
      "stock",
      symbol,
    ],

    queryFn: () =>
      getStockDetail(
        symbol!
      ),

    enabled:
      Boolean(symbol),

  });

  if (isLoading) {

    return (

      <Box
        display="flex"
        justifyContent="center"
        mt={10}
      >

        <CircularProgress />

      </Box>

    );

  }

  if (isError || !data) {

    return (

      <Box>

        <Typography
          variant="h5"
          color="error"
        >

          Unable to load stock data

        </Typography>

        <Button
          sx={{ mt: 2 }}
          variant="contained"
          onClick={() =>
            navigate(-1)
          }
        >

          Go Back

        </Button>

      </Box>

    );

  }

  return (

    <Box>

      <Typography
        variant="h4"
      >

        {data.symbol}

      </Typography>

      <Typography
        variant="body1"
        color="text.secondary"
      >

        {data.name}

      </Typography>

      <Typography
        variant="h3"
        sx={{ mt: 2 }}
      >

        ₹{data.current_price}

      </Typography>

      {data.change_percent !==
        undefined && (

        <Typography
          color={
            data.change_percent >= 0
              ? "success.main"
              : "error.main"
          }
        >

          {data.change_percent >= 0
            ? "+"
            : ""}

          {data.change_percent}%

        </Typography>

      )}

      <IndicatorCards
        indicators={
          data.indicators
        }
      />

      <Box
        sx={{ mt: 4 }}
      >

        <Typography
          variant="h5"
          sx={{ mb: 2 }}
        >

          Price Chart

        </Typography>

        <StockChart
          data={data.prices}
        />

      </Box>

    </Box>

  );

}
