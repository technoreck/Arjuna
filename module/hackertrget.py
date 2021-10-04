
from data.data import HEADERS, api_load
import json
import re
import socket
import requests
from prettytable import PrettyTable

space = "   "
apihack = "https://api.hackertarget.com/{}/?q={}"
iplookurl = "https://ipgeolocation.abstractapi.com/v1/?api_key={}&ip_address={}"


def apihk(opt,x):

    if not x: return
    if x.split(".")[0].isnumeric(): x = socket.gethostbyname(x)
    else: pass
    req = requests.get(apihack.format(opt,x),stream=True,headers=HEADERS)
    for res in req.iter_lines():
        print(f"{space}{res.decode('utf-8')}")
    return



def getdata(url):
	r=requests.get(url)
	return r.text

def splited(x):
    x= x.split('_')
    code_con={ 
	'+93'  :'AF',
	'+355':'AL',
	'+213':'DZ',
	'+376':'AD',
	'+244':'AO',
	'+672':'AQ',
	'+54'  :'AR',
	'+374':'AM',
    '+297':'AW',
	'+61'  :'AU',
	'+43'  :'AT',
	'+994':'AZ',
	'+973':'BH',
	'+880':'BD',
	'+375':'BY',
    '+32'  :'BE',
	'+501':'BZ',
	'+229':'BJ',
	'+975':'BT',
	'+591':'BO',
	'+387':'BA',
	'+267':'BW',
	'+55'  :'BR',
	'+246':'IO',
	'+673':'BN',
	'+359':'BG',
	'+226':'BF',
    '+257':'BI',
    '+855':'KH',
	'+61'  :'CX',
	'+61'  :'CC',
	'+57'  :'CO',
	'+269':'KM',
	'+682':'CK',
	'+506':'CR',
	'+385':'HR',
	'+53'  :'CU',
	'+599':'CW',
	'+357':'CY',
	'+420':'CZ',
	'+243':'CD',
    '+45'  :'DK',
	'+253':'DJ',
	'+670':'TL',
	'+593':'EC',
	'+20'  :'EG',
	'+503':'SV',
	'+240':'GQ',
	'+291':'ER',
    '+372':'EE',
	'+251':'ET',
	'+500':'FK',
	'+298':'FO',
	'+679':'FJ',
	'+358':'FI',	
	'+44-1481':'GG',
	'+44-1624':'IM',
	'+1-684':'AS', 
	'+1-264':'AI', 
	'+1-268':'AG', 
	'+1-242':'BS',
	'+1-246':'BB', 
	'+1-441':'BM',
	'+1-284':'VG', 
	'+1-345':'KY',
	'+1-473':'GD', 
	'+1-671':'GU', 
	'+1-876':'JM', 
	'+1-664':'MS', 
	'+1-670':'MP',
	'+1-869':'KN',
	'+1-758':'LC',
	'+1-784':'VC',
	'+1-721':'SX',
	'+1-340':'VI', 
	'+1-649':'TC', 
	'+93'  :'AF',
	'+355':'AL',
	'+213':'DZ',
	'+376':'AD',
	'+244':'AO',
	'+672':'AQ',
	'+54'  :'AR',
	'+374':'AM',
    '+297':'AW',
	'+61'  :'AU',
	'+43'  :'AT',
	'+994':'AZ',
	'+973':'BH',
	'+880':'BD',
	'+375':'BY',
    '+32'  :'BE',
	'+501':'BZ',
	'+229':'BJ',
	'+975':'BT',
	'+591':'BO',
	'+387':'BA',
	'+267':'BW',
	'+55'  :'BR',
	'+246':'IO',
	'+673':'BN',
	'+359':'BG',
	'+226':'BF',
    '+257':'BI',
    '+855':'KH',
	'+61'  :'CX',
	'+61'  :'CC',
	'+57'  :'CO',
	'+269':'KM',
	'+682':'CK',
	'+506':'CR',
	'+385':'HR',
	'+53'  :'CU',
	'+599':'CW',
	'+357':'CY',
	'+420':'CZ',
	'+243':'CD',
    '+45'  :'DK',
	'+253':'DJ',
	'+670':'TL',
	'+593':'EC',
	'+20'  :'EG',
	'+503':'SV',
	'+240':'GQ',
	'+291':'ER',
    '+372':'EE',
	'+251':'ET',
	'+500':'FK',
	'+298':'FO',
	'+679':'FJ',
	'+358':'FI',
	'+33'  :'FR',
	'+689':'PF',
	'+241':'GA',
	'+220':'GM',
    '+995':'GE',
	'+49'  :'DE',
	'+233':'GH',
	'+350':'GI',
	'+30'  :'GR',
	'+299':'GL',
	'+502':'GT',
	'+224':'GN',
	'+245':'GW',
	'+592':'GY',
	'+509':'HT',
	'+504':'HN',
	'+852':'HK',
	'+36'  :'HU',
	'+354':'IS',
    '+91'  :'IN',
	'+62'  :'ID',
	'+98'  :'IR',
	'+964':'IQ',
	'+353':'IE',
	'+972':'IL',
	'+39'  :'IT',
    '+225':'CI',
	'+81'  :'JP',
	'+962':'JO',
	'+7'   :'KZ',
	'+254':'KE',
	'+686':'KI',
	'+383':'XK',
	'+965':'KW',
	'+996':'KG',
	'+856':'LA',
	'+371':'LV',
	'+961':'LB',
	'+266':'LS',
	'+231':'LR',
	'+218':'LY',
	'+423':'LI',
	'+370':'LT',
	'+352':'LU',
	'+853':'MO',
	'+389':'MK',
	'+261':'MG',
	'+265':'MW',
	'+60'  :'MY',
	'+960':'MV',
	'+223':'ML',
	'+356':'MT',
	'+692':'MH',
	'+222':'MR',
	'+230':'MU',
	'+262':'YT',
	'+52'  :'MX',
	'+691':'FM',
	'+373':'MD',
	'+377':'MC',
	'+976':'MN',
	'+382':'ME',
	'+212':'MA',
	'+258':'MZ',
	'+95'  :'MM',
	'+264':'NA',
	'+674':'NR',
	'+977':'NP',
	'+31'  :'NL',
	'+599':'AN',
	'+687':'NC',
	'+64'  :'NZ',
	'+505':'NI',
	'+227':'NE',
    '+234':'NG',
    '+683':'NU',
	'+850':'KP',
	'+47'  :'NO',
	'+968':'OM',
	'+92'  :'PK',
	'+680':'PW',
	'+970':'PS',
	'+507':'PA',
	'+675':'PG',
	'+595':'PY',
	'+51'  :'PE',
	'+63'  :'PH',
	'+64'  :'PN',
	'+48'  :'PL',
	'+351':'PT',
    '+974':'QA',
	'+242':'CG',
    '+262':'RE',
	'+40'  :'RO',
	'+7'   :'RU',
	'+250':'RW',
	'+590':'BL',
	'+290':'SH',
	'+590':'MF',
	'+508':'PM',
	'+685':'WS',
	'+378':'SM',
	'+239':'ST',
	'+966':'SA',
	'+221':'SN',
	'+381':'RS',
	'+248':'SC',
	'+232':'SL',
	'+65'  :'SG',
	'+421':'SK',
	'+386':'SI',
	'+677':'SB',
	'+252':'SO',
	'+27'  :'ZA',
    '+82'  :'KR',
	'+211':'SS',
	'+34'  :'ES',
	'+94'  :'LK',
	'+249':'SD',
	'+597':'SR',
	'+47'  :'SJ',
	'+268':'SZ',
	'+46'  :'SE',
	'+41'  :'CH',
	'+963':'SY',
	'+886':'TW',
	'+992':'TJ',
	'+255':'TZ',
	'+66'  :'TH',
	'+228':'TG',
	'+690':'TK',
	'+676':'TO',
	'+216':'TN',
	'+90'  :'TR',
	'+993':'TM',
	'+688':'TV',
	'+256':'UG',
	'+380':'UA',
	'+971':'AE',
	'+44'  :'GB',
	'+1'   :'US',
	'+598':'UY',
	'+998':'UZ',
    '+678':'VU',
	'+379':'VA',
	'+58'  :'VE',
	'+84'  :'VN',
	'+681':'WF',
	'+212':'EH',
	'+967':'YE',
	'+260':'ZM',
	'+263':'ZW',
	'+33':'FR',
	'+689':'PF',
	'+241':'GA',
	'+220':'GM',
    '+995':'GE',
	'+49'  :'DE',
	'+233':'GH',
	'+350':'GI',
	'+30'  :'GR',
	'+299':'GL',
	'+502':'GT',
	'+224':'GN',
	'+245':'GW',
	'+592':'GY',
	'+509':'HT',
	'+504':'HN',
	'+852':'HK',
	'+36'  :'HU',
	'+354':'IS',
    '+91'  :'IN',
	'+62'  :'ID',
	'+98'  :'IR',
	'+964':'IQ',
	'+353':'IE',
	'+972':'IL',
	'+39'  :'IT',
    '+225':'CI',
	'+231':'LR',
	'+218':'LY',
	'+423':'LI',
	'+370':'LT',
	'+352':'LU',
	'+853':'MO',
	'+389':'MK',
	'+261':'MG',
	'+265':'MW',
	'+60'  :'MY',
	'+960':'MV',
	'+223':'ML',
	'+356':'MT',
	'+692':'MH',
	'+222':'MR',
	'+230':'MU',
	'+262':'YT',
	'+52'  :'MX',
	'+691':'FM',
	'+373':'MD',
	'+377':'MC',
	'+976':'MN',
	'+382':'ME',
	'+212':'MA',
	'+258':'MZ',
	'+95'  :'MM',
	'+264':'NA',
	'+674':'NR',
	'+977':'NP',
	'+31'  :'NL',
	'+599':'AN',
	'+687':'NC',
	'+64'  :'NZ',
	'+505':'NI',
	'+227':'NE',
    '+234':'NG',
    '+683':'NU',
	'+850':'KP',
	'+47'  :'NO',
	'+968':'OM',
	'+92'  :'PK',
	'+680':'PW',
	'+970':'PS',
	'+507':'PA',
	'+675':'PG',
	'+595':'PY',
	'+51'  :'PE',
	'+63'  :'PH',
	'+64'  :'PN',
	'+48'  :'PL',
	'+351':'PT',
    '+974':'QA',
	'+242':'CG',
    '+262':'RE',
	'+40'  :'RO',
	'+7'   :'RU',
	'+250':'RW',
	'+590':'BL',
	'+290':'SH',
	'+590':'MF',
	'+508':'PM',
	'+685':'WS',
	'+378':'SM',
	'+239':'ST',
	'+966':'SA',
	'+221':'SN',
	'+381':'RS',
	'+248':'SC',
	'+232':'SL',
	'+65'  :'SG',
	'+421':'SK',
	'+386':'SI',
	'+677':'SB',
	'+252':'SO',
	'+27'  :'ZA',
    '+82'  :'KR',
	'+211':'SS',
	'+34'  :'ES',
	'+94'  :'LK',
	'+249':'SD',
	'+597':'SR',
	'+47'  :'SJ',
	'+268':'SZ',
	'+46'  :'SE',
	'+41'  :'CH',
	'+963':'SY',
	'+886':'TW',
	'+992':'TJ',
	'+255':'TZ',
	'+66'  :'TH',
	'+228':'TG',
	'+690':'TK',
	'+676':'TO',
	'+216':'TN',
	'+90'  :'TR',
	'+993':'TM',
	'+688':'TV',
	'+256':'UG',
	'+380':'UA',
	'+971':'AE',
	'+44'  :'GB',
	'+1'   :'US',
	'+598':'UY',
	'+998':'UZ',
    '+678':'VU',
	'+379':'VA',
	'+58'  :'VE',
	'+84'  :'VN',
	'+681':'WF',
	'+212':'EH',
	'+967':'YE',
	'+260':'ZM',
	'+263':'ZW'
    }

    return code_con[x[0]],x[1]


def phone(tobesplited):
    country,number = splited(tobesplited)
    data=getdata('http://apilayer.net/api/validate?access_key='+api_load('Numverify')+'&number='+number+'&country_code='+country+'&format=1')
    json_data = json.loads(data)
    print(f''' 
        valid                   : {json_data['valid']}
        Number                  : {json_data['number']}
        Local_Format            : {json_data['local_format']}
        International_format    : {json_data['international_format']}
        Country_prefix          : {json_data['country_prefix']}
        Country_code            : {json_data['country_code']}
        Country_name            : {json_data['country_name']}
        Location                : {json_data['location']}
        Carrier                 : {json_data['carrier']}
        Line_type               : {json_data['line_type']}
    ''')


def apibanner(x):

    if not x: return
    if x.split(".")[0].isnumeric(): x = socket.gethostbyname(x)
    else: pass
    print("-"*44)
    req = requests.get(apihack.format('bannerlookup',x),stream=True)
   # print(req.text)
    json_data = json.loads(req.text)
    t = PrettyTable(['Banner data ','Information'])

    try: 
        t.add_row(['Ip',json_data['ip']]) 
    except: pass
    t.add_row(['Http_80'," "])
    t.add_row(['---------',"----------"])
    try:
        t.add_row(['Title',json_data['http80']['title']])
    except: pass
    try:
        t.add_row(['Server',json_data['http80']['server']])
    except: pass
    try:
        t.add_row(['Apps',json_data['http80']['apps']])
    except: pass
    t.add_row(["---------","-----------"])  
    t.add_row(['',''])
    t.add_row(['Http_443'," "])
    t.add_row(["---------","-----------"])
    try:
        t.add_row(['Title',json_data['https443']['title']])
    except: pass
    try:
        t.add_row(['Server',json_data['https443']['server']])
    except: pass
    try:
        t.add_row(['Apps',json_data['https443']['apps']])
    except: pass
    try:
        t.add_row(['Apps',json_data['https443']['generator']])
    except: pass
    try:
        t.add_row(['Apps',json_data['https443']['cn']])
    except:pass
    t.add_row(["---------","-----------"])
    try:
        t.add_row(["SSH",json_data['ssh']])
    except: pass
    

    print(t)


def iplookup(x):
	try:
		url = iplookurl.format(api_load('Abstract'),socket.gethostbyname(x))
		req = requests.get(url,headers=HEADERS).json()
		t = PrettyTable(['Data','Information'])
		if req['ip_address']:t.add_row(['Ip address',req['ip_address']])
		if req['city']:	t.add_row(['City',req['city']])
		if req['region']:t.add_row(['Region',req['region']])	
		if req['postal_code']:t.add_row(['Postal code',req['postal_code']])	
		if req['country']:t.add_row(['Country',req['country']])	
		if req['continent']:t.add_row(['Continent',req['continent']])	
		if req['longitude']:t.add_row(['Longitude',req['longitude']])	
		if req['latitude']:t.add_row(['Latitude',req['latitude']])	
		data2=req['security']
		if data2['is_vpn']:
			t.add_row(['Vpn Service','Yes'])
		else: 
			t.add_row(["Vpn Service","No"])
		t.add_row([" "," "])	
		data2 = req['connection']
		if data2['isp_name']:t.add_row(['Isp name',data2['isp_name']])
		if data2['organization_name']:t.add_row(['Organization name',data2['organization_name']])
		if data2['autonomous_system_number']:t.add_row(['AS Number',data2['autonomous_system_number']])
		if data2['autonomous_system_organization']:t.add_row(['AS Organization',data2['autonomous_system_organization']])
		if data2['connection_type']:t.add_row(['Connection type',data2['connection_type']])
	except socket.gaierror:
		print("\033[91m Invalid Url Found \033[0m")
		return

	print(t)