import React, { useState, useEffect } from 'react';
import {Radio, RadioGroup, FormControlLabel, FormControl, FormLabel} from '@mui/material';


function TMSelection({tmNames, selectedTM, setSelectedTM}) {
  const handleChange = (e) => {
    setSelectedTM(e.target.value);
  };

  return (
    <div className="App">
      <header className="App-header">
        <FormControl>
          <FormLabel id="demo-radio-buttons-group-label">Choose TM</FormLabel>
          <RadioGroup
            aria-labelledby="demo-radio-buttons-group-label"
            // defaultValue="female"
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
