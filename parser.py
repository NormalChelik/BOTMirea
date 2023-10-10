import dateutil
import requests
from icalendar import Calendar
from dateutil.parser import parse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Date" : "Tue, 03 Oct 2023 22:04:46 GMT"
}

variable = requests.Session()
response = variable.get("https://schedule-of.mirea.ru/_next/data/JlnyE2wBwvqeBeu7hohS5/index.json?s=1_820", headers = headers)
response.encoding = 'utf-8'

raspisanue = response.json().get("pageProps")["scheduleLoadInfo"][0]["iCalContent"]
calendar = Calendar.from_ical(raspisanue)

for event in calendar.walk('VEVENT'):
    event_name = event['SUMMARY']
    event_start = parse(event['DTSTART'].to_ical())
    event_end = parse(event['DTEND'].to_ical())
    event_location = event['LOCATION']
    print(event_name, event_start, event_end, event_location)