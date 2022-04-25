<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/NNLong1208/ChatBot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">ChatBot for Sales Automation </h3>

  <p align="center">
    A project of NEU students!
    <br />
    <a href="https://github.com/NNLong1208/ChatBot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/NNLong1208/ChatBot">View Demo</a>
    ·
    <a href="https://github.com/NNLong1208/ChatBot/issues">Report Bug</a>
    ·
    <a href="https://github.com/NNLong1208/ChatBot/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#anaconda">Anaconda</a></li>
        <li><a href="#docker">Docker</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#reference">Reference</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

* An API is created for a chatbot project that will be integrated into the sales website.
* Project for the purpose of education.
* Improved response time was achieved in this project.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python](https://www.python.org/)
* [Rasa](https://rasa.com/)
* [Docker](https://www.docker.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

* Clone the repo
   ```sh
   git clone https://github.com/NNLong1208/ChatBot
   cd ChatBot
   ```
### Anaconda

This is an example of how to list things you need to use the software and how to install them.
* Update pip
  ```sh
  pip install --upgrade pip
  ```
* Install package
  ```sh
  pip install -r requirements.txt
  ```
* Run
  ```sh
  python -m flash run --host=0.0.0.0
  ```
  

### Docker 

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

* Build image 
  ```sh
  docker build -t chatbot . 
  ```
* Run image
  ```sh
  docker run -p 5000:5000 chatbot
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
* Python
  ```sh
  import requests
  import json
  url = "http://localhost:5000/api"
  payload = json.dumps({
    "text": "Xin Chào, có ai ở đây không"
  })
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
  ```
  
 * NodeJs
  ```sh
  var request = require('request');
  var options = {
  'method': 'POST',
  'url': 'http://localhost:5000/api',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "text": "Xin Chào, có ai ở đây không"
  })

  };
  request(options, function (error, response) {
    if (error) throw new Error(error);
    console.log(response.body);
  });
  ```
  
  * JavaScript
  ```sh
  var settings = {
  "url": "http://localhost:5000/api",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "text": "Xin Chào, có ai ở đây không"
  }),
  };

  $.ajax(settings).done(function (response) {
    console.log(response);
  });
  ```
  You can use any language to call the API in addition to the ones listed above.
<!-- ROADMAP -->
## Roadmap

- [x] Crate repo
- [x] Train model
- [x] Write API
- [x] Wrap code into Docker
- [ ] Update
    - [x] Update model v1
    - [x] Update model v2
    - [ ] Update model v3
- [ ] Deploy on Telegram

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under theGNU General Public License v3.0. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Nguyễn Ngọc Long - [FaceBook](https://www.facebook.com/lnn1208/) - [Gmail](ngoclong1282001@gmail.com)

Project Link: [https://github.com/NNLong1208/ChatBot](https://github.com/NNLong1208/ChatBot)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Reference -->
## Reference

You can see the code of my website [here](https://github.com/thanhdat02112001/Eshop)

* [Rasa repo](https://github.com/RasaHQ/rasa)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/NNLong1208/ChatBot.svg?style=for-the-badge
[contributors-url]: https://github.com/NNLong1208/ChatBot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/NNLong1208/ChatBot.svg?style=for-the-badge
[forks-url]: https://github.com/NNLong1208/ChatBot/network/members
[stars-shield]: https://img.shields.io/github/stars/NNLong1208/ChatBot.svg?style=for-the-badge
[stars-url]: https://github.com/NNLong1208/ChatBot/stargazers
[issues-shield]: https://img.shields.io/github/issues/NNLong1208/ChatBot.svg?style=for-the-badge
[issues-url]: https://github.com/NNLong1208/ChatBot/issues
[license-shield]: https://img.shields.io/github/license/NNLong1208/ChatBot.svg?style=for-the-badge
[license-url]: https://github.com/NNLong1208/ChatBot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://github.com/NNLong1208/ChatBot
[product-screenshot]: images/screenshot.png
