import {Link} from 'react-router-dom'

const Navbar = () => {

    const welcome = "Hello Shuhrat!"
    return (
        <nav className="navbar">
            <h1>{welcome}</h1>
            {/* <span className="lock"></span> */}
            <div className="links">
                <Link to ="/">Home</Link>
                {/* <Link to="/create">Create</Link> */}
                <Link to="/test">Test</Link>
                




            </div>
            
        </nav>
    );
}
 
export default Navbar;