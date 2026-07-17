function Header({ siteName, count }) {

    return (

        <header className="header">

            <h1>{siteName}</h1>

            <h3>Enrolled Courses : {count}</h3>

        </header>

    );

}

export default Header;