#!/usr/bin/bash

sed -E s/t//g  lot_1.txt  | sort -n | less
