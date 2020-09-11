#!/usr/bin/env bash

sudo fuser -k 8000/tcp

uwsgi -d --ini uwsgi.ini

nginx -s reload
