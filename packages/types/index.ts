export interface Trade {
  id: number;
  pair: string;
  direction: "LONG" | "SHORT";
  entry_price: number;
  exit_price: number;
  pnl: number;
  emotion?: string;
  created_at: string;
}
