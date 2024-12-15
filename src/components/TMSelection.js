import {Radio, RadioGroup, FormControlLabel, FormControl, FormLabel} from '@mui/material';


function TMSelection({tmNames, selectedTM, setSelectedTM}) {
  const handleChange = (e) => {
    setSelectedTM(e.target.value);
  };

  return (
    <div>
      <header>
        <FormControl>
          <FormLabel>Choose TM</FormLabel>
          <RadioGroup
            aria-labelledby="demo-radio-buttons-group-label"
            name="radio-buttons-group"
            value={selectedTM}
            onChange={handleChange}
          >
            {tmNames.map(tmName => (
              <FormControlLabel
                value={tmName}
                control={<Radio />}
                label={tmName}
              />
            ))}
          </RadioGroup>
        </FormControl>
      </header>
    </div>
  );
}

export default TMSelection;
