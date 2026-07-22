import {
  Card,
  CardContent,
  Grid,
  Typography,
} from "@mui/material";

interface Props {

  indicators?: {

    rsi?: number;

    ema20?: number;

    ema50?: number;

    macd?: number;

  };

}

export default function IndicatorCards({
  indicators,
}: Props) {

  const items = [

    {
      title: "RSI",

      value:
        indicators?.rsi ??
        "-",
    },

    {
      title: "EMA 20",

      value:
        indicators?.ema20 ??
        "-",
    },

    {
      title: "EMA 50",

      value:
        indicators?.ema50 ??
        "-",
    },

    {
      title: "MACD",

      value:
        indicators?.macd ??
        "-",
    },

  ];

  return (

    <Grid
      container
      spacing={2}
      sx={{ mt: 2 }}
    >

      {items.map((item) => (

        <Grid
          key={item.title}
          size={{
            xs: 12,
            sm: 6,
            md: 3,
          }}
        >

          <Card>

            <CardContent>

              <Typography
                variant="body2"
                color="text.secondary"
              >

                {item.title}

              </Typography>

              <Typography
                variant="h5"
                sx={{ mt: 1 }}
              >

                {item.value}

              </Typography>

            </CardContent>

          </Card>

        </Grid>

      ))}

    </Grid>

  );

}
