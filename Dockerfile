FROM jenkins:2.46.2

# install JJB
USER root
RUN apt-get update  && \
	apt-get install -y jenkins-job-builder python-virtualenv && \
	virtualenv --system-site-packages '/usr/local/jjb_venv' && \
	/bin/bash -c 'source /usr/local/jjb_venv/bin/activate && \
	pip install "jenkins-job-builder>=1.6"'
USER jenkins

# Install Jenkins plugins
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

# Remove initial startup banner
RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state

# Copy JJB sources
COPY jjb-runner.sh /usr/local/bin/jjb-runner.sh
COPY jjb /usr/local/src/jjb
RUN /usr/local/bin/jjb-runner.sh

