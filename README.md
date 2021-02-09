<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
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
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">CampusQwest Backend</h3>

  <p align="center">
    This repository includes various files that build the backend infrastructure for CampusQwest
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
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
        <li><a href="#setup">Setup</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

TODO: May expand on this section of the README...
### Built With

The backend for the team's Senior Design project used:
* [Terraform](https://terraform.io)
* [AWS](https://aws.amazon.com)
* [Python 3](https://python.org)



<!-- GETTING STARTED -->
## Getting Started

To setup the backend, the steps below will help in accomplishing this task. This assumes the AWS CLI has been configured properly and that terraform  and Python 3.8 are installed.

### Setup 

1. Clone the repo and change into the directory
2. Set up a virtual environment in Python
   ```sh
   python -m venv venv
   source ./venv/bin/activate
   ```
3. Install the Python dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Then use the shell script for deployment
   ```JS
   chmod +x deploy.sh
   ./deploy.sh
   ```


<!-- USAGE EXAMPLES -->
## Usage

TODO: Might use this section...

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/DJPoland/CampusQwest-backend/issues) for a list of proposed features (and known issues).

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/DJPoland/CampusQwest-backend/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/DJPoland/CampusQwest-backend/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
