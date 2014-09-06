#!/usr/bin/python

"""Test of sayAll."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_Add"))
sequence.append(utils.AssertPresentationAction(
    "1. KP_Add to do a SayAll",
    ["SPEECH OUTPUT: 'nested-tables image link'",
     "SPEECH OUTPUT: 'Campus'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '  .  '",
     "SPEECH OUTPUT: 'Classroom'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '  .  '",
     "SPEECH OUTPUT: 'Communicate'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '  .  '",
     "SPEECH OUTPUT: 'Reports'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Your Learning Plan'",
     "SPEECH OUTPUT: 'Below is a list of the courses that make up your learning plan.'",
     "SPEECH OUTPUT: 'UNIX 2007'",
     "SPEECH OUTPUT: 'blank'",
     "SPEECH OUTPUT: 'Take Course'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'blank'",
     "SPEECH OUTPUT: 'blank'",
     "SPEECH OUTPUT: 'You have completed 87 of the 87 modules in this course.'",
     "SPEECH OUTPUT: 'separator'",
     "SPEECH OUTPUT: 'SQL Plus'",
     "SPEECH OUTPUT: 'blank'",
     "SPEECH OUTPUT: 'Take Course'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'blank'",
     "SPEECH OUTPUT: 'blank'",
     "SPEECH OUTPUT: 'You have completed 59 of the 184 modules in this course.'",
     "SPEECH OUTPUT: 'separator'"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
