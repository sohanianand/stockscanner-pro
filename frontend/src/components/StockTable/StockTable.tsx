import {

    Table,

    TableBody,

    TableCell,

    TableHead,

    TableRow,

    Paper,

} from "@mui/material";

export default function StockTable({
    data,
}: any) {

    return (

        <Paper sx={{ mt: 3 }}>

            <Table>

                <TableHead>

                    <TableRow>

                        <TableCell>Symbol</TableCell>

                        <TableCell>Close</TableCell>

                        <TableCell>RSI</TableCell>

                        <TableCell>EMA20</TableCell>

                        <TableCell>EMA50</TableCell>

                        <TableCell>Volume</TableCell>

                    </TableRow>

                </TableHead>

                <TableBody>

                    {data.map((stock: any) => (

                        <TableRow
                            key={stock.symbol}
                        >

                            <TableCell>
                                {stock.symbol}
                            </TableCell>

                            <TableCell>
                                {stock.close}
                            </TableCell>

                            <TableCell>
                                {stock.rsi}
                            </TableCell>

                            <TableCell>
                                {stock.ema20}
                            </TableCell>

                            <TableCell>
                                {stock.ema50}
                            </TableCell>

                            <TableCell>
                                {stock.volume}
                            </TableCell>

                        </TableRow>

                    ))}

                </TableBody>

            </Table>

        </Paper>

    );

}
