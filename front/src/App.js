import logo from './logo.svg';
import React from 'react';
import axios from 'axios';
import './App.css';

const baseURL = 'http://127.0.0.1:3030'

function App() {
  const axios_POST = (testName) => {
    axios.post(baseURL, {
        'request': {
            'name': testName,
            'date': new Date(),
            'format': 'xml'
        },
        'request_type': 'auto_test'
    })
    .then(function (response) {
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error.message);
    });
  };
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <button onClick={() => axios_POST('test_01')}>CLICK_1</button>
        <button onClick={() => axios_POST('test_02')}>CLICK_2</button>
        <button onClick={() => axios_POST('test_error')}>CLICK_test_error</button>
      </header>
    </div>
  );
}

export default App;
