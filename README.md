# python-api-sidequest

## API We Will Use
https://opentdb.com/api_config.php

## Helpful Links to learn Web Development
- Flask: https://flask.palletsprojects.com/en/1.1.x/
- HTML: https://www.w3schools.com/html/ 
    * Things like {} are part of the Jinja2 template language, which essentially appears to extend the capabilities of HTML. 
- CSS: https://www.w3schools.com/css/default.asp
TypeScript from previous iterations of COMP110: https://comp110.com/topics
(TypeScript, as I understand it, is a more strongly typed version of JavaScript. The webpage includes how to incorporate TypeScript with HTML and CSS, and more resources on HTML/CSS/web development!)

## Running the example news website
To run locally, first clone this repository by following the steps in [https://21s.comp110.com/resources/setup/workspace.html#setup-your-workspace-in-visual-studio-code],
substituting the github link with [https://github.com/christineiym/python-api-sidequest.git]. 


Then, open your terminal and install the requirements in requirements.txt by running
pip install <requirement> (or if that does not work, pip3 install <requirement>)
for each requirement.
Alternatively, reinstall the updated COMP110 list of requirements by running this:
python -m pip install pip -r requirements.txt --user

Now, open a new terminal and write the following: 
1. export FLASK_APP=example_code.news
  - Alternatively, do the following: 
    1) cd example_code (cd stands for change directory, so this navigates you to the appropriate folder)
    2) export FLASK_APP=news
2. python -m flask run
Finally, click the link!

### Notes:
- For security/legal purposes, I ask that each of us have our own (free) newsAPI key (which can be obtained at [https://newsapi.org/]), which can be inserted in \__init\__.py to let the website work.
- Testing a website is sometimes like running a Jupyter Notebook -- to see your changes, you may have to close and open the website. Often, you may also just need to open an entirely new browser or an incognito window. This is because your computer caches information on the website to let it load faster, with the result that it may not be updated as quickly as you like.
- Feel free to copy the code into your sandbox folder and make edits to get a feel for how it works! However, please do not deploy the code -- it may cause problems with copyright laws. If you do accidentally deploy code on Heroku, you can either delete the app or you can take it down for maintenance (these options are found at the bottom of the Settings page for your project).
