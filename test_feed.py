import xml.etree.ElementTree as ET
from datetime import datetime, timezone

tree = ET.parse("gh_28ac995bf1b5.xml")
root = tree.getroot()
channel = root.find("channel")

item = ET.SubElement(channel, "item")
title = ET.SubElement(item, "title")
title.text = "【测试】这是一条新的测试文章，用于验证 Inoreader 抓取机制"

link = ET.SubElement(item, "link")
link.text = "https://mp.weixin.qq.com/test_article_123"

guid = ET.SubElement(item, "guid")
guid.text = "https://mp.weixin.qq.com/test_article_123_unique"

desc = ET.SubElement(item, "description")
desc.text = "如果您看到了这篇文章，说明 Inoreader 订阅和解析完全正常！之前的文章没有显示是因为您退订重订后，Inoreader 去重了旧文章。"

pubDate = ET.SubElement(item, "pubDate")
pubDate.text = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')

tree.write("gh_28ac995bf1b5.xml", encoding="utf-8", xml_declaration=True)
