# Bitly url shorterer

This is a console URL shortener which uses bit.ly API and also counts clicks on the short link. 

### How it works

Run the python script with this console command:
```
python main.py [Paste your link. It should start with HTTP or HTTPS]
```
For example:
```
python main.py https://google.com
```
And the result will look like:
```
Short link: https://bit.ly/2JiL9AU
```
### How to install
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```