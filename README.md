*** UI Vision Automation Script ***

***Tech Stack***
** Python + pycharm + Scipting + Command line + Jenkins + Groovy + Git.

Capability to run mutiple macros in the browser using command line arguments
In current implementation you can pass a list as a parameter, which will contain the name of the macros you want to run.
It can be configured in other ways also like passing folders or html files.

Macros will be fetched from the hard drive, where UI vision root folder is configured by the user, which is also configurable.

All the paths created and used are mostly dynamic in nature will be common for everyone who are using MAC machines.

**Jenkins integration using SCM (Groovy Script)** : 

Project will have a jenkinsFile which can be used for controlling and monitoring the execution flow of script.
***

***Multiple parameters*** :

1. --macro macro1name macro2name macro3name 2. --incognito #(if you want to run browser in incognito mode)#
3. -- headless mode #(to run browser in headless mode)
4. -- userProfile #(to run browser with different profiles)

***How to Run Your Macros On Jenkins***

1. Just Create a new pipiline of type pipeline only.

2. Configure Git repository.

3. Configure Build with Parameter : {MACRO_LIST} : Enter macro names.

4. Build.

***Notes:***

1. For Macro's better execution run use locators such as : ID, testID or Dynamic xpaths. 

2. When providing multiple macro names remember to put a single space between each macro name.

**(You can ask dev team to add the ids or testid in the elements that are required)** 
