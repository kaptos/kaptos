const Dotenv = require('dotenv-webpack');

module.exports = {
    entry: [
        './src/index.jsx'
    ],
    node: {
      fs: 'empty'
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            },
            {
              test: /\.css$/,
              use: ['style-loader', 'css-loader']
            },
            {
              test: /\.(woff(2)?|ttf|eot|otf)(\?v=\d+\.\d+\.\d+)?$/,
              loader: 'file-loader'
            },
            {
                test: /\.svg$/,
                loader: 'svg-inline-loader'
            }
        ]
    },
    plugins: [
      new Dotenv()
    ],
    output: {
        path: __dirname + '/kaptos/static/ui/',
        filename: 'kaptos.js',
        publicPath: '/static/ui/'

    },
    resolve: {
      extensions: ['.js', '.jsx']
    },
    optimization: {
        splitChunks: {
          chunks: 'async',
          minSize: 30000,
          maxSize: 0,
          minChunks: 1,
          maxAsyncRequests: 5,
          maxInitialRequests: 3,
          automaticNameDelimiter: '~',
          automaticNameMaxLength: 30,
          name: false,
          cacheGroups: {
            vendors: {
              test: /[\\/]node_modules[\\/]/,
              priority: -10
            },
            default: {
              minChunks: 2,
              priority: -20,
              reuseExistingChunk: true
            }
          }
        }
    },
    watchOptions: {
      ignored: "node_modules/",
      poll: 1000
    }
};
