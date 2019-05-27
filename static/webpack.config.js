var webpack = require('webpack');  
module.exports = {  
  entry: [
    "./js/index.jsx"
  ],
  output: {
    path: __dirname + '/static',
    filename: "bundle.js"
  },
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        },
        
        exclude: /node_modules/
      }
    ]
  },
  plugins: [
  ]
};