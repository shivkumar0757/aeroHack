import './App.css';
import React, {useState} from "react";

function App() {
  const base_url= 'http://localhost:8000';
  const[data,setData] = useState('localData');
  const[status,setStatus] = useState('Click to check status');

  async  function fetchData()
  {
    var resp;
    try {
          console.log('fetch data triggered');
          resp= await fetch(base_url+'/ping');
          console.log(resp.status)
          
          if (resp.status === 200)
          {
            setStatus('Application is running.');
            fetch(base_url+'/').then((res) => res.text())
            .then((json) => {
            //console.log(json);
            setData(json);
            });
          }
          else   setStatus('unable to get data');  
    } catch (err) {
      console.log(err);
      setStatus('unable to get data: Error occures.');
    }
  }


  return (
    <div className="App">
      
      {data}
      <br/><br/>
<p>
<button onClick={fetchData}>Check Status</button>
    <br/>  {status}
</p>
      

    </div>
  );
}

export default App;
