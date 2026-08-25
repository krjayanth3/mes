/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './website/**/*.py',
  ],
  theme: {
    extend: {
      colors: {
        mes: {
          maroon: '#800000',
          darkmaroon: '#5c0000',
          lightmaroon: '#a31515',
          gold: '#d4af37',
          lightgold: '#f9e79f',
          navy: '#0f172a',
        },
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        heading: ['Outfit', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
