# importing speedtest module
import speedtest

s = speedtest.Speedtest()

option = int(input("""What do you want to know :
	1) upload speed
	2) download speed
	3) ping"""))

if option == 1:
	print(s.upload())

elif option==2:
	print(s.download())

elif option ==3:
	s.getserver(s)
	print(s.results.ping)

else:
	print("Invalid option")