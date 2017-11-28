#!/bin/bash

ssh -X 3525553@ssh.ufr-info-p6.jussieu.fr << EOF
  ssh -X ppti-14-302-02.ufr-info-p6.jussieu.fr << EOF2
  	touch /test1.py;
  EOF2		
EOF
