import path from 'path';
import HtmlWebpackPlugin from 'html-webpack-plugin';
import HtmlWebpackInlineSourcePlugin from 'html-webpack-inline-source-plugin';
import ScriptExtHtmlWebpackPlugin from 'script-ext-html-webpack-plugin';

const ROOT = path.join(__dirname, '..');

export default {
  entry: path.join(ROOT, 'src/index.js'),
  output: {
    path: path.join(ROOT, 'dist'),
    filename: '[name].bundle.js'
  },
  mode: 'production',
  module: {
    rules: [{
        test: /\.js/,
        exclude: /(node_modules)/,
        use: [{
          loader: 'babel-loader'
        }, ]
      },
      {
        test: /\.(html)$/,
        exclude: /(node_modules)/,
        use: {
          loader: 'html-loader',
          options: {
          }
        }
      },
      {
        test: /\.(png|jp(e*)g|svg)$/,
        exclude: /(node_modules)/,
        use: [{
          loader: 'base64-inline-loader',
          options: {
            // limit: 800000000,
          }
        }]
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      title: 'Custom template',
      template: path.join(ROOT, 'src/index.template.ejs'),
      inlineSource: '.(js|css|png|jp(e*)g|svg)'
    }),
    new HtmlWebpackInlineSourcePlugin(),
    new ScriptExtHtmlWebpackPlugin({
      defaultAttribute: 'defer'
    })
  ],
  stats: {
    colors: true
  },
  devtool: 'source-map'
};