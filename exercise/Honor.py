import requests
from lxml import etree
import re
import threading
from queue import Queue
import os
from time import sleep
import json


class HeroSpider():
	def __init__(self):
		self.start_url = "https://pvp.qq.com/web201605/js/herolist.json"
		self.url = "https://pvp.qq.com/web201605/herodetail/{}.shtml"
		self.headers = {"User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
		self.hero_url_queue = Queue()
		self.skin_queue = Queue()
	
	# 获取英雄url列表
	def get_hero_list(self):
		url = self.start_url
		res = requests.get(url, headers=self.headers).content
		res = json.loads(res)
		for i in res:
			url = self.url.format(i["ename"])
			self.hero_url_queue.put(url)
	
	# 访问英雄页面，获取信息
	def get_skin_list(self):
		while True:
			# 1. 从queue获取url
			url = self.hero_url_queue.get()
			# 2. 访问该url, 获取信息
			response = requests.get(url,
			                        headers=self.headers).content.decode('gbk')
			response = etree.HTML(response)
			# 3. 将数据放入skin_queue队列
			item = {}
			item["hero_name"] = response.xpath("//h2[@class='cover-name']/text()")[0]
			item["hero_id"] = response.xpath("//span[@class='hidden']/text()")[0]
			skin_name_list = str(response.xpath("//ul[@class='pic-pf-list pic-pf-list3']/@data-imgname")).split("|")
			# 格式化皮肤名称
			item["skin_name_list"] = [re.findall(r'\[?\'?(.*)&.*', skin_name)[0] for skin_name in skin_name_list]
			# 4. 将item添加到队列
			self.skin_queue.put(item)
			# 5. 任务完成，hero_queue队列-1
			self.hero_url_queue.task_done()
	
	#  保存图片的函数
	def save_skin(self):
		while True:
			# 1. 从queue获取数据
			item = self.skin_queue.get()
			# 2. 创建英雄文件夹
			os.mkdir("heros/" + item["hero_name"])
			# 2. 构造url和文件名等数据
			for skin_name in item["skin_name_list"]:
				print(skin_name)
				skin_id = item["skin_name_list"].index(skin_name) + 1
				skin_url = "http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/%s/%s-bigskin-%d.jpg" % (item["hero_id"], item["hero_id"], skin_id)
				skin_img = requests.get(skin_url, headers=self.headers)
				with open("heros/" + item["hero_name"] + "/" + skin_name +'.jpg', "wb") as f:
					f.write(skin_img.content)
			# 3. 任务完成，skin_queue队列-1
			self.skin_queue.task_done()
	
	def run(self):
		os.mkdir("heros")
		
		# 一. 构建人物列表
		t_list = []
		
		# 1. 构建各个英雄的链接
		t_get_hero_list = threading.Thread(target=self.get_hero_list)
		t_list.append(t_get_hero_list)
		
		# 2. 获取英雄皮肤信息
		for i in range(5):
			t_get_skin_list = threading.Thread(target=self.get_skin_list)
			t_list.append(t_get_skin_list)
		
		# 3. 遍历skin_queue队列，保存图片
		for i in range(5):
			t_save_skin = threading.Thread(target=self.save_skin)
			t_list.append(t_save_skin)
		
		# 二. 遍历任务，启动t.start()
		for t in t_list:
			t.setDaemon(True)  # 设置成守护进程，随主进程关闭而关闭； 解决函数中while True跳出问题
			t.start()
		
		sleep(10)  #  让主进程休眠10s，等第一个页面获取，因为在获取之前队列还是空队列，此时不能让程序认为队列是完成状态, 网速不好的可以多睡一会
		for q in [self.hero_url_queue, self.skin_queue]:
			q.join()  # 阻塞主线程，等任务队列完成之后，再完成


if __name__ == "__main__":
	hero = HeroSpider()
	hero.run()
