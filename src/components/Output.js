// import {TextField} from '@mui/material';

function Output({outputStr}) {

  return (
    <div
      style={{ 
        display: 'flex', 
        justifyContent: 'center'
      }}
    >
      <div style={{ textAlign: 'left' }}>
        {outputStr.map((line, index) => (
          <p key={index}>{line}</p>
        ))}
      </div>
      {/* TODO: convert string output of turing machine into nice boxes */}
    </div>
  );
}

export default Output;
