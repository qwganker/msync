# msync 多网站博客同步编辑工具  QQ交流: 448081525

1. 支持一键发布博客到多个平台(简书/csdn/今日头条/掘金)
2. 本地管理多平台文章, 支持更新发布和删除功能

### 效果
- 文章发布
![](/img/msync-1.png)

- 文章管理
![](/img/msync-2.png)


### 安装依赖
python 3.9.1

1. 后台
```bash
pip3 install -r requirements.txt
```

2. 前端
```bash
npm install
```

3. 打包运行
```bash
/bin/bash build_run.sh
```

4. 本地访问
```
http://127.0.0.1:8000/
```

### 注意事项
1. 目前只支持 firefox 浏览器
2. 简书/csdn/今日头条/掘金网站需求以前通过firefox登录过, 因为msync需要使用firefox的cookies

### Release
##### v1.0.0 (2021.1.18) 第一版发布
