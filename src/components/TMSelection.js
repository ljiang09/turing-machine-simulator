import React, { useState } from 'react';
import {Radio, RadioGroup, FormControlLabel, FormControl, Button} from '@mui/material';


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
        {/* {(tmContents !== null && selectedTM !== null) && 
          <div className="content-column-content">
            {Object.entries(tmContents).map(([key, value]) => (
              <>
                {key === "delta" ? 
                  <>
                    <p className='Body-subheader'>{key}</p>
                    <div className="three-col-container">
                      {value.map((item, index) => (
                        <div key={index} className="three-col-item">
                          ({item.join(", ")})
                        </div>
                      ))}
                    </div>
                  </>
                :
                  <>
                    <p className='Body-subheader'>{key}</p>
                    <p className="three-col-item">{value}</p>
                  </>
                }
                
              </>
            ))}
          </div>
        } */}
        {(tmRepresentation !== null && selectedTM !== null) && 
          <div className="content-column-content">
            <p className='Body-subheader'>Content</p>
            <p className="three-col-item">{tmRepresentation["tmContent"]}</p>
            <p className='Body-subheader'>Example Strings</p>
            <p className="three-col-item">{tmRepresentation["tmExample"]}</p>
            {/* {(tmContents !== null) && 
              <Button onClick={setOpen(!open)}>{(open === true) ? "See Encoding" : "Hide Encoding"}</Button>
            } */}
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
