#!/bin/bash

make pdf/algebra-cc.pdf

while inotifywait -qre close_write,move,create,delete .; do make pdf/algebra-cc.pdf; done
