# 0x04. AirBnB clone - Web framework
### `Python` `Back-end` `Webserver` `Flask`
## Resources
**Read or watch**:

* [What is a Web Framework?](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)
* [A Minimal Application](https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application)
* [Routing](https://flask.palletsprojects.com/en/1.0.x/quickstart/#routing) (*except “HTTP Methods”*)
* [Rendering Templates](https://flask.palletsprojects.com/en/1.0.x/quickstart/#rendering-templates)
* [Synopsis](https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis)
* [Variables](https://jinja.palletsprojects.com/en/2.9.x/templates/#variables)
* [Comments](https://jinja.palletsprojects.com/en/2.9.x/templates/#comments)
* [Whitespace Control](https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control)
* [List of Control Structures](https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures) (*read up to “Call”*)
* [Flask](https://palletsprojects.com/p/flask/)
* [Jinja](https://jinja.palletsprojects.com/en/2.9.x/templates/)
### General
* What is a Web Framework
* How to build a web framework with Flask
* How to define routes in Flask
* What is a route
* How to handle variables in a route
* What is a template
* How to create a HTML response in Flask by using a template
* How to create a dynamic template (loops, conditions…)
* How to display in HTML data from a MySQL database

## Requirements
## Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version `3.4.3`)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `PEP 8` style (version `1.7`)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## HTML/CSS Files
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* A `README.md` file at the root of the folder of the project is mandatory
* Your code should be W3C compliant and validate with [W3C-Validator](https://github.com/alx-tools/W3C-Validator) (except for jinja template)
* All your CSS files should be in the `styles` folder
* All your images should be in the `images` folder
* You are not allowed to use `!important` or `id` (`#...` in the CSS file)
* All tags must be in uppercase
* Current screenshots have been done on `Chrome 56.0.2924.87`.
* No cross browsers

# More Info

### Install Flask
```
$ pip3 install Flask
```

![hbnb_step3](https://github.com/samuelselasi/AirBnB_clone_v2/assets/85158665/70218b47-7782-4171-bf31-424d3d606688)

## Tasks

[0. Hello Flask!](./0-hello_route.py)

Write a script that starts a Flask web application:

* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
	* `/`: display “`Hello HBNB!`”
* You must use the option `strict_slashes=False` in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$
```

[1. HBNB](./1-hbnb_route.py)

Write a script that starts a Flask web application:

* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
        * `/`: display “`Hello HBNB!`”
	* `/hbnb`: display “HBNB”
* You must use the option `strict_slashes=False` in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$
```

[2. C is fun!](./2-c_route.py)

Write a script that starts a Flask web application:

* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
        * `/`: display “`Hello HBNB!`”
        * `/hbnb`: display “HBNB”
	* `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
* You must use the option `strict_slashes=False` in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
```

[3. Python is cool!](./3-python_route.py)

Write a script that starts a Flask web application:

* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
        * `/`: display “`Hello HBNB!`”
        * `/hbnb`: display “HBNB”
        * `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
	* `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
		* The default value of `text` is “is cool”
* You must use the option `strict_slashes=False` in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$
```

[4. Is it a number?](./4-number_route.py)

Write a script that starts a Flask web application:

* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
        * `/`: display “`Hello HBNB!`”
        * `/hbnb`: display “HBNB”
        * `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
        * `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
                * The default value of `text` is “is cool”
	* `/number/<n>`: display “`n` is a number” only if `n` is an integer
* You must use the option `strict_slashes=False` in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
```

[5. Number template](./5-number_template.py)

Write a script that starts a Flask web application:

* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
        * `/`: display “`Hello HBNB!`”
        * `/hbnb`: display “HBNB”
        * `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
        * `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
                * The default value of `text` is “is cool”
        * `/number/<n>`: display “`n` is a number” **only** if `n` is an integer
	* `/number_template/<n>`: display a HTML page **only** if `n` is an integer:
		* `H1` tag: “Number: `n`” inside the tag `BODY`
* You must use the option `strict_slashes=False` in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
```

[6. Odd or even?](./6-number_odd_or_even.py)

Write a script that starts a Flask web application:

* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
        * `/`: display “`Hello HBNB!`”
        * `/hbnb`: display “HBNB”
        * `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
        * `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
                * The default value of `text` is “is cool”
        * `/number/<n>`: display “`n` is a number” **only** if `n` is an integer
        * `/number_template/<n>`: display a HTML page **only** if `n` is an integer:
                * `H1` tag: “Number: `n`” inside the tag `BODY`
	* `/number_odd_or_even/<n>`: display a HTML page **only** if `n` is an integer:
		* `H1` tag: “Number: `n` is `even|odd`” inside the tag `BODY`
* You must use the option `strict_slashes=False` in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
```

