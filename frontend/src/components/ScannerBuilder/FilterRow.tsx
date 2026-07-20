import {
  Grid,
  MenuItem,
  Select,
  TextField,
  IconButton,
} from "@mui/material";

import DeleteIcon from "@mui/icons-material/Delete";

const fields = [
  "close",
  "volume",
  "rsi",
  "ema20",
  "ema50",
  "sma20",
  "macd",
];

const operators = [
  "=",
  ">",
  "<",
  ">=",
  "<=",
  "!=",
];

export default function FilterRow({
  filter,
  onChange,
  onDelete,
}: any) {

  return (

    <Grid
      container
      spacing={2}
      sx={{ mb: 2 }}
    >

      <Grid size={4}>

        <Select
          fullWidth
          value={filter.field}
          onChange={(e) =>
            onChange({
              ...filter,
              field: e.target.value,
            })
          }
        >

          {
            fields.map((field) => (

              <MenuItem
                key={field}
                value={field}
              >

                {field}

              </MenuItem>

            ))
          }

        </Select>

      </Grid>

      <Grid size={2}>

        <Select
          fullWidth
          value={filter.operator}
          onChange={(e) =>
            onChange({
              ...filter,
              operator: e.target.value,
            })
          }
        >

          {
            operators.map((op) => (

              <MenuItem
                key={op}
                value={op}
              >

                {op}

              </MenuItem>

            ))
          }

        </Select>

      </Grid>

      <Grid size={4}>

        <TextField
          fullWidth
          value={filter.value}
          onChange={(e) =>
            onChange({
              ...filter,
              value: e.target.value,
            })
          }
        />

      </Grid>

      <Grid size={2}>

        <IconButton
          color="error"
          onClick={onDelete}
        >

          <DeleteIcon />

        </IconButton>

      </Grid>

    </Grid>

  );

}
