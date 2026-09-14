"""RSS feed generator — stdlib XML only, no lxml."""

import xml.etree.ElementTree as ET
from datetime import datetime


def generate_feed(pages: list, title: str = 'Site', base_url: str = '') -> str:
    rss = ET.Element('rss', version='2.0')
    channel = ET.SubElement(rss, 'channel')
    ET.SubElement(channel, 'title').text = title
    ET.SubElement(channel, 'lastBuildDate').text = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    for page in pages:
        item = ET.SubElement(channel, 'item')
        ET.SubElement(item, 'title').text = page.get('title', '')
        ET.SubElement(item, 'link').text = f"{base_url}/{page.get('path', '')}"
    return ET.tostring(rss, encoding='unicode', xml_declaration=True)
