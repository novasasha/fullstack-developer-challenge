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

No additional packages or libraries are required but you may add any that you wish.  Please do not modify the instructions component (found at `/src/pages/HomeInstructions. vue`) or any of the instruction text for the exercise (these will be clearly denoted in  the code with an `...__instructions` class) until your submission has been graded.  Any other code (including router, store, styling, and components) are free for you to modify at your discretion.

Continue reading for project setup and submission.

## Project setup

- Clone this repository
- Change the remote to a private GitHub repository under your username
- Push code to that remote, using clear Commits and Pull Requests with clear messages
- Code!

## Submission

This project should be submitted by adding [@znicholasbrown](https://github.com/znicholasbrown), [@pleek91](https://github.com/pleek91), [@zhen0](https://github.com/zhen0) as collaborators to your cloned repository on GitHub. Once you've done so, please send an email to [jenny@prefect.io](jenny@prefect.io) to confirm your submission and to submit your exercise 1 python questionnaire answers.

## Recommended IDE

- [VSCode](https://code.visualstudio.com/)
- [Volar](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar) (vscode extension) is registered as a workspace recommended extension. 

## Local Development

To start, make sure you're on the right version of node.

```
nvm use
```

Then, install the project dependencies.

```
npm ci
```


### Transpiles and hot-reloads for development

Then, start your development server.

```
npm run dev
```

### Lints and fixes files

This project is setup to use the same ESLint config our frontend developers actually use. https://www.npmjs.com/package/@prefecthq/eslint-config. The workspace settings (assuming you're using vscode) are setup to automatically fix any fixable eslint errors on save.

## Making your work public

_The work you do on this project is your own_. As such, you can make it publicly  available at your discretion (on your GitHub, as part of a portfolio etc.).

If you plan to make this repository public, **please do not do so until after your  submission has been graded** (we'll let you know when that is!). In addition, please  remove or replace Prefect in the `<title>` block of the root html file (found in `/public/index.html`), the `<link>` and `<meta>` blocks between the comments in that same  file, as well as the associated logos in that folder. Last, please remove or  replace the Prefect logo in the root application file (found in `/src/App.vue`) and the  associated `.svg` found in the assets folder.

If you haven't modified the `index.html` file as part of your challenge (you shouldn't  need to), you can run the following command from the root of the project directory to automatically remove / replace all of the above:

```bash
$ mv public/index-template.html public/index.html && \
  rm public/{*.png,*.xml,*.ico,*.svg,*.webmanifest} && \
  mv src/assets/vue-logo.svg src/assets/logo.svg
```
