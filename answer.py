#!/usr/bin/env python

import random

print "Content-Type: text/html"
print
print """
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>Gamelan Note Tester - Answer</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!--<link rel="stylesheet" href="css/normalize.min.css">-->
        <!--<link rel="stylesheet" href="css/main.css">-->

        <!--<script src="js/vendor/modernizr-2.6.2.min.js"></script>-->
    </head>
    <body>
"""
notes = ['calung-1', 'calung-2', 'calung-3', 'calung-4', 'calung-5']

note = random.choice(notes)

answers = ['correct', 'incorrect']

answer = random.choice(answers)

print "<div id='container'>"

print "Your answer was: {0}\nthis is {1}".format(note, answer)

print "</div>"


print """
    </body>
</html>
"""