#!/bin/bash
ifconfig | grep wl | awk {'print $1'} | tr "\:\ " " "