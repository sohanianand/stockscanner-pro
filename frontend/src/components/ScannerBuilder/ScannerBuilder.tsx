import { useState } from "react";
import { Paper } from "@mui/material";

import FilterRow from "./FilterRow";
import ScannerToolbar from "./ScannerToolbar";
import ScannerResults from "./ScannerResults";

import { useScanner } from "../../hooks/useScanner";

export default function ScannerBuilder() {

    const scanner = useScanner();

    const [condition, setCondition] = useState("AND");

    const [filters, setFilters] = useState([
        {
            field: "rsi",
            operator: "<",
            value: 30,
        },
    ]);

    const updateFilter = (index: number, filter: any) => {

        const copy = [...filters];

        copy[index] = filter;

        setFilters(copy);

    };

    const deleteFilter = (index: number) => {

        setFilters(filters.filter((_, i) => i !== index));

    };

    const addFilter = () => {

        setFilters([
            ...filters,
            {
                field: "close",
                operator: ">",
                value: "",
            },
        ]);

    };

    const runScanner = () => {

        scanner.mutate({

            condition,

            filters,

            page: 1,

            page_size: 50,

        });

    };

    return (

        <Paper sx={{ p: 3 }}>

            <ScannerToolbar
                condition={condition}
                setCondition={setCondition}
                addFilter={addFilter}
                run={runScanner}
            />

            {filters.map((filter, index) => (

                <FilterRow
                    key={index}
                    filter={filter}
                    onChange={(value: any) =>
                        updateFilter(index, value)
                    }
                    onDelete={() =>
                        deleteFilter(index)
                    }
                />

            ))}

            <ScannerResults
                loading={scanner.isPending}
                data={scanner.data}
            />

        </Paper>

    );

}
