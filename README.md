# Docker Based Selenium Python Test Automation

This project demonstrates how to perform web automation testing using Selenium and Python within a Docker container. It includes steps to set up a headless browser environment, execute search queries on different search engines, and compare the results.

## Prerequisites

* Docker should be installed on your system (MacOS, Windows, Linux)

## Installation

To build and run the project, follow these steps:

1. Clone this repository to your local machine.

```bash
git clone https://github.com/akkaya040/*.git
```

2. Navigate to the project directory.
```bash
cd your-repo
```

# Usage

## Build the Docker container
```bash
docker build -t selenium-automation .
```
#### If we want to test parameter to test during build step.

```bash
docker build . --build-arg browser=chrome --build-arg keyword=araba -t testrunner
```
## Run Test In Builded Docker Container
```bash
docker run -it testrunner
```
* This command will start the automation process within the Docker container. The automated tests will be executed against search engines, and the results will be compared with the given args browser and keyword during build step.

* If we want to run same build with another args, we will pass and override these values as env value.

```bash
docker run -e browser=firefox -e keyword=deneme -it testrunner
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


