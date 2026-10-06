HEAD='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="https://inmanjeffrey89-cell.github.io/data-tools/{slug}">
<style>body{{max-width:720px;margin:2rem auto;padding:0 1rem;font:16px/1.6 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#1a1a1a}}
h1{{font-size:1.8rem;line-height:1.2}}h2{{margin-top:2rem}}code,pre{{background:#f4f4f5;border-radius:6px}}pre{{padding:1rem;overflow:auto}}code{{padding:2px 5px}}
a{{color:#1d4ed8}}.cta{{display:inline-block;background:#1d4ed8;color:#fff;padding:.6rem 1rem;border-radius:8px;text-decoration:none;margin:.3rem .3rem .3rem 0}}
.muted{{color:#666}}nav a{{margin-right:1rem}}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #e5e5e5;padding:.5rem}}</style></head><body>
<nav class=muted><a href="/data-tools/">All tools</a></nav>'''
FOOT='<hr><p class=muted>Open-source CLIs (MIT) + hosted versions on Apify. Built by an indie dev. Found a bug? Open a GitHub issue.</p></body></html>'

TOOLS=[
 dict(slug='youtube-transcript', title='YouTube Transcript API (free + bulk) — no API key',
   desc='Get YouTube video transcripts as text or SRT without the YouTube Data API. Free CLI, or hosted for bulk.',
   h1='Get a YouTube transcript without the YouTube Data API',
   lead='The official YouTube Data API does not return transcript text for videos you do not own. Here are two ways that do — a free command-line tool, and a hosted version for bulk jobs.',
   npm='yt-transcript-cli', cli='npx yt-transcript-cli "https://www.youtube.com/watch?v=dQw4w9WgXcQ"',
   actor='youtube-transcript-scraper', actordesc='a list of video URLs in, clean text + timestamped segments + SRT out, pay only for transcripts actually delivered (videos with no captions are free)',
   use='feeding videos into an LLM/RAG pipeline, building a searchable archive, generating subtitles',
   limits='A transcript only exists if the video has captions on YouTube. Private and age-restricted videos cannot be read.'),
 dict(slug='youtube-channel-transcripts', title='Download every transcript from a YouTube channel',
   desc='Pull transcripts for every video in a YouTube channel or playlist, as text + SRT. One call.',
   h1='Download transcripts for a whole YouTube channel or playlist',
   lead='Point it at a channel or playlist and get every video transcript — no need to collect the URLs yourself.',
   npm=None, cli=None,
   actor='youtube-channel-transcript-scraper', actordesc='a channel URL / @handle / playlist in, every video transcript out (text + SRT), pay per delivered transcript, no-caption videos free',
   use='mining a creator back-catalogue for an LLM, competitive content analysis, bulk subtitle export',
   limits='Returns a channel’s uploads newest-first. Members-only and private videos are skipped.'),
 dict(slug='google-trends-api', title='Google Trends API — interest over time as JSON/CSV',
   desc='Google Trends interest-over-time for any keyword as clean JSON. Free CLI or hosted at scale.',
   h1='A Google Trends "API" that actually returns data',
   lead='Google Trends has no official API, and most quick scripts return empty because of a session handshake. These handle it.',
   npm='gtrends-cli', cli='npx gtrends-cli "bitcoin" US "today 3-m"',
   actor='google-trends-scraper', actordesc='any list of keywords in, interest-over-time points as clean JSON out, pay only for keywords that return data',
   use='market and niche research, SEO seasonality, retail-attention signals on tickers',
   limits='Values are Google’s relative 0–100 index per keyword, not absolute search volumes.'),
 dict(slug='keyword-research-api', title='Free keyword research from Google/YouTube/Amazon autocomplete',
   desc='Hundreds of real keyword ideas per seed from Google, YouTube, Amazon and Bing autocomplete. No API key.',
   h1='Keyword ideas from the autocomplete people actually type',
   lead='Autocomplete endpoints are open and return the real phrases searchers use. This mines them at depth.',
   npm='keyword-ideas-cli', cli='npx keyword-ideas-cli "coffee maker" google deep',
   actor='keyword-research-scraper', actordesc='seed terms in, hundreds of deduped keyword ideas per seed out across Google/YouTube/Amazon/Bing, pay per seed, empty seeds free',
   use='SEO content planning, PPC keyword lists, Amazon product research',
   limits='These are autocomplete suggestions (what people search), not monthly volume numbers — pair with Google Trends to gauge demand.'),
 dict(slug='google-play-reviews-api', title='Google Play reviews API — bulk export, no dev account',
   desc='Download Google Play Store reviews for any Android app as JSON. Free CLI or hosted at scale.',
   h1='Export Google Play Store reviews without a developer account',
   lead='Rating, text, version, author, date — for any app, as clean JSON.',
   npm='play-reviews-cli', cli='npx play-reviews-cli com.instagram.android 200',
   actor='google-play-reviews-scraper', actordesc='app package names in, reviews out (rating/text/version/date), pay per review, apps with no reviews free',
   use='monitoring your own app’s 1-star reviews, competitor review mining, sentiment analysis',
   limits='Reviews are per country — run several storefronts for worldwide coverage.'),
 dict(slug='app-store-reviews-api', title='App Store reviews API — bulk iOS reviews as JSON',
   desc='Download Apple App Store reviews for any app as JSON. No developer account.',
   h1='Export Apple App Store reviews without a developer account',
   lead='Rating, title, text, app version, author, date — for any iOS app.',
   npm=None, cli=None,
   actor='app-store-reviews-scraper', actordesc='app IDs/URLs in, reviews out, pay per review, apps with no reviews free',
   use='app teams tracking regressions by version, competitor research, review sentiment',
   limits='Apple’s public feed returns up to ~500 most-recent reviews per app per country.'),
]

def page(t):
    s=HEAD.format(title=t['title'],desc=t['desc'],slug=t['slug'])
    s+=f"<h1>{t['h1']}</h1><p>{t['lead']}</p>"
    if t['npm']:
        s+=f"<h2>Free: the command-line tool</h2><p>No signup, no key — run it with <code>npx</code>:</p><pre>{t['cli']}</pre>"
        s+=f'<p><a class=cta href="https://github.com/inmanjeffrey89-cell/{t["npm"]}">View on GitHub</a><a class=cta href="https://www.npmjs.com/package/{t["npm"]}">npm</a></p>'
    s+=f"<h2>At scale: the hosted version</h2><p>For bulk jobs, scheduling, and reliability (rotating proxies, retries), the hosted version takes {t['actordesc']}.</p>"
    s+=f'<p><a class=cta href="https://apify.com/beacondata/{t["actor"]}">Open on Apify</a></p>'
    s+=f"<h2>Common uses</h2><p>{t['use']}.</p><h2>Honest limitations</h2><p>{t['limits']}</p>"
    s+=FOOT
    return s

import os
for t in TOOLS:
    open(t['slug']+'.html','w').write(page(t))

# index
idx=HEAD.format(title='Free data tools — scrapers & APIs with no API key',desc='Free command-line tools and hosted scrapers: YouTube transcripts, Google Trends, keyword research, app reviews. No API key.',slug='')
idx=idx.replace('<nav class=muted><a href="/data-tools/">All tools</a></nav>','')
idx+='<h1>Free data tools &amp; scrapers</h1><p>Open-source command-line tools (run with <code>npx</code>, no API key) plus hosted versions for bulk jobs. Pick a problem:</p><ul>'
for t in TOOLS:
    idx+=f'<li><a href="/data-tools/{t["slug"]}">{t["h1"]}</a></li>'
idx+='</ul>'+FOOT
open('index.html','w').write(idx)
print('generated', len(TOOLS)+1, 'pages')
