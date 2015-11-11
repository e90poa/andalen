
# To run:
- Install brew
- brew install git
- Install http://postgresapp.com/
- Install https://toolbelt.heroku.com/
- $ cd ~/Projects/ 
- $ git clone git@github.com:e90poa/andalen.git 
- $ pip install venv
- $ virtualenv venv
- $ source venv/bin/activate
- $ pip install -r pip.requirements.txt

# To Deploy:
- First add heroku in git: $ git remote add heroku https://git.heroku.com/andalen.git
- Then just push the committed code to deploy:
    $ git push heroku master

# Crash-course in git:
- See what changed: $ git status
- Add a file to commit (called staging): $ git add <filename>
- Commit file: $ git commit -m "My first commit"
- Push commit to server: $ git push origin master
- Pull latest changes: $ git pull origin master
- Remove an added file from commit: $ git reset <filename>
- Revert a file to original state: $ git checkout <filename>


# Please note:
**Do not commit any passwords or sensitive information without making repo private**
Use heroku config to store these things - look here: https://dashboard.heroku.com/apps/andalen/settings

