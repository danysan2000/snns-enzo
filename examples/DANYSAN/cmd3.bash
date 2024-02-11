#!/bin/bash

 sort -n lot_2.txt  | uniq -c  | sort -n +0 -1  | less 
