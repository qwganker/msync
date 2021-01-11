module.exports = {
    // chainWebpack: config => {
    //   config.plugin("define").tap(args => {
    //     args[0]["process.env"].BASE_URL = JSON.stringify(process.env.BASE_URL);
    //     return args;
    //   });
    // },
    assetsDir: 'static',
    // outputDir:'dist'
    // indexPath: 'static/public/index.html'
    publicPath: './', 
    devServer: {
      proxy: {
        '/v1': {
          target: 'http://127.0.0.1:8000',
          changeOrigin: true,
        }
      }
    },
};