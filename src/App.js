import React, { useState, useEffect } from 'react';
import { Button } from '@mui/material';
import './App.css';
import TMSelection from "./components/TMSelection.js";
import StringInput from "./components/StringInput.js";

function App() {
  const [selectedTM, setSelectedTM] = useState(null);
  const [tmNames, setTMNames] = useState([]);
  const [tmContents, setTMContents] = useState([]);
  const [inputStr, setInputStr] = useState("");
  const [outputStr, setOutputStr] = useState([]);
  const [outputRes, setOutputRes] = useState("");

  useEffect(() => {
    fetch('/tmNames').then(res => res.json()).then(data => {
      setTMNames(data.tmNames);
      setTMContents(data.tmContents);
    });
  }, []);

  const runMachine = () => {
    const encodedTM = encodeURIComponent(selectedTM);
    const encodedInputStr = encodeURIComponent(inputStr);
    fetch(`/runMachine?tm=${encodedTM}&inputStr=${encodedInputStr}`).then(res => res.json()).then(data => {
      setOutputRes(data.result);
      setOutputStr(data.steps.split('\n'));
    });
  }


  return (
    <div className="App">
      <header className="App-header">
        {/* TODO: ideally we show the TM string contents */}
        {/* or the format it should be in */}
        {/* tmContents[selectedTM] */}
        <p>Selected TM: {selectedTM}</p>
        <TMSelection
          tmNames={tmNames}
          selectedTM={selectedTM}
          setSelectedTM={setSelectedTM}
        />
        <StringInput inputStr={inputStr} setInputStr={setInputStr} />
      </header>
      <Button
        onClick={runMachine}
      >
        Run Machine
      </Button>

      <div>
        {outputStr.map((line, index) => (
          <p key={index}>{line}</p>
        ))}
      </div>
      <p>
        {outputRes}
      </p>
      
    </div>
  );
}

export default App;
