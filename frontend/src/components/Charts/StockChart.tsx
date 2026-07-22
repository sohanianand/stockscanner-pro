import { useEffect, useRef } from "react";

import {
  createChart,
  ColorType,
  CandlestickSeries,
} from "lightweight-charts";

interface PriceData {
  date: string;
  open: number;
  high: number;
  low: number;
  close: number;
}

interface Props {
  data: PriceData[];
}

export default function StockChart({
  data,
}: Props) {

  const chartContainerRef =
    useRef<HTMLDivElement>(null);

  useEffect(() => {

    if (!chartContainerRef.current) {
      return;
    }

    const chart = createChart(
      chartContainerRef.current,
      {
        width:
          chartContainerRef.current.clientWidth,

        height: 500,

        layout: {
          background: {
            type: ColorType.Solid,
            color: "#121212",
          },

          textColor: "#ffffff",
        },

        grid: {
          vertLines: {
            visible: false,
          },

          horzLines: {
            visible: false,
          },
        },
      }
    );

    const candlestickSeries =
      chart.addSeries(
        CandlestickSeries,
        {}
      );

    candlestickSeries.setData(

      data.map((item) => ({

        time:
          item.date.substring(0, 10),

        open: item.open,

        high: item.high,

        low: item.low,

        close: item.close,

      }))

    );

    chart.timeScale().fitContent();

    const resizeObserver =
      new ResizeObserver(() => {

        if (
          chartContainerRef.current
        ) {

          chart.applyOptions({

            width:
              chartContainerRef.current
                .clientWidth,

          });

        }

      });

    resizeObserver.observe(
      chartContainerRef.current
    );

    return () => {

      resizeObserver.disconnect();

      chart.remove();

    };

  }, [data]);

  return (

    <div
      ref={chartContainerRef}
      style={{
        width: "100%",
        height: "500px",
      }}
    />

  );

}
