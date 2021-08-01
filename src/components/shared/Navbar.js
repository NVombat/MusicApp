import { useState } from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  const [navbarOpen, setNavbarOpen] = useState(false);
  return (
    <>
      <nav className='relative flex flex-wrap items-center justify-between px-2 py-3 bg-pink-500 mb-3'>
        <div className='container px-4 mx-auto flex flex-wrap items-center justify-between'>
          <div className='w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start'>
            <Link
              className='text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase text-white'
              to='/'>
              Music App
            </Link>
            <button
              className='text-white cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none'
              type='button'
              onClick={() => setNavbarOpen(!navbarOpen)}>
              <i className='fas fa-bars'></i>
            </button>
          </div>
          <div
            className={
              'lg:flex flex-grow items-center' +
              (navbarOpen ? ' flex' : ' hidden')
            }
            id='example-navbar-danger'>
            <ul className='flex flex-col lg:flex-row list-none lg:ml-auto'>
              <li className='nav-item'>
                <Link
                  className='px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-white hover:opacity-75'
                  to='/auth'>
                  <span className='ml-2'>Login</span>
                </Link>
              </li>
              <li className='nav-item'>
                <Link
                  className='px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-white hover:opacity-75'
                  to='/profile'>
                  <span className='ml-2'>Profile</span>
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </>
  );
};

export default Navbar;
