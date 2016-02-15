#!/usr/bin/python 
#-*-coding:utf-8
print "你好，世界";
a = 2;
if a == 1:
	print "true";
else :
	print "false";
	
#raw_input("\n\npress the enter key to exit");
a,b,c=1,2,"guohuanwen";
print a,b,c;
print c[2:4]*2;
#list
list = [1,2,"guo",12.34,"huanwen"];
print list;
#元组（不能二次赋值）
tuple = ("and",1,"d");
print tuple;
dictionary = {'guo':"huan","wen":"gu"};
print dictionary;
print dictionary["guo"];
print dictionary.keys();
print dictionary.values