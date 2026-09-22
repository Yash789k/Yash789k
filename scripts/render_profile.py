#!/usr/bin/env python3
"""Render repository-owned profile visuals from public GitHub metadata only."""
import argparse
from collections import Counter
from datetime import datetime, timezone
from html import escape
import json
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
USER = 'Yash789k'
COLORS = ['#52f5a3', '#68d8ff', '#c9a0ff', '#ffb86b', '#ff79b0', '#8493a9']


def svg(name, width, height, body, title, desc=''):
    markup = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc or title)}</desc>
<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#0c1522"/><stop offset="1" stop-color="#111225"/></linearGradient><pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M 28 0 L 0 0 0 28" fill="none" stroke="#26344c" stroke-opacity=".35"/></pattern></defs>
<style>text{{font-family:'SFMono-Regular',Consolas,'Liberation Mono',monospace}} .muted{{fill:#9aaec5}} .pulse{{animation:pulse 3s ease-in-out infinite}} .cursor{{animation:blink 1.3s steps(2,end) infinite}} .flow{{stroke-dasharray:8 16;animation:flow 6s linear infinite}} @keyframes blink{{50%{{opacity:0}}}} @keyframes pulse{{50%{{opacity:.35}}}} @keyframes flow{{to{{stroke-dashoffset:-144}}}} @media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style>
<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="16" fill="url(#bg)" stroke="#2a3b50"/>
{body}</svg>'''
    ET.fromstring(markup)
    (ASSETS / name).write_text(markup + '\n')


def text(x, y, value, size=18, color='#e9f1fc', extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" {extra}>{escape(str(value))}</text>'


def static_assets():
    body = '<rect x="1" y="1" width="918" height="358" rx="16" fill="url(#grid)"/>'
    body += '<path d="M0 45 H920" stroke="#2a3b50"/>'
    for i, color in enumerate(['#ff6b8a', '#ffd166', '#52f5a3']):
        body += f'<circle cx="{25+i*21}" cy="24" r="5" fill="{color}"/>'
    body += text(98, 29, 'yash@github: ~/build-lab', 13, '#9aaec5')
    body += text(795, 29, 'SESSION 001', 11, '#52f5a3')
    body += text(34, 85, '$ whoami', 18, '#52f5a3')
    body += text(32, 143, 'YASH KATARIA', 49, '#f1f7ff', 'font-weight="700" letter-spacing="-2"')
    body += text(35, 180, 'Curiosity in. Working software out.', 21, '#9bb3ce')
    body += text(35, 221, 'ML / AI', 14, '#52f5a3')
    body += text(153, 221, 'DATA SYSTEMS', 14, '#68d8ff')
    body += text(338, 221, 'DEVELOPER TOOLS', 14, '#c9a0ff')
    body += '<path d="M35 249 H886" stroke="#29374b"/>'
    body += text(35, 282, '$ ./learn-build-repeat', 16, '#52f5a3')
    body += text(35, 321, 'Hong Kong  /  building, experimenting, learning', 14, '#9aaec5')
    body += '<rect class="cursor" x="288" y="268" width="10" height="18" fill="#52f5a3"/>'
    body += '<g transform="translate(662 90)"><rect width="215" height="135" rx="12" fill="#0b101c" stroke="#344760"/>'
    for i,(label,color) in enumerate([('IDEA','#52f5a3'),('BUILD','#68d8ff'),('TEST','#c9a0ff')]):
        yy=28+i*39
        body += f'<circle class="pulse" cx="23" cy="{yy-5}" r="4" fill="{color}" style="animation-delay:{i*.7}s"/>'
        body += text(39,yy,label,13,color)
        body += f'<path class="flow" d="M106 {yy-5} H190" stroke="{color}" stroke-width="2" opacity=".55"/>'
    body += '</g>'
    svg('terminal-header.svg', 920, 360, body, 'Yash Kataria — ML/AI, data systems, developer tools', 'Animated terminal header. Based in Hong Kong. Curiosity in. Working software out.')

    projects = [
        ('patchwatch.svg','01','PATCHWATCH / EVALLAB','Python dependency upgrades, with proof.',
         'Sandboxed verification. Reviewable diffs. Repeatable evaluations.',
         'PYTHON  /  DOCKER  /  PYTEST','#52f5a3', ['inspect','upgrade','verify']),
        ('trade-engine.svg','02','ML TRADE ENGINE','Machine learning meets market research.',
         'Ensemble signals, out-of-sample backtests, and risk analysis.',
         'PYTHON  /  PYTORCH  /  MLflow','#68d8ff', ['data','model','backtest']),
        ('tariff-mapper.svg','03','TARIFFMAPPER','A clearer path through customs codes.',
         'China–Indonesia classification mapping with citations and review flags.',
         'TYPESCRIPT  /  NEXT.JS  /  AI','#c9a0ff', ['describe','map','review']),
    ]
    for filename,number,title,headline,desc,stack,color,steps in projects:
        body = f'<path d="M1 17 V157" stroke="{color}" stroke-width="3"/>'
        body += text(25,30,f'PROJECT {number}  /  {title}',13,color)
        body += text(25,66,headline,23,'#f1f7ff','font-weight="600"')
        body += text(25,97,desc,13,'#9aaec5')
        body += text(25,140,stack,11,color)
        body += text(885,32,'↗',24,color,'text-anchor="end"')
        body += text(885,140,' → '.join(steps),11,'#9aaec5','text-anchor="end"')
        svg(filename,920,164,body,title,headline+' '+desc)

    labels=['Python','PyTorch','TypeScript','Next.js','Docker','Git / CI']
    body=text(25,34,'$ cat toolbox.txt',15,'#52f5a3')
    for i,label in enumerate(labels):
        x=25+i*148
        body += f'<rect x="{x}" y="55" width="135" height="43" rx="7" fill="#142235" stroke="#34465c"/>'
        body += text(x+67,82,label,15,COLORS[i%len(COLORS)],'text-anchor="middle"')
    svg('toolbox.svg',920,121,body,'Tools in my public projects','Python, PyTorch, TypeScript, Next.js, Docker, Git and CI.')


def api(path):
    req=urllib.request.Request('https://api.github.com'+path, headers={
        'User-Agent':'Yash789k-profile-visuals', 'Accept':'application/vnd.github+json',
        'X-GitHub-Api-Version':'2022-11-28'})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def refresh_data():
    all_repos=[]
    for page in range(1,21):
        batch=api(f'/users/{USER}/repos?type=owner&per_page=100&page={page}')
        all_repos.extend(r for r in batch if not r.get('private') and r['owner']['login'].lower()==USER.lower())
        if len(batch)<100:
            break
    else:
        raise RuntimeError('Repository pagination exceeded the supported limit')
    originals=[r for r in all_repos if not r['fork'] and r['name'].lower()!=USER.lower() and r['size']>0]
    languages=Counter(r['language'] for r in originals if r.get('language'))
    recent=sorted(originals,key=lambda r:r.get('pushed_at') or '',reverse=True)[:3]
    data={
        'updated_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d'),
        'public_repository_count':len(all_repos),
        'original_project_count':len(originals),
        'primary_languages':dict(languages.most_common()),
        'recent_projects':[{'name':r['name'],'url':r['html_url'],'pushed_at':r['pushed_at']} for r in recent],
        'scope':'Public, owner repositories only. Language counts exclude forks, empty repositories, and the profile repository. Counts describe repositories, not skill levels.'
    }
    (ASSETS/'public-data.json').write_text(json.dumps(data,indent=2)+'\n')
    return data


def data_assets(data):
    langs=data['primary_languages']
    body=text(27,37,'$ github --public-only',17,'#52f5a3')
    metrics=[(27,data['public_repository_count'],'public repositories'),(267,data['original_project_count'],'original projects'),(516,len(langs),'primary languages')]
    for x,value,label in metrics:
        body+=text(x,95,value,39,'#f1f7ff','font-weight="700"')
        body+=text(x,123,label,13,'#9aaec5')
    body+=text(888,93,'UPDATED',12,'#52f5a3','text-anchor="end"')
    body+=text(888,120,data['updated_utc'],12,'#9aaec5','text-anchor="end"')
    body+='<path d="M27 148 H892" stroke="#2a3b50"/>'
    total=sum(langs.values()) or 1
    x=27.0
    for i,(language,count) in enumerate(langs.items()):
        width=865*count/total
        body+=f'<rect x="{x:.2f}" y="174" width="{width:.2f}" height="12" fill="{COLORS[i%len(COLORS)]}"/>'
        x+=width
    for i,(language,count) in enumerate(list(langs.items())[:6]):
        x=27+(i%3)*291;y=216+(i//3)*24
        body+=f'<circle cx="{x+5}" cy="{y-4}" r="4" fill="{COLORS[i%len(COLORS)]}"/>'
        body+=text(x+18,y,f'{language} · {count} repos',12,'#c3d1e3')
    body+=text(27,272,'Primary language per non-fork project · not a skill ranking',11,'#9aaec5')
    svg('public-activity.svg',920,294,body,'Public repository activity',f"{data['public_repository_count']} public repositories. {data['original_project_count']} non-fork non-empty projects. Updated {data['updated_utc']} UTC.")
    body=text(27,36,'$ ls --sort=recent ./public-projects',16,'#68d8ff')
    for i,repo in enumerate(data['recent_projects']):
        y=76+i*35
        body+=text(27,y,'↳',17,'#52f5a3')
        body+=text(55,y,repo['name'],16,'#e9f1fc')
        body+=text(890,y,repo['pushed_at'][:10],13,'#9aaec5','text-anchor="end"')
    svg('recent-projects.svg',920,177,body,'Recently updated public projects', '; '.join(r['name'] for r in data['recent_projects']))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--offline',action='store_true',help='Render from the existing public-data.json snapshot')
    args=parser.parse_args()
    ASSETS.mkdir(exist_ok=True)
    static_assets()
    data=json.loads((ASSETS/'public-data.json').read_text()) if args.offline else refresh_data()
    data_assets(data)
    print('Rendered profile visuals from public GitHub metadata.')


if __name__=='__main__':
    main()
