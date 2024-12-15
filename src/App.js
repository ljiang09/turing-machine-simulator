import React, { useState, useEffect } from 'react';
import './App.css';
import TMSelection from "./components/TMSelection.js";
import StringInput from "./components/StringInput.js";

function App() {
  const [selectedTM, setSelectedTM] = useState(null);
  const [tmNames, setTMNames] = useState([]);
  const [tmContents, setTMContents] = useState([]);
  const [inputStr, setInputStr] = useState("");

  useEffect(() => {
    fetch('/tmNames').then(res => res.json()).then(data => {
      setTMNames(data.tmNames);
      setTMContents(data.tmContents);
    });
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        {/* TODO: ideally we show the TM string contents */}
        {/* tmContents[selectedTM] */}
        <p>Selected TM: {selectedTM}</p>
        <TMSelection
          tmNames={tmNames}
          selectedTM={selectedTM}
          setSelectedTM={setSelectedTM}
        />
        <StringInput inputStr={inputStr} setInputStr={setInputStr} />
      </header>
    </div>
  );
}

export default App;
