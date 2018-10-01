# Personality Text Summary Python Wrapper
This is a Python wrapper for the Personality Text Summary library implemented in Javascript by IBM's Watson developers.
Currently, it relies heavily on the Javascript standalone library, but I am looking to re-implement it in the future.

## Prerequisites
You will need Python, node, and npm installed.
For Windows users, to install Python, click [here](https://www.python.org/downloads/windows/) to find the version of Python you would like to download and install. To install node and npm, click [here](https://nodejs.org/en/download/) to find the versions of node and npm you would like to install.
For Mac users, open a Terminal and execute the following commands:
```sh
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
brew install node
```
For Linux users, open a Terminal and execute the following commands:
```sh
sudo apt-get install python
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## Usage
Clone my repository into whatever directory you would like. Then, create a new Python script.
See the following Python code for how you can use the `getSummary()` method in your script.
```sh
# coding: utf-8
from watson_developer_cloud import PersonalityInsightsV3 as PersonalityInsights
import personalitysummary

# Below are your IBM Bluemix Credentials, where 'IBM_USERNAME' is your username and 'IBM_PASSWORD' is your password.
pi_username = 'IBM_USERNAME'
pi_password = 'IBM_PASSWORD'
pi_version = "IBM_version"
pi_url = "IBM_url"

personality_insights = PersonalityInsights(username=pi_username, password=pi_password, pi_version, pi_url)

# 'text' can be any text you want to analyze and obtain a personality summary of. I've provided the Gettysburg Address as an example.
text = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."
pi_result = personality_insights.profile(text)

# getSummary() returns a summary of the profile obtained from the above text.
# It can take one parameter, which is just the profile.
sum_r1 = personalitysummary.getSummary(pi_result)

# It can also take three parameters, which would be the profile, language, and version of the Personality Insights Summary.
# The language can be one of {'en', 'es', 'ja', 'ko'}.  Version refers to which version of Watson Personality Insights to use, and can be either 'v2' or 'v3'.
# The default above is set to 'en' and 'v3'.
sum_r2 = personalitysummary.getSummary(pi_result, 'es', 'v2')

# Prints summaries obtained to console.
print(sum_r1)
print(sum_r2)
```
