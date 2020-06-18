<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Unofficial Stash</h3>

  <p align="center">
    Unofficial CLI Implementation for Stashaway
    <br />

  </p>
</p>

## Disclaimer
Please do note that this is the Unofficial Implementation of Stashaway


<!-- ABOUT THE PROJECT -->
## About The Project
A simple way to preview, store, monitor your balance, securities easily. 

This application only works for [Stashaway Malaysia](https://www.stashaway.my/).

This application cannot be automated, and need human involvement daily.

### Prerequisites

This are the things you are required to run this application.

Luckily, you can just install the requirements provided
```sh
pip install -r requirements.txt
```


### Installation
 
1. Clone the repo
```sh
git clone https://github.com/liej6799/unofficial_stash
```
2. Install the requirement packages
```sh
pip install -r requirements.txt
```


<!-- USAGE EXAMPLES -->
## Usage

This is how to run the application

### Login

When you first install please login 
```sh
python main.py login
```
Input
```sh
Email: awd@mail.com
Password: (hidden)
```

### Validate 2FA

After success login, you will get this output:
```sh
The credentials provided is correct, code has been sent to this number: %{number}.
```
Now you need to run the 2fa module
```sh
python main.py validate-2fa
```

Input
```sh
Code from SMS: 123456
```

### Daily

Run this module to get current data from the api, make sure run this daily

As currently the bearer provided expired quickly, 
and need to fill in 2fa sms everytime, it is not possible to run this tool as a automation.

As result, this command must be manually run everyday.

Simply run:
```sh
python main.py daily
```

Then it will populate the database with latest data.

### Display

When all the hardwork has been done, you can just run this module to display your data gathered.
```sh
python main.py display-all
```

### More Info

Using [Click](https://click.palletsprojects.com/en/7.x/) library to create cli application, you can view all the command available
```sh
python main.py
```


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Stashaway MY](https://www.stashaway.my/)



