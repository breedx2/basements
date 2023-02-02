#!/bin/bash

MYDIR=$(dirname "$0")

AUDIODEV=0

# override for local development
if [ -f "${MYDIR}/.audiodev" ] ; then
	AUDIODEV=$(cat "${MYDIR}/.audiodev")
fi

/usr/bin/pd -verbose -alsa \
    -channels 2 \
    -r 48000 \
	-audiodev ${AUDIODEV} \
    -audiobuf 10 \
    -path "${MYDIR}" \
    -send "pd dsp 1" "${MYDIR}/basements.pd"

