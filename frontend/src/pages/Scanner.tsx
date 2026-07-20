import {

    Typography,

    Box,

} from "@mui/material";

import ScannerBuilder from "../components/ScannerBuilder/ScannerBuilder";

export default function Scanner() {

    return (

        <Box>

            <Typography
                variant="h4"
                mb={3}
            >

                Scanner Builder

            </Typography>

            <ScannerBuilder />

        </Box>

    );

}
