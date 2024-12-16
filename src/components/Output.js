// import {TextField} from '@mui/material';

function Output({outputStr}) {

  const parseString = (str) => {
    return str.map((line) => {
      
      let modifiedLine = line.replace(/ /g, '');
      let newLine = []

      for (let index = 0; index < modifiedLine.length; index++) {
        let char = modifiedLine[index];
        if (char === "[" || char === "]") continue;
        else {
          const isInBrackets = modifiedLine[index - 1] === "[" && modifiedLine[index + 1] === "]";
          const content = isInBrackets ? (
            <span key={index} className="bracketed">{char}</span>
          ) : (
            <span key={index} className="normal">{char}</span>
          );
          newLine.push(content);
        }
      }
      return newLine;
    });
  };

  return (
    <div
      style={{ 
        display: 'flex', 
        justifyContent: 'center'
      }}
    >
      <div style={{ textAlign: 'left', display: 'flex', flexDirection: "column", gap: "3px" }}>
        {parseString(outputStr).map((line, idx) => (
          <div key={idx} style={{display: 'flex', gap: "1px"}}>
            {line}
          </div>
        ))}
      </div>
      {/* TODO: convert string output of turing machine into nice boxes */}
    </div>
  );
}

export default Output;
