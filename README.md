一直忘记查车牌摇号信息，就想着用爬虫直接给我发邮件。一开始使用阿里云配置服务器，但是要掏钱就很烦。

今天来介绍一个不需要花钱就可以实现一些自动化流程的服务。

# 仓库地址

https://github.com/Sunlei012/Spider-CarCard

# Actions是什么

大家知道，持续集成由很多操作组成，比如抓取代码、运行测试、登录远程服务器，发布到第三方服务等等。GitHub 把这些操作就称为 actions。

很多操作在不同项目里面是类似的，完全可以共享。GitHub 注意到了这一点，想出了一个很妙的点子，允许开发者把每个操作写成独立的脚本文件，存放到代码仓库，使得其他开发者可以引用。

如果你需要某个 action，不必自己写复杂的脚本，直接引用他人写好的 action 即可，整个持续集成过程，就变成了一个 actions 的组合。这就是 GitHub Actions 最特别的地方。

GitHub建立了一个market，有很多有意思的Actions可以去引用，包括一些自动发邮件，自动编译等。

# 使用Actions

方法很简单，只需创建一个.github/workflows文件夹，在里面编写一个.yml文件，push到GitHub上就可以在仓库中发现此Actions。

# 编写.yml文件

参考yml格式要求。

## 基本组成

* name: 为你的actions起一个名字吧

~~~yml
  name: 'Spider card card in TianJin'
~~~

* on: 触发方式，最常见的就是push，schedule（定时）
  
~~~yml
  on:
  push:
    branches: 
      - master
  schedule:
    - cron: '0 */1 * * *'
~~~

* jobs: 具体执行workflow的部分，要写出每一项任务的id
  * run-on: 执行任务的环境
  * steps: 每一个步骤的具体执行

~~~yml
jobs:
  Spider-CarCard:
    runs-on: ubuntu-latest
    steps:
      - name: 'Checkout'
        uses: actions/checkout@v2
      - name: 'Set up Python'
        uses: actions/setup-python@v2
        with:
          python-version: 3.7
      - name: 'Install requirements'
        run: pip install -r requirements.txt
      - name: 'Working'
        env:
          APPLYCODE: ${{secrets.APPLYCODE}}
          HOST: ${{secrets.HOST}}
          USERNAME: ${{secrets.USERNAME}}
          PASSWORD: ${{secrets.PASSWORD}}
          RECEIVE_MAIL: ${{secrets.RECEIVE_MAIL}}
        run: python Spider-CarCard.py
~~~

头两个step是引用的market中的actions很便捷。

在Install requirements中我们使用pip安装所需要的库文件（路径以git目录为根路径）。

# 使用加密变量

在working中我使用了五个加密变量使得在程序中需要加密的内容通过GitHub后台传入。

secrets为GitHub定义的类，里面属性的值我们可以在settings中的secrets中定义与赋值（不用带secrets前缀类名）。

在程序中我们也只需要通过使用环境变量的方式获取这些值（依然不用使用secrets前缀类名）

## 引用

* 阮一峰的网络日志--GitHub Actions 入门教程
http://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html

* GitHub Actions官方文档
https://docs.github.com/en/free-pro-team@latest/actions/creating-actions/about-actions#versioning-your-action