import twitter
  api = twitter.Api()
  statuses = api.GetUserTimeline('collowski')
  for tweet in statuses:
    print tweet
