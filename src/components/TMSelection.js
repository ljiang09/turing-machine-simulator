import {Radio, RadioGroup, FormControlLabel, FormControl} from '@mui/material';


// Component for selecting TM
function TMSelection({tmNames, selectedTM, setSelectedTM, tmContents, tmRepresentation}) {
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
        {(tmRepresentation !== null && selectedTM !== null) && 
          <div className="content-column-content">
            <p className='Body-subheader'>Content</p>
            <p className="three-col-item">{tmRepresentation["tmContent"]}</p>
            <p className='Body-subheader'>Example Strings</p>
            <p className="three-col-item">{tmRepresentation["tmExample"]}</p>
          </div>
        }
        {(tmRepresentation === null || selectedTM === null) && 
          <div className="content-column-content">
            <p>Select a Turing Machine to see its details here.</p>
          </div>
        }
      </div>
    </div>
  );
}

export default TMSelection;
