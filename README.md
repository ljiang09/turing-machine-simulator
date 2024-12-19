# turing-machine-simulator
FOCS 2024 final project: turing machine visual simulator

## Initial Setup

TODO
install npm

## Running the app locally

Note that you will need two terminals to be open, one to run the backend and one to run the frontend.

### Backend Setup

It's recommended to run the backend in a virtual environment. This is because you might already have different versions of dependencies already installed on your device, which might interfere with the dependencies in this project.

A virtual environment provides a clean, isolated space where you install only the dependencies required for this specific project. Once you're done working, you can deactivate the virtual environment, and your system is clean and free of unnecessary packages.

1. In a terminal, run the following commands to create the virtual environment:

`$ python3 -m venv venv`
`$ source venv/bin/activate` (if you're using Windows, run `$ venv\Scripts\activate` instead)

2. Go to the root directory of this repo. Install dependencies with `$ pip install -r requirements.txt`

3. Run `$ npm run start-api` to start the Flask server


### Front-end Setup

1. In your second terminal, go to the root directory of this repo and run `$ npm install` to get all required dependencies in your environment.

2. Next run `$ npm start` to run the front-end app locally in the browser. If you go to the URL it prompts (something like `http://localhost:3000/`), you should see the app running.
