import React, { useState, useEffect } from 'react';
import './App.css';
import GrammarSelection from "./components/GrammarSelection.js";

function App() {
  const [selectedGrammar, setSelectedGrammar] = useState(null);
  const [grammarNames, setGrammarNames] = useState([]);
  const [grammarContents, setGrammarContents] = useState([]);

  useEffect(() => {
    fetch('/grammarNames').then(res => res.json()).then(data => {
      setGrammarNames(data.grammarNames);
      setGrammarContents(data.grammarContents);
      console.log(data.grammarContents)
    });
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        <p>
          TURING MACHINE HERE
        </p>
        {/* TODO: ideally we show the grammar contents */}
        {/* grammarContents[selectedGrammar] */}
        <p>Selected grammar: {JSON.stringify(grammarContents)}</p>
        <GrammarSelection
          grammarNames={grammarNames}
          selectedGrammar={selectedGrammar}
          setSelectedGrammar={setSelectedGrammar}
        />
      </header>
    </div>
  );
}

export default App;
