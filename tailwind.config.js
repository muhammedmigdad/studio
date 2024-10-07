// tailwind.config.js
module.exports = {
    content: [
      './templates/**/*.html',
      './static/**/*.js',
    ],
    theme: {
      extend: {
        colors: {
          // Custom colors
          lightBeige: '#ebc6a1',
          darkGray: '#2D2D2D',
          lightGray: '#F4F4F4',
          buttonBg: '#E9E1D9',
        },
      },
    },
    plugins: [],
  }
  