#!/bin/bash
export FLASK_APP=flask-starter
export FLASK_ENV=development

#Application Config
export APPLICATION_HOST=127.0.0.1
export APPLICATION_PORT=5000
export SERVICE_LOG=$FLASK_APP.log

#Database Config
export APPLICATION_POSTGRES_USER=postgres
#export APPLICATION_POSTGRES_PW=
export APPLICATION_POSTGRES_HOST=127.0.0.1
export APPLICATION_POSTGRES_PORT=5432
export APPLICATION_POSTGRES_DB=postgres

#JSONRPC Config
export ENABLE_WEB_BROWSABLE_API=True


python $FLASK_APP/app.py &