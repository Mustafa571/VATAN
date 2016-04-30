# -*- coding: utf-8 -*-
import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import requests
import re
import urlresolver
import urllib2
import xbmcaddon,xbmc
import json, base64
import hashlib
import os.path
from xml.dom import minidom
from urlparse import parse_qs

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
	return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

if mode is None:
	url = build_url({'mode': 'folder', 'foldername': 'Ulusal Kanallar'})
	li = xbmcgui.ListItem('Ulusal Kanallar', iconImage='http://www.ulusalkanal.com.tr/images/haberler/ulusal_kanal_25_31_mart_yayin_akisi_h10064.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
	url = build_url({'mode': 'folder', 'foldername': 'Maç Özetleri'})
	li = xbmcgui.ListItem('Maç Özetleri', iconImage='http://media07.ligtv.com.tr/img/news/2016/2/20/iste-bursaspor-fenerbahce-macinin-ozeti/748_416/ozet.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
	url = build_url({'mode': 'folder', 'foldername': 'Özel Kanallar'})
	li = xbmcgui.ListItem('Özel Kanallar', iconImage='http://i.huffpost.com/gen/2385860/images/o-STREAMING-facebook.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
	url = build_url({'mode': 'folder', 'foldername': 'Filmler'})
	li = xbmcgui.ListItem('Filmler', iconImage='http://profesyonellogo.com/wp-content/uploads/2012/10/sinema_LOGO.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)-facebook.jpg
	url = build_url({'mode': 'folder', 'foldername': 'Diziler'})
	li = xbmcgui.ListItem('Diziler', iconImage='https://lh5.ggpht.com/8LStBl9nroWvyl5Rfxd0f0TneWtL1Yu7HFI4-hBsr-xKhTmtKKdg_viioYfZ1hMJnO4a')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
	url = build_url({'mode': 'folder', 'foldername': 'Alman Kanalları'})
	li = xbmcgui.ListItem('Alman Kanalları', iconImage='https://andronews.de/wp-content/uploads/2014/04/screenshot-140425-153659-1024x455.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
	
	xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder':
	foldername = args['foldername'][0]
	channellogo = 'http://www.ulusalkanal.com.tr/images/haberler/ulusal_kanal_25_31_mart_yayin_akisi_h10064.jpg'
	if foldername == "Ulusal Kanallar":
		r = requests.get("https://raw.githubusercontent.com/Mustafa571/VATAN/master/Kanallar.txt")
		match = re.compile('(.+)\*(.+)').findall(r.content)
		for channel in match:
			channelname = channel[0]
			channelurl = channel[1].replace(' ',"")
			channelurl = ''.join(channelurl.splitlines())
			li = xbmcgui.ListItem(channelname, iconImage=channellogo)
			xbmcplugin.addDirectoryItem(handle=addon_handle, url=channelurl, listitem=li)
		
	elif foldername == "Maç Özetleri":
		r = requests.get("http://www.ligtv.com.tr/mac-ozetleri/spor-toto-super-lig")
		match = re.compile('data-title=.+?(?=data-player)').findall(r.content)
		for link in match:
			link = link.replace('\'',"")
			link = link.replace('data-title=',"")
			link = link.replace('Ligtv.com.tr',"")
			link = link.split('  data-video=')
			link[0] = link[0].replace('maç özeti',"")
			link[0] = link[0].replace('İY',"")
			link[1] = link[1].replace(' ',"")
			li = xbmcgui.ListItem(link[0], iconImage='http://media07.ligtv.com.tr/img/news/2016/2/20/iste-bursaspor-fenerbahce-macinin-ozeti/748_416/ozet.jpg')
			xbmcplugin.addDirectoryItem(handle=addon_handle, url=link[1], listitem=li)
			
	elif foldername == "Özel Kanallar":
		r = requests.get("https://raw.githubusercontent.com/Mustafa571/test7/master/%C3%96zel%20Kanallar.txt")
		match = re.compile('(.+)\*(.+)').findall(r.content)
		for channel in match:
			channelname = channel[0]
			channelurl = channel[1].replace(' ',"")
			channelurl = ''.join(channelurl.splitlines())
			li = xbmcgui.ListItem(channelname, iconImage='http://i.huffpost.com/gen/2385860/images/o-STREAMING-facebook.jpg')
			xbmcplugin.addDirectoryItem(handle=addon_handle, url=channelurl, listitem=li)
			
        elif foldername == "Filmler":
		r = requests.get("https://raw.githubusercontent.com/Mustafa571/VATAN/master/Filmler.txt")
		match = re.compile('(.+)\*(.+)').findall(r.content)
		for channel in match:
			channelname = channel[0]
			channelurl = channel[1].replace(' ',"")
			channelurl = ''.join(channelurl.splitlines())
			li = xbmcgui.ListItem(channelname, iconImage='http://profesyonellogo.com/wp-content/uploads/2012/10/sinema_LOGO.jpg')
			xbmcplugin.addDirectoryItem(handle=addon_handle, url=channelurl, listitem=li)
			
	elif foldername == "Diziler":
		r = requests.get("https://raw.githubusercontent.com/Mustafa571/VATAN/master/Diziler.txt")
		match = re.compile('(.+)\*(.+)').findall(r.content)
		for channel in match:
			channelname = channel[0]
			channelurl = channel[1].replace(' ',"")
			channelurl = ''.join(channelurl.splitlines())
			li = xbmcgui.ListItem(channelname, iconImage='https://lh5.ggpht.com/8LStBl9nroWvyl5Rfxd0f0TneWtL1Yu7HFI4-hBsr-xKhTmtKKdg_viioYfZ1hMJnO4a')
			xbmcplugin.addDirectoryItem(handle=addon_handle, url=channelurl, listitem=li)
			
	elif foldername == "Alman Kanalları":
		r = requests.get("https://raw.githubusercontent.com/Mustafa571/VATAN/master/Alman%20Kanallari.txt")
		match = re.compile('(.+)\*(.+)').findall(r.content)
		for channel in match:
			channelname = channel[0]
			channelurl = channel[1].replace(' ',"")
			channelurl = ''.join(channelurl.splitlines())
			li = xbmcgui.ListItem(channelname, iconImage='https://andronews.de/wp-content/uploads/2014/04/screenshot-140425-153659-1024x455.jpg')
			xbmcplugin.addDirectoryItem(handle=addon_handle, url=channelurl, listitem=li)
		
	xbmcplugin.endOfDirectory(addon_handle)
