import {Link} from 'react-router-dom'

const Navbar = () => {
    return (
        <nav className="navbar">
            <h1>Shuhrat's Toyota Camry</h1>
            <div className="links">
                <Link to ="/">Home</Link>
                <Link to="/create">Create</Link>
                <Link to="/test">Test</Link>

            </div>
        </nav>
    );
}
 
export default Navbar;