import api from "./api";

export interface StockPrice {
  date: string;
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number;
}

export interface StockIndicators {
  rsi?: number;
  ema20?: number;
  ema50?: number;
  macd?: number;
  bollinger_upper?: number;
  bollinger_middle?: number;
  bollinger_lower?: number;
}

export interface StockDetail {
  symbol: string;
  name?: string;
  exchange?: string;
  current_price: number;
  change_percent?: number;
  prices: StockPrice[];
  indicators?: StockIndicators;
}

export async function getStockDetail(
  symbol: string
): Promise<StockDetail> {

  const response = await api.get(
    `/stocks/${symbol}`
  );

  return response.data;
}
