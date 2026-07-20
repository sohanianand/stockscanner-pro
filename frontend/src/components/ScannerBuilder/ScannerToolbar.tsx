import {
  Stack,
  Button,
  ToggleButton,
  ToggleButtonGroup,
} from "@mui/material";

export default function ScannerToolbar({
  condition,
  setCondition,
  addFilter,
  run,
}: any) {

  return (

    <Stack
      direction="row"
      spacing={2}
      sx={{ mb: 3 }}
    >

      <ToggleButtonGroup
        value={condition}
        exclusive
        onChange={(_, value) => {

          if (value) {

            setCondition(value);

          }

        }}
      >

        <ToggleButton value="AND">
          AND
        </ToggleButton>

        <ToggleButton value="OR">
          OR
        </ToggleButton>

      </ToggleButtonGroup>

      <Button
        variant="outlined"
        onClick={addFilter}
      >

        Add Filter

      </Button>

      <Button
        variant="contained"
        onClick={run}
      >

        Run Scanner

      </Button>

    </Stack>

  );

}
