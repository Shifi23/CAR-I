// import './App.css';
import Navbar from './Navbar';
import Home from './Home';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Create from './Create';
import Test from './Test';
import styled, { ThemeProvider } from "styled-components";
import { lightTheme, darkTheme, GlobalStyles } from "./themes.js";
import { useState } from "react"
import { CgSun } from "react-icons/cg";
import { HiMoon } from "react-icons/hi";


const StyledApp = styled.div`
  color: ${(props) => props.theme.fontColor};
  background-color: ${props => props.theme.body};

`;
const Toggle = styled.button`
    height: 50px;
    width: 50px;
    position: absolute;
    top: 20px;
    right: 20px; 
    border-radius: 50%;
    border: none;
    background-color: ${props => props.theme.body};
    color: ${props => props.theme.fontColor};
    &:focus {
        outline: none;
    }

`;

function App() {
  const [theme, setTheme] = useState("light");

  function themeToggler() {
    theme === "light" ? setTheme("dark") : setTheme("light");

  };


  const icon = theme === "light" ? <HiMoon size={35} /> : <CgSun size={35} />;
  return (

    <Router>
      <ThemeProvider theme={theme === "light" ? lightTheme : darkTheme}>
        <h4 style={{ color: "#fdba00", position: 'absolute', top: '20px', left: '45%' }}>Proceed with Caution!</h4>
        <GlobalStyles />
        <StyledApp className="App" >
          <Toggle onClick={themeToggler}>
            {icon}</Toggle>
          <Navbar></Navbar>
          <div className="content">
            <Switch>
              <Route exact path="/home">
                <Home />
              </Route>
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
        </StyledApp>

      </ThemeProvider>

    </Router>
  );
}

export default App;
