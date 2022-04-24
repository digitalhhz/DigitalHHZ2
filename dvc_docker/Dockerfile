#dockerfile

FROM debian:buster-slim
RUN apt-get update && \
	apt-get install -y --allow-unauthenticated openssh-server g++ && \
 	mkdir /var/run/sshd && \
	echo 'root:dvc' | chpasswd && \
	sed -i -E 's/#\s*PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
	sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
 	apt-get clean

RUN apt-get upgrade -y

RUN apt-get install vim -y
RUN apt-get install git -y
RUN apt-get install python3-pip -y

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

ADD . /app
WORKDIR /app
COPY ./scripts/ ./scripts

ARG GITUSER
ARG GITPAT

RUN git config --global credential.helper store
RUN git clone https://GITUSER:GITPAT@github.com/digitalhhz/cogitat.git

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
