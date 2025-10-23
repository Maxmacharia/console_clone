#!/usr/bin/env bash

FULL_PATH = "/data/web_static/releases/test"

LINK_PATH = "/data/web_static/current"

FILE_NAME = "index.html"

mkdir -p "$FULL_PATH"

touch "$FULL_PATH/$FILE_NAME"

ln -sf "$FULL_PATH $LINK_PATH

sudo chown -R ubuntu:ubuntu "$FULL_PATH"

server {
	listen		8080
	access_log	off;
	location / {
		proxy_pass		http://127.0.0.1:8000;
	}
	location /data/web_static/current {
		alias /hbnb_static
	}
}
