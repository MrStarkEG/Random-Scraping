import asyncio

from pyppeteer import launch
from time import sleep


async def main():
    browser = await launch(headless=False, executablePath="C:/Program Files/Google/Chrome/Application/chrome.exe")
    page = await browser.newPage()

    await page.goto('https://speedtest.net', {'waitUntil': 'networkidle2'})

    await page.waitForSelector('.start-text', {'timeout': 2000})
    await page.click('.start-text')

    await page.wait(60000)

    download_speed = await page.waitForSelector('.download-speed', {'timeout': 120000})
    print("Ur down speed = {}".format(download_speed.text))
    upload_speed = await page.waitForSelector('.downloadupload-speed', {'timeout': 120000})
    print("Ur up speed = {}".format(upload_speed.text))

    await browser.close()

asyncio.run(main())
