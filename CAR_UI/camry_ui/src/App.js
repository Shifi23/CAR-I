// import './App.css';
import Navbar from './Navbar';
import Home from './Home';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Create from './Create';
import Test from './Test';
function App() {
  // const title = 'Hi shuhrat';

  return (
    <Router>
      <div className="App">
        <Navbar></Navbar>
        <div className="content">
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route path="/create">
              <Create />
            </Route>
            <Route path='/test'>
              <Test />
            </Route>


          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
