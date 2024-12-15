import {TextField} from '@mui/material';

function StringInput({inputStr, setInputStr}) {

  return (
    <div className="App">
      <header className="App-header">
        <TextField
          value={inputStr}
          label="Enter your string"
          onChange={(e) => {
            setInputStr(e.target.value);
          }}
          variant="outlined"
        />
      </header>
    </div>
  );
}

export default StringInput;
