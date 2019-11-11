# Project 3

Final Project for CSCI 204!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Setup Git

What things you need to install the software and how to install them

#### First time setting up Git

Tell Git who you are

```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

Generate SSH key (To make connection with Git)

```
ssh-keygen -t rsa
```

then see the SSH key

```
cat ~/.ssh/id_rsa.pub
```

Copy the key (including the "ssh-rsa" at the beginning)

Click on your avatar, click on Settings near the end, click on SSH and GPG keys tab, click New SSH key, paste the key and click Add SSH key

Clone Project from Github

```
git clone git@github.com:sontungtran/CS204-Project3.git
```

Create new branch & navigate into your branch

```
git checkout -b [your-name]
```

and check with ```git status```

#### Make sure you run ```git pull``` before editing anything

#### After your work is done
Push to your branch with

```
git add -A
git commit -m 'Commit Message'
git push origin [your branch's name]
```

### Setup Virtual Environment

Create your own virtual environment

```
python -m venv ~/[your-virtual-environment-name]
```

Activate virtual environment with

```
source ~/env/bin/activate
```

and install packages

```
pip install -r requirements.txt --user
```

## Bridges [Documentation](http://bridgesuncc.github.io/doc/python-api/1.0/html/namespace_bridges.html)

## Running the tests

Explain how to run the automated tests for this system (TODO)

### Break down into end to end tests

Explain what these tests test and why (TODO)

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Authors

List of [contributors](https://github.com/sontungtran/CS204-Project3/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements

* Thanks Prof. Dancy for giving us 1 week to setup all these
* Inspiration: Not to get C for the Final Project
* Look at dis GIF!

![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)
