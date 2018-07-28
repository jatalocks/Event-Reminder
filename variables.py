haifa = "110619208966868"
tel_aviv = "106371992735156"
usr = "amitai333@gmail.com"
pwd = "Amitai321"
url1 = 'https://www.facebook.com/events/discovery/?suggestion_token={"time":"today","city":"'
url2 = url1 + tel_aviv
url = url2 + '"}&acontext={"source":2,"source_dashboard_filter":"discovery","action_history":"[{\"surface\":\"dashboard\",\"mechanism\":\"dashboard_home_discovery_filter\"},{\"surface\":\"discover_filter_list\",\"mechanism\":\"surface\",\"extra_data\":{\"dashboard_filter\":\"discovery\"}}]","has_source":true}'

SCROLL_PAUSE_TIME = 1.5
prefs = {"profile.default_content_setting_values.notifications" : 2}

getName = """ return document.getElementById("pageTitle").text """
getStartingTime = """ return document.getElementsByClassName("_164e")[0].nextSibling.nextSibling.innerText """
getEndingTime = """ return document.getElementsByClassName("_164e")[0].nextSibling.nextSibling.nextSibling.nextSibling.innerText """
getAddr = """ return document.getElementsByClassName("_5xhp fsm fwn fcg")[1].innerText """
getPlace = """ return document.getElementsByClassName("_5xhk")[1].text """
getImage = """ return document.getElementsByClassName("uiScaledImageContainer _3ojl")[0].childNodes[0].src """
getImage2 = """ return document.getElementsByClassName("_m54 _1jto _3htz hidden_elem")[0].childNodes[0].src """

getID = """ return document.getElementsByClassName("_7ty")[0].href """
last = """ return document.body.scrollHeight """
scroll = """ window.scrollTo(0, document.body.scrollHeight); """
styling = """ <style>
html,
body {
	height: 100%;
}

body {
	margin: 0;
	background: linear-gradient(45deg, #49a09d, #5f2c82);
	font-family: sans-serif;
	font-weight: 100;
  margin: 0;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

.container {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
}

table {
	width: 100%;
    height: 100%;
	border-collapse: collapse;
	box-shadow: 0 0 20px rgba(0,0,0,0.1);
}

th,
td {
	padding: 15px;
	background-color: rgba(255,255,255,0.2);
	color: #fff;
  word-wrap: break-word;
}

th {
	text-align: left;
}

thead {
	th {
		background-color: #55608f;
	}
}
</style>
"""
