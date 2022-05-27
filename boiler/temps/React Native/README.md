# ReactNative-Node-Express

- This repository has the code to support React Native as FrontEnd, a Node/Express BackEnd and connect them together.
- This repository can also be used as a starting point (boilerplate), if you whant to create your own ReactNative and Node app.
- There are two separated apps. The client which serves the FrontEnd (using ReactNative), and the API (in Node/Express).
- Make sure you have downloaded Expo app on your mobile from AppStore/ PlayStore and mobile, laptop/desktop is connected to same network.

---

## Requirements

For development, you will only need Node.js and a node global package, Yarn, installed in your environement.

### Node

- #### Node installation on Windows

  Just go on [official Node.js website](https://nodejs.org/) and download the installer.
  Also, be sure to have `git` available in your PATH, `npm` might need it (You can find git [here](https://git-scm.com/)).

- #### Node installation on Ubuntu

  You can install nodejs and npm easily with apt install, just run the following commands.

      $ sudo apt install nodejs
      $ sudo apt install npm

- #### Other Operating Systems
  You can find more information about the installation on the [official Node.js website](https://nodejs.org/) and the [official NPM website](https://npmjs.org/).

If the installation was successful, you should be able to run the following command.

    $ node --version
    v8.11.3

    $ npm --version
    6.1.0

If you need to update `npm`, you can make it using `npm`! Cool right? After running the following command, just open again the command line and be happy.

    $ npm install npm -g

###

### Yarn installation

After installing node, this project will need yarn too, so just run the following command.

      $ npm install -g yarn

---

## Install

    $ git clone https://github.com/YOUR_USERNAME/PROJECT_TITLE
    $ cd PROJECT_TITLE
    $ yarn install

## Configure app

Open `a/nice/path/to/a.file` then edit it with your settings. You will need:

- A setting;
- Another setting;
- One more setting;

## Running the project

    $ yarn start

## Simple build for production

    $ yarn build

## How to run the API

- In your terminal, navigate to the `api` directory.
- Run `npm install` to install all dependencies.
- Run `npm run start` to start the app.

## How to run the Client/ my-app

- In another terminal, navigate to the `client` directory.
- Run `npm install` to install all dependencies.
- Run `npm run start` to start the app

## Check if they are connected

- Now scan the QR code using expo app.
- If you see interface saying `Click to connect to server`, it means the FrontEnd is working.
- Then click on connect button, if you see `API is working properly`, it means backend is working.
- Enjoy!
