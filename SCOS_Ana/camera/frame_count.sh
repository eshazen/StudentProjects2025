#!/bin/bash
ffprobe -show_packets $1 2>/dev/null | grep video | wc -l
