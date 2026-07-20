export type LogicalOperator = "AND" | "OR";

export type ComparisonOperator =
  | "="
  | ">"
  | "<"
  | ">="
  | "<="
  | "!=";

export interface ScannerFilter {
  field: string;
  operator: ComparisonOperator;
  value: string | number;
}

export interface SortRequest {
  field: string;
  direction: "asc" | "desc";
}

export interface ScannerRequest {
  condition: LogicalOperator;
  filters: ScannerFilter[];
  sort?: SortRequest;
  page: number;
  page_size: number;
}

export interface ScanResult {
  symbol: string;
  close: number;
  volume: number;
  rsi: number;
  ema20: number;
  ema50: number;
  sma20: number;
  macd: number;
}

export interface ScannerResponse {
  total: number;
  page: number;
  page_size: number;
  results: ScanResult[];
}
