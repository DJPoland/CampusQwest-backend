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
        <li><a href="#configured-with">Configured With</a></li>
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
### Configured With:

The tools needed for CampusQwest includes:
* [Terraform](https://terraform.io)
* [AWS CLI](https://aws.amazon.com)
* [Python 3](https://python.org)
* An operating system that supports shell scripts (UNIX/*NIX environments)



<!-- GETTING STARTED -->
## Getting Started

To setup the backend, the steps below will help in accomplishing this task. This assumes the AWS CLI has been configured properly and that terraform  and Python 3.8 are installed.

### Setup 
1. Ensure you have configured the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) with your AWS account and have the [Terraform CLI](https://www.terraform.io/downloads.html).
2. Clone the repo and change into the directory ```~/CampusQwest-backend/lambdas ```
3. Set up a virtual environment in Python (Note: Make sure the environment is Python 3.8.*, not 3.9+ due to AWS Lambda runtime support).
   ```sh
   python -m venv venv
   source ./venv/bin/activate
   ```
4. Install the Python dependencies
   ```sh
   pip install -r requirements.txt
   ```
5. Then use the shell script for generating deployable Lambda functions
   ```JS
   chmod +x create_lambdas.sh
   ./create_lambdas.sh
   ```
6. Now simply head back to the root of the directory and manage the infrastructure with the Terraform CLI.


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
