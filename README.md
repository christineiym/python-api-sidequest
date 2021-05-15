# python-api-sidequest

## Important Updates
We will take small steps first - so no APIs just yet!

## Repository Structure
- draft_product: The working draft of the website that will serve as the basis for sidequest(s).
  * resources: Various references used to develop the website; will be converted into links that students can explore for more information on web development (or we can put the links with more info in a separate page of their website!).
  * unc_abbreviations: Website that allows students to practice using Python dictionaries with web development.
    * Has a Python dictionary in constants pre-populated with abbreviations like LDOC and their meanings, as I thought that dealing with a Python dictionary with data might be a good stepping stone for them to consult actual databases.
- example_code: Previous personal code that serves as a reference for the website.
  * news: Site that displays news about UNC; does not have search or GET/POST capabilities.
- planning_notes: Record of the progress made on the sidequest.
- sandbox_christine: For individual experimentation.
  * random_code_snippets: Has alternate (in-progress) code for the website.
- sandbox_david: For individual experimentation. Currently empty.

## Helpful Links to learn Web Development
- Flask: https://flask.palletsprojects.com/en/1.1.x/
- HTML: https://www.w3schools.com/html/ 
    * Things like {} are part of the Jinja template language that works with HTML (more info on that here: https://jinja.palletsprojects.com/en/2.11.x/templates/. 
- CSS: https://www.w3schools.com/css/default.asp
- TypeScript from previous iterations of COMP110: https://comp110.com/topics  (TypeScript, as I understand it, is a more strongly typed version of JavaScript. The webpage includes how to incorporate TypeScript with HTML and CSS, and more resources on HTML/CSS/web development!)

## Running the example news website 
(For learning purposes; a similar process may be followed to run the example product, whose steps to run are included in the docstring.)

To run locally, first clone this repository by following steps 1 - 7 in https://21s.comp110.com/resources/setup/workspace.html#setup-your-workspace-in-visual-studio-code,
substituting the github link with https://github.com/christineiym/python-api-sidequest.git. 

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
- For security/legal purposes, I ask that each of us have our own (free) newsAPI key (which can be obtained at https://newsapi.org/), which can be inserted in \_\_init\_\_.py to let the website work.
- Testing a website is sometimes like running a Jupyter Notebook -- to see your changes, you may have to close and open the website. Often, you may also just need to open an entirely new browser or an incognito window. This is because your computer caches information on the website to let it load faster, with the result that it may not be updated as quickly as you like.
- Feel free to copy the code into your sandbox folder and make edits to get a feel for how it works! However, please ask me if you are interested in deploying code to Heroku. 
- If you deploy code on Heroku and want to take it down, you can either delete the app or you can take it down for maintenance (these options are found at the bottom of the Settings page for your project).

## API We May Use in the Future
https://opentdb.com/api_config.php
Note: if documentation for the API is not that great, we should not feel a pressure to use it.
