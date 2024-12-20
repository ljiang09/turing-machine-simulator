import {TextField} from '@mui/material';

// Component that takes in user string input
function StringInput({inputStr, setInputStr}) {
  return (
    <div>
      <header>
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
