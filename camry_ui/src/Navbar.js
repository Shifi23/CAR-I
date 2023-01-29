import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'


const Navbar = () => {


    const [dateState, setDateState] = useState(new Date());
    const hour = (dateState.getHours())
    useEffect(() => {
        setInterval(() => setDateState(new Date()), 30000);
    }, []);

    const welcome = ((hour >= 22 && "Its Late, Drive Safe") || (hour < 12 && "Good Morning") || (hour < 17 && "Good Afternoon") || (hour < 22 && "Good Evening")) + " Shuhrat"
    const [door, setDoor] = useState("Locked");


    const handleCLick_UL = () => {
        if (door === "Unlocked") {
            setDoor("Locked")

        } else {
            setDoor("Unlocked")
        }


    }

    return (


        <nav className="navbar">
            <h1>{welcome}</h1>

            {/* <span className="lock"></span> */}
            <div className="links">
                <Link to="/home">Home</Link>
                {/* <Link to="/create">Create</Link> */}
                <Link to="/test" >Test-beta</Link>
            </div>



            <h4>
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
            </h4>

            <div className="lockunlock">
                <span onClick={handleCLick_UL} className={door === "Unlocked" ? "lock unlocked" : "lock"}></span>
            </div>



        </nav>
    );
}

export default Navbar;