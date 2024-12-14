import React, { useState, useEffect } from 'react';
import {Radio, RadioGroup, FormControlLabel, FormControl, FormLabel} from '@mui/material';


function GrammarSelection({grammarNames, selectedGrammar, setSelectedGrammar}) {
  const handleChange = (e) => {
    setSelectedGrammar(e.target.value);
  };

  return (
    <div className="App">
      <header className="App-header">
        <FormControl>
          <FormLabel id="demo-radio-buttons-group-label">Choose Grammar</FormLabel>
          <RadioGroup
            aria-labelledby="demo-radio-buttons-group-label"
            // defaultValue="female"
            name="radio-buttons-group"
            value={selectedGrammar}
            onChange={handleChange}
          >
            {grammarNames.map(grammarName => (
              <FormControlLabel
                value={grammarName}
                control={<Radio />}
                label={grammarName}
              />
            ))}
          </RadioGroup>
        </FormControl>
      </header>
    </div>
  );
}

export default GrammarSelection;
