import path from 'path';

import HtmlWebpackPlugin from 'html-webpack-plugin';
import HtmlWebpackInlineSourcePlugin from 'html-webpack-inline-source-plugin';

import MiniCssExtractPlugin from 'mini-css-extract-plugin';
import TerserJSPlugin from 'terser-webpack-plugin';
import OptimizeCSSAssetsPlugin from 'optimize-css-assets-webpack-plugin';

const ROOT = path.join(__dirname, '..');
const DIST = path.join(ROOT, 'dist');

export default function (env) {
  return {
    entry: path.join(ROOT, 'src/index.js'),
    output: {
      path: DIST,
    },
    optimization: {
      minimize: true,
      mergeDuplicateChunks: true,
      usedExports: true,
      minimizer: [
        new TerserJSPlugin({
          parallel: 4,
          cache: true
        }),
        new OptimizeCSSAssetsPlugin({

        })
      ],
    },
    mode: 'development',
    module: {
      rules: [{
          test: /\.js/,
          include: path.resolve(ROOT, 'src'),
          exclude: /(node_modules)/,
          use: [{
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env'],
              // plugins: ['@babel/plugin-transform-runtime']
            }
          }, ]
        },
        {
          test: /\.(html)$/,
          include: [path.resolve(ROOT, 'src'), path.resolve(ROOT, 'dist')],
          exclude: /(node_modules)/,
          use: {
            loader: 'html-loader',
            options: {
              url: false
            }
          }
        },
        {
          test: /\.(png|jp(e*)g|svg|woff(2?)|ttf|eot|svg)$/,
          use: [{
            loader: 'base64-inline-loader',
          }]
        },
        {
          test: /\.(s?)css$/,
          use: [
            MiniCssExtractPlugin.loader, // creates style nodes from JS strings
            "css-loader", // translates CSS into CommonJS
            "sass-loader" // compiles Sass to CSS, using Node Sass by default
          ]
        }
      ]
    },
    plugins: [
      new HtmlWebpackPlugin({
        template: path.join(DIST, 'pandoc.html'),
        inlineSource: '.(js|css)'
      }),
      new HtmlWebpackInlineSourcePlugin(),
      new MiniCssExtractPlugin({
        filename: '[name].css',
        chunkFilename: '[id].css',
      })
    ],
    stats: {
      colors: true
    },
    performance: {
      hints: false
    },
    // devtool: 'source-map',
    devServer: {
      contentBase: DIST,
      compress: true,
      index: 'index.html',
      inline: true,
      open: true,
      host: "0.0.0.0",
      port: 8080,
    }
  }
};