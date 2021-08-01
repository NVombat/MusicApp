module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false,
  theme: {
    extend: {
      fontFamily: {
        montserrat: ['"Montserrat"', 'sans-serif'],
      },
    },
    screens: {
      xs: '360px',
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
