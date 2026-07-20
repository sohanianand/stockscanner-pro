import { useState } from "react";
import { Paper } from "@mui/material";

import FilterRow from "./FilterRow";
import ScannerToolbar from "./ScannerToolbar";
import ScannerResults from "./ScannerResults";
import { useScanner } from "../../hooks/useScanner";

type ComparisonOperator = "=" | ">" | "<" | ">=" | "<=" | "!=";
type LogicalOperator = "AND" | "OR";

interface ScannerFilter {
  field: string;
  operator: ComparisonOperator;
  value: string;
<<<<<<< HEAD
}

export default function ScannerBuilder() {
  const scanner = useScanner();

  const [condition, setCondition] =
    useState<LogicalOperator>("AND");

  const [filters, setFilters] = useState<ScannerFilter[]>([
    {
      field: "rsi",
      operator: "<",
      value: "30"
    }
  ]);

  const updateFilter = (
    index: number,
    filter: ScannerFilter
  ) => {
    setFilters((prev) =>
      prev.map((item, i) =>
        i === index ? filter : item
      )
    );
  };

  const deleteFilter = (index: number) => {
    setFilters((prev) =>
      prev.filter((_, i) => i !== index)
    );
  };

  const addFilter = () => {
    setFilters((prev) => [
      ...prev,
      {
        field: "close",
        operator: ">",
        value: ""
      }
    ]);
  };

  const runScanner = () => {
    scanner.mutate({
      condition,
      filters: filters.map((f) => ({
        ...f,
        value:
          f.value === ""
            ? 0
            : Number(f.value)
      })),
      page: 1,
      page_size: 50
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
          onChange={(value: ScannerFilter) =>
            updateFilter(index, value)
          }
          onDelete={() => deleteFilter(index)}
        />
      ))}

      <ScannerResults
        loading={scanner.isPending}
        data={scanner.data}
      />
    </Paper>
  );
}

export default function ScannerBuilder() {
  const scanner = useScanner();

  const [condition, setCondition] =
    useState<LogicalOperator>("AND");

  const [filters, setFilters] = useState<ScannerFilter[]>([
    {
      field: "rsi",
      operator: "<",
      value: "30"
    }
  ]);

  const updateFilter = (
    index: number,
    filter: ScannerFilter
  ) => {
    setFilters((prev) =>
      prev.map((item, i) =>
        i === index ? filter : item
      )
    );
  };

  const deleteFilter = (index: number) => {
    setFilters((prev) =>
      prev.filter((_, i) => i !== index)
    );
  };

  const addFilter = () => {
    setFilters((prev) => [
      ...prev,
      {
        field: "close",
        operator: ">",
        value: ""
      }
    ]);
  };

  const runScanner = () => {
    scanner.mutate({
      condition,
      filters: filters.map((f) => ({
        ...f,
        value:
          f.value === ""
            ? 0
            : Number(f.value)
      })),
      page: 1,
      page_size: 50
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
          onChange={(value: ScannerFilter) =>
            updateFilter(index, value)
          }
          onDelete={() => deleteFilter(index)}
        />
      ))}

      <ScannerResults
        loading={scanner.isPending}
        data={scanner.data}
      />
    </Paper>
  );
}
