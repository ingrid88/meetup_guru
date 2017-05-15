from __future__ import unicode_literals

#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to

import datetime
import requests
import json
import time
import codecs
import sys
# import meetup-pages-names-dates as meetup


# 1. Return the local meeetups by meetupID
# 2. Look at each and count # of RSVPs https://api.meetup.com/2/rsvps?&sign=true&photo-host=public&event_id=234481909&page=20


# 1. return top 5 recommended events (meetup url)
# input: location, text (string describing meetup)
# eg http://api.meetup.com/find/events?lon=-74.0059&key=6e54503d561d3752495d443681d6875&lat=40.7128&text=datascience+python
# "lat": 40.743953704833984,
# "lon": -73.9854507446289

# https://api.meetup.com/recommended/events?&sign=true&photo-host=public&lon=-74.0059&page=40&topic_category=data&lat=40.7128

def findout(topic, location):

    api_key= "27231503824b247871211a2178305f"
    if location == 'NY':
        lon = -74.0059
        lat = 40.7128
    elif location == 'Portland, Oregon':
        lon = -122.6765
        lat = 45.5231
    else:
        lon = -74.0059
        lat = 40.7128

    response=get_results({ "lon":lon, "key":api_key, "lat":lat, "text":topic})
    print response[0]

    thingy = lambda x: x['link']+ \
        " \n Called: "+x['name']+ \
        " at "+datetime.datetime.fromtimestamp((x['time']+ \
        x['utc_offset'])/1000).strftime('%c')+ \
        " time!"
    return "\n".join(map(thingy,response[0:5]))



def get_results(params):

    request = requests.get("http://api.meetup.com/find/events",params=params)
    data = request.json()

    return data


    #
@respond_to('what is going on (.*)')
def giveme(message, something):
    match = re.search(r'in (\w+)', something)
    if match:
        location = match.group(1)
        print location
    else:
        location = 'Portland, Oregon'
    match = re.search(r'on (.*)', something)
    if match:
        topic = match.group(1)
        print match.group(1)
    else:
        topic = 'art'

    message.reply('Let me find out what is going on in {} on {} ...'.format(location, topic))
    message.send(findout(topic, location))
    message.reply('yo')



@respond_to('what is recommended on (.*)')
def giveme(message, something):
    match = re.search(r'in (\w+)', something)
    if match:
        location = match.group(1)
    else:
        location = 'Portland, Oregon'
    match = re.search(r'on (\w+)', something)
    if match:
        topic = match.group(1)
    else:
        topic = 'art'

    message.reply('Let me find out what is going on in {} on {} ...'.format(location, topic))
    message.send(findout(topic, location))
    message.reply('yo')



@respond_to('hello$', re.IGNORECASE)
def hello_reply(message):
    message.reply('hello sender!')


@respond_to('^reply_webapi$')
def hello_webapi(message):
    message.reply_webapi('hello there!', attachments=[{
        'fallback': 'test attachment',
        'fields': [
            {
                'title': 'test table field',
                'value': 'test table value',
                'short': True
            }
        ]
    }])


@respond_to('^reply_webapi_not_as_user$')
def hello_webapi_not_as_user(message):
    message.reply_webapi('hi!', as_user=False)


@respond_to('hello_formatting')
def hello_reply_formatting(message):
    # Format message with italic style
    message.reply('_hello_ sender!')


@listen_to('hello$')
def hello_send(message):
    message.send('hello channel!')


@listen_to('hello_decorators')
@respond_to('hello_decorators')
def hello_decorators(message):
    # print(message)
    # main()
    message.send('hello!')
    message.send(main())
    message.send('hello!')


@listen_to('meetup')
@respond_to('meetup')
def hello_decorators(message):
    message.send('hello!')

@listen_to('hey!')
@respond_to('hey!')
def hey(message):
    # message.reply(message)
    message.react('eggplant')


@respond_to('potato')
def redwejf(message):
    # message.reply(message)
    message.send('you said my name and potato')

@listen_to('potdato')
def redjf(message):
    # message.reply(message)
    message.send('listen potato')
