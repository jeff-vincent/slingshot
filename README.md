### Where Ideas Take Flight


Slingshot allows public speakers to leverage their audiences' cell phones as answer-submission devices by collecting data via text message, and presenting it in a dynamic UI for impromptu analysis. 

Quizzes and surveys are currently limited to a multiple-choice answer format. However, there is still plenty of room to build in layered analysis. For example, if survey participants are pre-registered, any number of `sms_user.demographic` (experience, opinion, etc. of text message answer submitters) data could be assigned to the `answer_objects` (incoming text message answers) to enrich the eventual analysis. 

It works by listening for and handling POST requests forwarded from a sms routing service. This document specifies [Twilio](https://twilio.com) for this service (largely because their docs are so good), but any sms routing service that delivers bidirectional sms to HTTP conversion should work. 

Upon receipt of the request, the sender's phone number (or any other reliable unique identifier in the POST request) can either be associated with a pre-existing `sms_user.id`, or Slingshot can operate anonymously and without any persistant storage. 

### Table of Contents

- [API]()

- [Viewing & Building the Docs]()

- [Running Slingshot Locally]()

  - Front End ([React](https://reactjs.org))
  
  - Back End ([Quart](https://gitlab.com/pgjones/quart))

- [Understanding Slingshot's Inner Workings]()


### API   

...

### Viewing & Building the Docs

The docs are driven by Sphinx. To build and view the docs, run the following: 

```bash
make docs
```
Then, go to `localhost:8000` to view the docs. 

### Running Slingshot Locally

##### Clone the repo

```bash
git clone https://github.com/jeff-vincent/Slingshot.git
```
```bash
git clone git@github.com:jeff-vincent/Slingshot.git
```
##### Install dependencies

Prerequisite package managers: [pip](https://pypi.org/project/pip/); [npm](https://www.npmjs.com/).

First, create a [virtualenv](https://pypi.org/project/virtualenv/) that runs Python3.7+, enter the `venv`, and then run the following:

```bash
(sudo) pip install -r requirements.txt
```
If you haven't already, create a Twilio account. Then select a phone number, and create a TwiML app as described at: 

- [https://www.twilio.com/console/sms/runtime/twiml-apps/add](https://www.twilio.com/console/sms/runtime/twiml-apps/add)
  

### Understanding Slingshot's Inner Workings

Slingshot handles HTTP requests from both the web-based front end and any text messages it receives (again, as HTTP POST requests via a sms routing service). 
  
![Imgur](https://i.imgur.com/OMkNnpP.jpg)

##### API

Incoming requests are handled by a universal HTTP API. 

##### Controllers

...

##### Models

...

-----------------------------------------------------

##### License

Copyright 2020 Jeffrey D. Vincent

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.