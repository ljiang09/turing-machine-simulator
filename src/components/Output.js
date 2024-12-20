import React, { useState, useEffect } from 'react';
import {ToggleButtonGroup, ToggleButton} from '@mui/material';

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

  var parsedString = parseString(outputStr).slice(0, -1);  // remove last element since the python function prints out a blank line
  const maxLength = Math.max(...parsedString.map(arr => arr.length));

  // pad smaller subarrays so the output HTML isn't jagged
  parsedString = parsedString.map(arr => {
    const padding = Array(maxLength - arr.length).fill(null).map((_, index) => (
      <span key={`padding-${index}`} className="blank">{' '}</span>
    ));
    return arr.concat(padding);
  });

  const [displayType, setDisplayType] = useState(true);
  const [frame, setFrame] = useState(0);

  // for the animated output, change the frame every second
  useEffect(() => {
    if (displayType === false) {
      const interval = setInterval(() => {
        setFrame((prev) => {
          if (prev >= parsedString.length - 1) {
            prev = 0
            return prev
          }
          return prev + 1;
        });
      }, 1000);

      return () => clearInterval(interval);
    } else {
      setFrame(0);
    }
  }, [displayType]);

  return (
    <div
      style={{ 
        display: 'flex', 
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center'
      }}
    >
      <ToggleButtonGroup
        value={displayType}
        exclusive
        onChange={() => setDisplayType(!displayType)}
        style={{paddingBottom: "20px"}}
      >
        <ToggleButton value={true} style={{ height: "40px", textTransform: "none" }}>
          <p>Animated</p>
        </ToggleButton>
        <ToggleButton value={false} style={{ height: "40px", textTransform: "none" }}>
          <p>Step-by-step</p>
        </ToggleButton>
      </ToggleButtonGroup>

      {displayType ? 
        <div style={{ textAlign: 'left', display: 'flex', flexDirection: "column", gap: "3px" }}>
          {parsedString.map((line, idx) => (
            <div key={idx} style={{display: 'flex', gap: "1px"}}>
              <div key={idx} style={{width: "30px"}}>
                {idx}
              </div>
              {line}
            </div>
          ))}
        </div>
        :
        <div
          style={{
            display: 'flex',
            flexDirection: "column",
            justifyContent: "center",
            gap: "3px"
          }}
        >
          <div>Step {frame}</div>
          <div
            style={{
              display: 'flex',
              justifyContent: "center",
              gap: "1px"
            }}
          >
            {parsedString[frame]}
          </div>
        </div>
      }
    </div>
  );
}

export default Output;
