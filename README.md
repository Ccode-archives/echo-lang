# echo-lang
A custom shell language made for educational purposes only.
# how to run a script
As of now you need to run
```bash
cat filename.ech | python3 lang.py -c
```
# How to use
## set var
```
test:=1
```
### call variable
```
test:=exit
test2:=hello world
print test2$
test$
```
The code above when typed in will print "hello world" then exit the program.
## currect working directory
```
pwd
```
## change directory
```
cd directory-name
```
## change directory to HOM
```
cd 
```
## list directories and files
```
ls
```
## list directories and files in path
```
ls /path
```
## print
```
print test
```
## calculate math
```
calc 5+3
```
## exit
```
exit
```
