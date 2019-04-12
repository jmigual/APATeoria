import path from 'path';
import HtmlWebpackPlugin from 'html-webpack-plugin';
import HtmlWebpackInlineSourcePlugin from 'html-webpack-inline-source-plugin';
import ScriptExtHtmlWebpackPlugin from 'script-ext-html-webpack-plugin';

const ROOT = path.join(__dirname, '..');

console.log(ROOT);

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
            }]
        }]
    },
    plugins: [
        new HtmlWebpackPlugin({
            title: 'Custom template',
            template: path.join(ROOT, 'src/index.template.ejs'),
            inlineSource: '.(js|css)'
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