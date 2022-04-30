# ChallengeDataAnalyticsWithPython

Hi! I am Leo :) I've wrote this code/mess.

This is my solution for the Data Analytics Challenge with Python.
You can read the "Challenge Data Analytics con Python.pdf" file to see all the tasks.
--Note: I'm still developing this project, only the first part is complete--
I have to say thanks to Alkemy's people because I've learned a lot by doing this challenge.

# What does the code do?
This code automatically queries three sources: museums, public libraries and cinemas. Then it creates a folder for each CSV file. The name and path of folders is also automatized.

# What do you need to run it?
You need to have python(programming language), pip(package manager for Python) and requests(an elegant and simple HTTP library for Python) installed in your computer. Most of computer already have python -and probably pip-. If you don't have python go https://www.python.org/ to downloads section. Python latest versions already include pip. Next, by using pip install requests packages. In a terminal/cmd type:
>pip install requests

Installation of requests package is very quick. And that's all you need :)

# How to use it?
Download -and unzip- the project.
Open your terminal/bash/cmd on project folder and type:
>python main.py

And that's it! Easy right? You now can check your folder and see that there are 3 new folders (museums, libraries and cinemas) with all the info in CSV files.

# Can I see the sources for the CSV files?
Sources are hardcoded in main.py and they are: 

url for museums
> https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv

url for cinemas
> https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv

url for libraries
> https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv

--Please, let me know if some link does not work--


# Things you can practice/learn
Get CSV files from the internet (by using requests library), open and write files, make directories, check current date with DateTime object.

Thanks for reading and happy coding :)
