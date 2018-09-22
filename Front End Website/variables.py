from datetime import datetime, timedelta

usr = "amitai333@gmail.com"
pwd = "Amitai321"

SCROLL_PAUSE_TIME = 1.5
prefs = {"profile.default_content_setting_values.notifications" : 2}
getName = """ return document.getElementById("pageTitle").text """
getStartingTime = """ return document.getElementsByClassName("_2ycp _5xhk")[0].children[1].textContent """
getEndingTime = """ return document.getElementsByClassName("_2ycp _5xhk")[0].children[2].textContent """
getAddr = """ return document.getElementsByClassName("_5xhp fsm fwn fcg")[1].innerText """
getPlace = """ return document.getElementsByClassName("_5xhk")[1].text """
getImage = """ return document.getElementsByClassName("uiScaledImageContainer _3ojl")[0].childNodes[0].src """
getImage2 = """ return document.getElementsByClassName("_m54 _1jto _3htz hidden_elem")[0].childNodes[0].src """
getDesc = """ return document.getElementsByClassName("_63ew")[0].textContent """
getID = """ return document.getElementsByClassName("_7ty")[0].href """
last = """ return document.body.scrollHeight """
scroll = """ window.scrollTo(0, document.body.scrollHeight); """


def eventsPageMaker(city,day):
	if (city == "haifa"):
		city = "110619208966868"
	if (city == "tel_aviv"):
		city = "106371992735156"
	days = [datetime.now().strftime('%Y-%m-%d'),
	(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
	(datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d'),
	(datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d'),
	(datetime.now() + timedelta(days=4)).strftime('%Y-%m-%d'),
	(datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d'),
	(datetime.now() + timedelta(days=6)).strftime('%Y-%m-%d'),
	(datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'),
	(datetime.now() + timedelta(days=8)).strftime('%Y-%m-%d')]

	day2 = days[day+1]
	day = days[day]
	start = 'https://www.facebook.com/events/discovery/?suggestion_token={"time":"{\\"start\\":\\"'
	start = start + day + '\\",\\"end\\":\\"' + day2 + '\\"}","city":"' + city
	start = start + '"}&acontext={"source":2,"source_dashboard_filter":"discovery","action_history":"[{\"surface\":\"dashboard\",\"mechanism\":\"dashboard_home_discovery_filter\"},{\"surface\":\"discover_filter_list\",\"mechanism\":\"surface\",\"extra_data\":{\"dashboard_filter\":\"discovery\"}}]","has_source":true}'
	print(start)
	return start
