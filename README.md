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
  
  - Back End ([Flask](http://flask.pocoo.org/))

- [Understanding Slingshot's Inner Workings]()


### API   

- All the information you need to make requests to the Slingshot API.

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

First, create a [virtualenv](https://pypi.org/project/virtualenv/) that runs Python3, enter the `venv`, and then run the following:

```bash
(sudo) pip install -r requirements.txt
```
If you haven't already, create a Twilio account. Then select a phone number, and create a TwiML app as described at: 

- [https://www.twilio.com/console/sms/runtime/twiml-apps/add](https://www.twilio.com/console/sms/runtime/twiml-apps/add)
  
##### Gotchas

If you're getting `CORS` errors, try using `ngrok`. You can find a handy install and basic use guide at: 

- [https://opensourcehacker.com/2015/03/27/testing-web-hook-http-api-callbacks-with-ngrok-in-python/](https://opensourcehacker.com/2015/03/27/testing-web-hook-http-api-callbacks-with-ngrok-in-python/)

##### Webpack build
 
```bash
npm run build
```
    
##### Tests

```bash
npm run tests
```

### Understanding Slingshot's Inner Workings

Slingshot handles HTTP requests from both the web-based front end and any text messages it receives (again, as HTTP POST requests via a sms routing service). 
  
![Imgur](https://i.imgur.com/OMkNnpP.jpg)

##### API

Incoming requests are handled by a universal HTTP API. 

##### Controllers

These modules currently house the logic for classes ``user``, ``sms``, and ``session``. 

##### Models

The models are very simple. A ``session_object`` is instantiated at "go". Each question posed is a new key in that dict., and the unsorted list of ``answer_objects`` is the associated value. 

-----------------------------------------------------

##### License

Copyright 2018 J.D. Vincent

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
