#!/bin/bash -e
# Run JJB and then copy output into Jenkins configuration
JJB_VENV_ACTIVATE='/usr/local/jjb_venv/bin/activate'
JJB_SRC='/usr/local/src/jjb'
JOBS_DIR='/usr/share/jenkins/ref/jobs'

jjb_temp="$(mktemp -d)"
source "$JJB_VENV_ACTIVATE"

set -x
cd "$JJB_SRC"
jenkins-jobs test --recursive yaml:projects -o "$jjb_temp"
find "$jjb_temp" -type f \
    -printf "mkdir -p '$JOBS_DIR/%P' && mv '%p' '$JOBS_DIR/%P/config.xml'\n" \
    | bash -ex
rm -rfv "$jjb_temp"
