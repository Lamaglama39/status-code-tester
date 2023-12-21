# status-code-tester

This is a test tool that returns various status codes.

## Description

This is an app that returns a status code based on the URL being accessed.
Please use it for testing purposes such as checking front-end operation.

## Getting Started

### Dependencies

- Almost all Linux distributions
- Docker
- Docker Compose

For reference,the author uses the following environment.
- WSL2 Ubuntu 22.04.4 LTS
- Docker version 25.0.3
- Docker Compose version v2.24.6-desktop.1

### Installing

* run docker-compose
```
$ git clone https://github.com/Lamaglama39/status-code-tester.git
$ cd status-code-tester
$ docker-compose up -d
```

### Usage example

* API docs
```
http://localhost:8000/docs/
```

### Developer operations

* Add python packages
```
$ docker-compose up
$ docker-compose exec api poetry add $PACKAGE_NAME
```

* Container Login
```
$ docker-compose exec api /bin/bash
```

## Project Structure
```
.
├── Dockerfile
├── LICENSE.md
├── README.md
├── api
│   ├── __init__.py
│   ├── main.py
│   └── status_messages.py
├── docker-compose.yml
├── infrastructure
├── poetry.lock
├── pyproject.toml
└── tests
```

## Author

[@Lamaglama39](https://twitter.com/lamaglama39)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details



