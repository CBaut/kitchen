# Kitchen App for Dojo After Dark

Django application to manage kitchen inventory.

## Prerequisites

- Make sure you have Python 3.7+ [installed locally](http://install.python-guide.org)
- Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

## How to run the project locally

- From the terminal `cd` into the folder you want to save the project
- Clone the project `git clone https://github.com/CBaut/kitchen.git`
- `cd` into the newly created project folder (`ls` or `dir` to view the contents of the current directory)
- create a virtual environment `python3 -m venv venv` or just `python`
- Activate the virtual environment:
  - For Windows: `call venv/Scripts/activate`
  - For Mac: `source venv/Scripts/activate`
- Install dependencies `pip3 install -r requirements.txt` or `pip`
- Migrate the database `python3 manage.py migrate`
- Start the project
  - For Windows: `heroku local web -f Procfile.windows`
  - For Mac: `heroku local`

Your app should now be running on [localhost:5000](http://localhost:5000/).
