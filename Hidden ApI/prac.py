import requests

url = "https://api.nike.com/cic/browse/v2"

querystring = {"queryid":"products","anonymousId":"C9117A9AF38DFB1448D7C6919F8BE4F0","country":"gb","endpoint":"/product_feed/rollup_threads/v2?filter=marketplace(GB)&filter=language(en-GB)&filter=employeePrice(true)&filter=attributeIds(16633190-45e5-4830-a068-232ac7aea82c,0f64ecc7-d624-4e91-b171-b83a03dd8550)&anchor=24&consumerChannelId=d9a5bc42-4b9c-4976-858a-f159cf99c647&count=5","language":"en-GB","localizedRangeStr":"{lowestPrice}—{highestPrice}"}

payload = ""
headers = {
    "cookie": "_abck=C54E82D4B5A3D211CF787B20491B9E05~-1~YAAQVh0gF9ub3jONAQAAIhPpQAuuEMbf%2FTBwrCzIma3VQYWfTJ17hG%2BmfWPGPJlzIHfPprwL4%2FkswMOflpRllLj0z6%2BwO4p%2Bbz0CtaVX%2BWL2qefQNmSIAo6jiKH7pQ3HiP%2Bg%2FXuunxpzTIzWLZvMB6MTFnfFre%2FPPi51cjRW4%2Fp6ydPhN7sK0FqjHOSj67vf82KCPayJKZc9j%2B1d%2BuSP0MyDFEMme1bT67x12cA1XzkFRHLoUfgo0gpi%2BBx7KTVCBId%2B3Iqm4mWcOMVhr9TJLxVevSHI5kXCfoocp7jmgxTEm0YQg1yR2zwRg2ae8nk0D4XoMcKAGxavtPr7uPBJ%2B3hOu0stagCPYVvE1JFdNEwcv0vbm4TZ5c%2BqY9ExEmS8qixbgP0u5cUE9q8JFySJga3lerHPfBdJrg%3D%3D~-1~-1~1706194517; bm_sz=0C94DF2499229521FAD9B82912B0A5EA~YAAQVh0gF9yb3jONAQAAIhPpQBY%2BijGqk4CSc8lduuEGSm2DVye5Ojm8zMi1ctRgzJpnrRbbMJVbeQHfwTc0fEAY%2F1RHK1mgP3LRaXqUEWquRfbiV6gY1vBdxatdpwHmQ8m%2BXOwRZ6VCI0%2BUlfeJ63cM8JGRQNZOnTsKBG8CEz0SFw9QxmuNxMQK%2B%2F19ZaagIpXtSOuQz2m7IZifN3UNx3YdTXyuva7aWqFL4KWqyok1nrygBtd3AK9ziQAJXFYLKQRrvM2aJjx7ZUfuN8FQ26MOrVBhUfbouTENEwYI7BrC6so7ZQrpD3y1ArY5y8EfSbWRpEGsv%2BuSNeIE6I9qTevkUCdf3RFD%2BMzYW8Di%2BIuK7IaTKEX8JJ4CaWxyjnAcBG8VTLoVNI8TOaYvukBQMf2bQPCZLotxcXLUPmvxwXr49w%3D%3D~3223877~3684165",
    "User-Agent": "insomnia/8.6.0"
}

r = requests.request("GET", url, data=payload, headers=headers, params=querystring)

info = r.json()

print(info['data']['products'])