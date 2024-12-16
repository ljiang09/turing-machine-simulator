import {Radio, RadioGroup, FormControlLabel, FormControl} from '@mui/material';


function TMSelection({tmNames, selectedTM, setSelectedTM, tmContents}) {
  const handleChange = (e) => {
    setSelectedTM(e.target.value);
  };

  return (
    <div className="container">
      <div className="form-column">
        <FormControl>
          <RadioGroup
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
      </div>

      <div class="vl"></div>

      <div className="content-column">
        {(tmContents !== null && selectedTM !== null) && 
          <div className="content-column-content">
            {Object.entries(tmContents).map(([key, value]) => (
              <>
                <p className='Body-subheader'>{key}</p>
                <p>{value}</p>
              </>
            ))}
          </div>
        }
        {(tmContents === null || selectedTM === null) && 
          <div className="content-column-content">
            <p>Select a Turing Machine to see its details here.</p>
          </div>
        }
      </div>
    </div>
  );
}

export default TMSelection;
