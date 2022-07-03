import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'
import logo from './images/logo.png';



const Navbar = () => {


    const [dateState, setDateState] = useState(new Date());
    useEffect(() => {
        setInterval(() => setDateState(new Date()), 30000);
    }, []);
    const welcome = "Hello Shuhrat!"
    return (
        <nav className="navbar">
            <h1>{welcome}</h1>
            {/* <span className="lock"></span> */}
            <div className="links">
                <Link to="/home">Home</Link>
                {/* <Link to="/create">Create</Link> */}
                <Link to="/test">Test</Link>

                <a>
                    {dateState.toLocaleDateString('en-US', {
                        weekday: 'long',
                        month: 'short',
                        day: 'numeric',
                        year: 'numeric',
                    })}
                    {"   "}
                    {dateState.toLocaleString('en-US', {
                        hour: 'numeric',
                        minute: 'numeric',
                        hour12: true,
                    })}
                </a>
                <a>

                </a>



            </div>
            <img src={logo} alt='' />
        </nav>
    );
}

export default Navbar;