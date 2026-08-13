#!/bin/bash

make build/index.html

while inotifywait -qre close_write,move,create,delete .; do make build/index.html; done
