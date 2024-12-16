import React, { useState, useEffect } from 'react';
import { Button } from '@mui/material';
import './App.css';
import TMSelection from "./components/TMSelection.js";
import StringInput from "./components/StringInput.js";
import Output from './components/Output.js';

function App() {
  const [selectedTM, setSelectedTM] = useState(null);
  const [tmNames, setTMNames] = useState([]);
  const [tmContents, setTMContents] = useState(null);
  const [inputStr, setInputStr] = useState("");
  const [outputStr, setOutputStr] = useState([]);
  const [outputRes, setOutputRes] = useState("");

  useEffect(() => {
    fetch('/tmNames').then(res => res.json()).then(data => {
      setTMNames(data.tmNames);
    });
  }, []);

  useEffect(() => {
    getTMContents();
  }, [selectedTM]);


  const getTMContents = () => {
    fetch(`/tmContent?tm=${selectedTM}`).then(res => res.json()).then(data => {
      setTMContents({
        "states": data.states.join(', '),
        "alphabet": data.alphabet.join(', '),
        "tape_alphabet": data.tape_alphabet.join(', '),
        "start": data.start,
        "accept": data.accept,
        "reject": data.reject,
        "delta": data.delta
      });
    });
  }

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
        <p>Turing Machine Visual Simulator</p>
        <p className="App-subheader">An Grocki, Lily Jiang</p>
      </header>

      {/* TODO: have visual represnetation of what each turing machine code looks like in python */}
      <p className="Body-header">Step 1: Select a TM to use</p>
      <TMSelection
        tmNames={tmNames}
        selectedTM={selectedTM}
        setSelectedTM={setSelectedTM}
        tmContents={tmContents}
      />

      <p className="Body-header">Step 2: Input a string to parse (can be empty)</p>
      <StringInput inputStr={inputStr} setInputStr={setInputStr} />
      
      <p className="Body-header">Step 3: Run to see the Turing Machine in action</p>
      <Button
        onClick={runMachine}
      >
        Run Machine
      </Button>

      {(outputRes !== "") && 
        <>
          <p className="Body-header">Output</p>
          <Output outputStr={outputStr} />
          <p>
            {outputRes ? 'Result: True' : 'Result: False'}
          </p>
        </>
      }

      <br />
      <br />
      <br />
      <br />
      
    </div>
  );
}

export default App;
