# Meetup Guru

- A tool build off of https://github.com/lins05/slackbot
- and https://github.com/trendct/walkthroughs/blob/master/0315-meetup-analysis

If you ask him `@meetup-guru what is going on in NY on data science and python`. He will parse `NY` after `in` and `data science and python` after the `on` word using regex into a get request that looks like # eg http://api.meetup.com/find/events?lon=-74.0059&key=******&lat=40.7128&text=datascience+python
# He will return top 5 recommended events (meetup url)

# Future
1. Use the google maps api to make other locations available.
1. Return the local meeetups by meetupID
2. Look at each and count # of RSVPs https://api.meetup.com/2/rsvps?&sign=true&photo-host=public&event_id=234481909&page=20
