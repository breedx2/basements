#!/bin/bash

MYDIR=$(dirname "$0")


/usr/bin/pd -verbose -jack \
    -channels 2 \
    -r 48000 \
    -alsamidi \
    -midiindev 2 \
    -midioutdev 2 \
    -audiobuf 10 \
    -path "${MYDIR}" \
    -send "pd dsp 1" "${MYDIR}/basements.pd"

