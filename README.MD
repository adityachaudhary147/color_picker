
Preview images of working REST API
![saMPLE1](http:https://github.com/adityachaudahry147/color_picker/images/sampe1.jpeg)
![SAMPLE2](http:https://github.com/adityachaudahry147/color_picker/images/sample2.jpeg)

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/adityachaudahry147/color_picker.git
$ cd color_picker
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/home/`, `http://127.0.0.1:8000/api/`.