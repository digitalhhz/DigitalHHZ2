FROM python:3.8
RUN apt-get update && \
	apt-get install -y --allow-unauthenticated openssh-server g++ && \
 	mkdir /var/run/sshd && \
	echo 'root:autoML' | chpasswd && \
	sed -i -E 's/#\s*PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
	sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
 	apt-get clean
RUN apt-get install curl
COPY requirements.txt requirements.txt
COPY .env /opt/.env
COPY KI_Lab_training.py /opt/KI_Lab_training.py
RUN pip3 install -r requirements.txt
WORKDIR /opt
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
