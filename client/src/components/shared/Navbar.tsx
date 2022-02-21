import { useContext, useState } from 'react';
import { Link } from 'react-router-dom';
import { useHistory } from 'react-router-dom';
import AuthContext from '../../context/auth-context';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import { NavLinks } from '../../data/Navbar';
import NavBurger from '../../utils/icons/NavBurger';

const Navbar = () => {
  const authCtx = useContext(AuthContext);
  const isLoggedIn = authCtx.isLoggedIn;
  const history = useHistory();

  const logoutHandler = () => {
    toast.success('Logout Successful');
    authCtx.logout();
    history.replace('/');
  };

  const [navbarOpen, setNavbarOpen] = useState<boolean>(false);
  return (
    <div>
      <nav className="relative flex flex-wrap items-center justify-between px-2 py-3 bg-blue-400">
        <div className="container px-4 mx-auto flex flex-wrap items-center justify-between">
          <div className="w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start">
            <Link
              className="text-xl font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase text-white"
              to="/"
            >
              VR1 Music App
            </Link>
            <button
              className="text-white cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none"
              type="button"
              onClick={() => setNavbarOpen(!navbarOpen)}
            >
              <NavBurger />
            </button>
          </div>
          <div
            className={
              'lg:flex flex-grow items-center' +
              (navbarOpen ? ' flex' : ' hidden')
            }
            id="example-navbar-danger"
          >
            <ul className="flex flex-col lg:flex-row list-none lg:ml-auto">
              {NavLinks.map((item) => (
                <li key={item.link}>
                  <Link
                    className="px-3 py-2 flex items-center text-lg font-bold leading-snug text-white hover:opacity-75 transform transition hover:scale-110"
                    to={item.link}
                  >
                    <i className="fab fa-facebook-square text-lg leading-lg text-white opacity-75"></i>
                    <span className="ml-2">{item.label}</span>
                  </Link>
                </li>
              ))}
              {!isLoggedIn && (
                <li>
                  <Link
                    className="px-3 py-2 flex items-center text-lg font-bold leading-snug text-white hover:opacity-75 transform transition hover:scale-110"
                    to="/auth"
                  >
                    <i className="fab fa-facebook-square text-lg leading-lg text-white opacity-75"></i>
                    <span className="ml-2">Login</span>
                  </Link>
                </li>
              )}
              {isLoggedIn && (
                <li>
                  <Link
                    className="px-3 py-2 flex items-center text-lg font-bold leading-snug text-white hover:opacity-75 transform transition hover:scale-110"
                    to="/record"
                  >
                    <i className="fab fa-facebook-square text-lg leading-lg text-white opacity-75"></i>
                    <span className="ml-2">Record</span>
                  </Link>
                </li>
              )}
              {isLoggedIn && (
                <li>
                  <Link
                    className="px-3 py-2 flex items-center text-lg font-bold leading-snug text-white hover:opacity-75 transform transition hover:scale-110"
                    to="/profile"
                  >
                    <i className="fab fa-facebook-square text-lg leading-lg text-white opacity-75"></i>
                    <span className="ml-2">Profile</span>
                  </Link>
                </li>
              )}

              {isLoggedIn && (
                <li className="flex bg-blue-500 text-white px-2 rounded-lg hover:bg-blue-600 focus:outline-none">
                  <button onClick={logoutHandler}>Logout</button>
                </li>
              )}
            </ul>
          </div>
        </div>
      </nav>
      <ToastContainer />
    </div>
  );
};

export default Navbar;
