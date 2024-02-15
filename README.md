*** UI Vision automation script is written in python, 

Capability to run mutiple macros in the browser using command line arguments, it takes a argument as a list named as 
--macro in which so you can provide multiple macroname with spaces, can use multiple arguments as per requirement.

Macros will be feched from hard drive, it is configurable.

All the paths created and  used are mostly dynamic in nature will be common for everyone using MAC machines.

**Jenkins integration using SCM (Groovy Script)** : 
Project will have a jenkinsFile which can be used for controlling and monitoring the execution flow of macros.
***

**Tech Stack**
** Python + pycharm + Scipting + Command line + Run Multiple Macros + Jenkins + Groovy.

**Command line argument**
** --macro macro1name macro2name macro3name --incognito #(if you want to run browser in incognito mode)#

**How to Run Your Macros On Jenkins**

1.Just Create a new pipiline of type pipeline only.

2.Configure Git repository.

3.Configure Build with Parameter : {MACRO_LIST} : Enter the macros names, put single space in between the names of multiple macros. 

**(Can also be done for a testSuiteFolder for that we can seperate the test cases in different folders LOB wise)**

4.Build.

**Note:**

1.For Macro's better execution run use locators such as : ID, testID or Dynamic xpaths. 

**(You can ask dev team to add the ids or testid in the elements that are required)** 






