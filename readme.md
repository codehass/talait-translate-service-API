<a name="readme-top"></a>

<div align="center">
  <img src="public/logo-dark.png" alt="logo" width="140"  height="auto" />

  <br/>
</div>

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
  - [🚀 Live Demo](#live-demo)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Install](#install)
  - [Usage](#usage)
  - [Login](#login)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [📝 License](#license)

# 📖 KidLingo Translation Service - API <a name="about-project"></a>

This repository contains the backend for the KidLingo translation platform, built with FastAPI. The backend provides a secure API that handles translation requests, authenticates users, and interacts with the Hugging Face Inference API to translate text between French and English. The API includes endpoints for user registration, login (JWT generation), and the main translation function. The backend also handles errors like missing tokens, service unavailability, and invalid input formats, ensuring a robust and reliable service. The app is fully dockerized for easy internal deployment.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

  <ul>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
    <li><a href="https://www.sqlalchemy.org/">SQLAlchemy</a></li>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
    <li><a href="https://www.docker.com/">Docker</a></li>
  </ul>

### Key Features <a name="key-features"></a>

- **Secure API with JWT authentication**

- **Integration with Hugging Face Inference API for translations (FR → EN / EN → FR)**

- **Handles errors such as missing tokens and service disruptions**

- **PostgreSQL database for user management**

- **Fully dockerized for deployment**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🚀 Live Demo <a name="live-demo"></a>

- [Live Demo Link](link to deployed project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Setup

Clone this repository to your desired folder:

```sh
  git clone git@github.com:codehass/KidLingo-translate-service-API.git
```

### Install

Install this project with:

```sh
  cd KidLingo-translate-service-API
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
```

create `.env` file and add your environment variables. You can copy `.env.example` as a template.

```sh
  cp .env.example .env
```

### Usage

To run the project, execute the following command:

```sh
  uvicorn app.main:app --reload
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 👥 Author <a name="authors"></a>

👤 **Hassan El Ouardy**

- GitHub: [@codehass](https://github.com/codehass)
- Twitter: [@hassanelourdy](https://twitter.com/hassanelourdy)
- LinkedIn: [@hassanelourdy](https://www.linkedin.com/in/hassanelouardy/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🔭 Future Features <a name="future-features"></a>

- **Rate limiting for translation endpoints**
- **Support for additional languages**
- **Translation history logging**
- **Enhanced monitoring and analytics**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## ⭐️ Show your support <a name="support"></a>

Join us in supporting our project to improve cross-lingual communication with AI translations! Your help makes a big difference in bridging language gaps effortlessly. Let's work together to bring positive change to language accessibility!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📝 License <a name="license"></a>

This project is [MIT](./MIT.md) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
