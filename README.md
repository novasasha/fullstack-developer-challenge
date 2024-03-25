<p align="center" >
 <svg viewBox="0 0 106 165" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M0 27.5L53 55V110L106 82.5V27.5L53 0L0 27.5Z"
    fill="#2D6DF6" />
  <path fill-rule="evenodd" clip-rule="evenodd" d="M0 27.5L53 55V110L106 82.5V27.5L53 0L0 27.5Z"
    fill="url(#paint0_linear_2070_5702)" />
  <path fill-rule="evenodd" clip-rule="evenodd" d="M53 110L0 82.5V137.5L53 165V110Z" fill="#C7EBFF" />
  <defs>
    <linearGradient id="paint0_linear_2070_5702" x1="53" y1="1" x2="53" y2="110"
      gradientUnits="userSpaceOnUse">
      <stop stop-color="#1C44D2" />
      <stop offset="0.369792" stop-color="#2D6DF6" />
      <stop offset="1" stop-color="#89D5FF" />
    </linearGradient>
  </defs>
</svg>  
</p>


# Prefect Fullstack Developer Challenge

Welcome to the Prefect Fullstack Developer Challenge!

This challenge consists of 3 exercises. The goal is to get a sense of how you solve problems and implement your code - the  questions are not designed to trick you.

No additional packages or libraries are required but you may add any that you wish.  Please do not modify the instructions component (found at `/src/pages/HomeInstructions.vue`) or any of the instruction text for the exercise (these will be clearly denoted in  the code with an `...__instructions` class) until your submission has been graded.  Any other code (including router, store, styling, and components) are free for you to modify at your discretion.

Continue reading for project setup and submission.

## Project setup

- Clone this repository
- Change the remote to a private GitHub repository under your username
- Push code to that remote, using clear Commits and Pull Requests with clear messages
- Code!

## Submission

This project should be submitted by adding [@znicholasbrown](https://github.com/znicholasbrown), [@pleek91](https://github.com/pleek91), [@zhen0](https://github.com/zhen0), [zangell44](https://github.com/zangell44) and [@collincchoy](https://github.com/collincchoy) as collaborators to your cloned repository on GitHub. Once you've done so, please send an email to [jenny@prefect.io](jenny@prefect.io) to confirm your submission.

## Recommended IDE

- [VSCode](https://code.visualstudio.com/)
- [Volar](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar) (vscode extension) is registered as a workspace recommended extension. 
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) Python language support with IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, and unit tests.

## Local Development

To start, make sure you're on the right versions of NodeJS and Python.

for Node:
```
nvm use
```

for Python:
```
pyenv local
```

Note that these assume you have Node Version Manager and Pyenv on your machine; you're free to use the environment managers of your choice, `.nvmrc` and `.python-version` files have been provided for convenience. 


Then, install project dependencies.

For Node:
```
npm ci
```

For Python:
```
pip install -r requirements.txt
```

### Transpiles and hot-reloads for development

Then, start your development server.

In one terminal, start your Fast API webserver with the following (from the root directory):
```
python server.py
```

And in another, start your Vue application with the following:
```
npm run dev
```

You should now be able to navigate to [localhost:5173](http://localhost:5173)! (Note: you may need to modify the `PORT` variable in `.env` if you've another process running on :5174)


### Lints and fixes files

This project is setup to use the same ESLint config our frontend developers actually use. https://www.npmjs.com/package/@prefecthq/eslint-config. The workspace settings (assuming you're using vscode) are setup to automatically fix any fixable eslint errors on save.

## Making your work public

_The work you do on this project is your own_. As such, you can make it publicly  available at your discretion (on your GitHub, as part of a portfolio etc.).

If you plan to make this repository public, **please do not do so until after your submission has been graded** (we'll let you know when that is!). In addition, please  remove or replace Prefect in the `<title>` block of the root html file (found in `/public/index.html`) and any associated logos.
