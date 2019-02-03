---
title: web渗透测试（黑盒）
date: 2018-11-20 14:17:46
tags:
---
## banner识别 ##

先谈几个工具：
- 云悉：http://www.yunsee.cn/ 很适合国内环境，CMS指纹识别很好。
- wappalyzer：https://www.wappalyzer.com/ 国际通用的识别工具，有浏览器插件，很方便。
- Fofa，shodan（偏向网络设备路由摄像头等），Zoomeye（偏向web）这些网络空间搜索器也很好用。
- whatweb：https://github.com/urbanadventurer/WhatWeb 很强大，kali自带，但对国内CMS识别不是很合适。
- CMSeeK：https://github.com/Tuhinshubhra/CMSeeK 集成了cms的poc，持续有更新，很适合 WordPress, Joomla, Drupal。

一般情况下，能够使用以上工具能获得信息的说明本身对banner信息就并没有做很多的隐藏，如果本身做了隐藏的，就要通过经验来获取更多的信息来做判断。

比如利用404界面判断，再比如利用目录字典扫描像wordpress里面的readme.html

例如简单的有服务器信息的，IIS→.NET，apacheHTTP→php，java系列的就不必多说。

### PHP ###

php大多都是使用各种CMS，在这里稍微总结一下所知的常见cms的特殊识别经验以及敏感后台目录。

- 基于ThinkPHP的CMS

[[漏洞分析]thinkphp 5.x全版本任意代码执行分析全记录](https://xz.aliyun.com/t/3570)
通用测试链接：http://TargetHost/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1

- Wordpress

css文件，根目录下的`readme.html`，后台登录`/wp-login.php`，路径目录`/wp-includes`、`/wp-content`。`/xmlrpc.php`如果开启了xmlrpc的服务，可以利用来进行批量爆破。
![](1.jpg)
推荐使用**wpscan**，一个专门针对wordpress的扫描器。

- Discuz！

国内的中小型论坛基本上大部分都是discuz，首先默认模版很明显首页路径`/portal.php`，后台登录路径为`/admin.php`，`/api/uc.php`也是一个特征目录。


- dedecms（织梦）

