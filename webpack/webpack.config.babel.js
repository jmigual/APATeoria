import path from 'path';
import webpack from 'webpack';

import HtmlWebpackPlugin from 'html-webpack-plugin';
import HtmlWebpackInlineSourcePlugin from 'html-webpack-inline-source-plugin';
import ScriptExtHtmlWebpackPlugin from 'script-ext-html-webpack-plugin';

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
          parallel: true,
        }),
        new OptimizeCSSAssetsPlugin({

        })],
    },
    mode: 'development',
    module: {
      rules: [{
          test: /\.js/,
          exclude: /(node_modules)/,
          use: [{
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env'],
              // plugins: ['@babel/plugin-transform-runtime']
            }
          }, 
        ]
        },
        {
          test: /\.(html)$/,
          exclude: /(node_modules)/,
          use: {
            loader: 'html-loader',
            options: {}
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
        title: env.title,
        template: path.join(ROOT, 'src/index.template.ejs'),
        inlineSource: '.(js|css)',
      }),
      new HtmlWebpackInlineSourcePlugin(),
      new ScriptExtHtmlWebpackPlugin({
        defaultAttribute: 'defer'
      }),
      new MiniCssExtractPlugin({
        filename: '[name].css',
        chunkFilename: '[id].css',
      }),
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
      port: 8080,
    }
  }
};