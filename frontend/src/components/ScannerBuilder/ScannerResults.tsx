import {
    CircularProgress,
    Typography,
} from "@mui/material";

import StockTable from "../StockTable/StockTable";

export default function ScannerResults({
    loading,
    data,
}: any) {

    if (loading) {

        return <CircularProgress />;

    }

    if (!data) {

        return (
            <Typography>
                Run scanner to see results
            </Typography>
        );

    }

    return (

        <StockTable
            data={data.results}
        />

    );

}
