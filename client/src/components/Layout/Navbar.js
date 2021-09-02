import React from 'react';
import { Link } from 'react-router-dom';

import BurgerButton from '../../utils/icons/BurgerButton';

const NavLinks = [
  {
    label: 'Home',
    link: '/',
  },
  {
    label: 'About Us',
    link: '/about',
  },
  {
    label: 'Song Tracks',
    link: '/song-tracks',
  },
  {
    label: 'Song Book',
    link: '/song-book',
  },
  {
    label: 'Sing',
    link: '/sing',
  },
];

export default function Navbar({ fixed }) {
  const [navbarOpen, setNavbarOpen] = React.useState(false);
  return (
    <>
      <nav className='relative flex flex-wrap items-center justify-between px-2 py-3 bg-yellow-500 mb-3'>
        <div className='container px-4 mx-auto flex flex-wrap items-center justify-between'>
          <div className='w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start'>
            <Link
              className='text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase text-black'
              to='/'>
              JVT
            </Link>
            <button
              className='text-black cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none'
              type='button'
              onClick={() => setNavbarOpen(!navbarOpen)}>
              <BurgerButton />
            </button>
          </div>
          <div
            className={
              'lg:flex flex-grow items-center' +
              (navbarOpen ? ' flex' : ' hidden')
            }
            id='example-navbar-danger'>
            <ul className='flex flex-col lg:flex-row list-none lg:ml-auto'>
              {NavLinks.map((navlink) => (
                <li className='nav-item'>
                  <Link
                    className='px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-black hover:opacity-75'
                    to={navlink.link}>
                    <i className='fab fa-facebook-square text-lg leading-lg text-black opacity-75'></i>
                    <span className='ml-2 '>{navlink.label}</span>
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </nav>
    </>
  );
}
