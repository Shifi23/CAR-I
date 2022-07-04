import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'
import logo from './images/logo.png';
import { lightTheme, darkTheme, GlobalStyles } from "./themes.js";
import styled, { ThemeProvider } from "styled-components";

const Navbar = () => {


    const [dateState, setDateState] = useState(new Date());
    const hour = (dateState.getHours())
    useEffect(() => {
        setInterval(() => setDateState(new Date()), 30000);
    }, []);

    const welcome = ((hour >= 22 && "Its Late, Drive Safe") || (hour < 12 && "Good Morning") || (hour < 17 && "Good Afternoon") || (hour < 22 && "Good Evening")) + " Shuhrat"
    const [door, setDoor] = useState("Locked");

    return (


        <nav className="navbar">
            <h1>{welcome}</h1>

            {/* <span className="lock"></span> */}
            <div className="links">
                <Link to="/home">Home</Link>
                {/* <Link to="/create">Create</Link> */}
                <Link to="/test" >Test-beta</Link>
            </div>

            <a>
                {dateState.toLocaleDateString('en-US', {
                    weekday: 'long',
                    month: 'short',
                    day: 'numeric',
                    year: 'numeric',
                })}
                &nbsp;&nbsp;&nbsp;&nbsp;
                {dateState.toLocaleString('en-US', {
                    hour: 'numeric',
                    minute: 'numeric',
                    hour12: true,
                })}
                &nbsp;&nbsp;&nbsp;&nbsp;
            </a>

            <div className="lockunlock">
                <span className={door === "Unlocked" ? "lock unlocked" : "lock"}></span>
            </div>

        </nav>
    );
}

export default Navbar;