# story-teller
a small inventory script for linux boxes (for now) written in python

#### Description
The script get the info from your linux system and puts them into a json file.

#### Usage

```
# python get_the_story.py
```

#### Notes

The script use dmidecode and for this root privileges is needed. The best way is to create a dedicated user with sudo privileges and set dmidecode to be runed without asking a password.
