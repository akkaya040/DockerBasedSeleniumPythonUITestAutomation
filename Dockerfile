FROM --platform=linux/amd64 python:3.8
MAINTAINER Kurtulus Akkaya akkaya040@gmail.com

#Args Will Be Passed Into Test
#Override for docker run after build as I wish
ARG browser
ENV browser=$browser
ARG keyword
ENV keyword=$keyword

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -


# Adding Google Chrome to the repositories And Install Chrome Stable
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# Adding Firefox to the repositories And Install Firefox Stable
RUN sh -c 'echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list'
RUN apt-get -y update
RUN apt-get install -y --no-install-recommends firefox


# Installing Chrome Driver Latest If it is needed.
#RUN apt-get install -yqq unzip
#RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
#RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable
ENV DISPLAY=:99

#Install Python Dependencies
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt

#Copy Test Files Then Test Run
COPY . .
CMD python test_search.py $browser $keyword
#CMD ["sh", "-c", "python test_search.py.py $browser $keyword"]
