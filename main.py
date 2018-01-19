# -*- coding: utf-8 -*-
import web
import json
from pytube import YouTube
render = web.template.render('templates/',base='layout')
urls = (
  '/','index',
  '/get_video_info','get_video_info'
)

class index:
  def GET(self):
    print('now is get:')
    return render.index()
  def POST(self):
    print('now is post')
    i = web.input()
    if i.url:
      start_new_download_progress(i.url)
    return render.show_process()
    
class get_video_info:
  def POST(self):
    info = web.input()
    print('now info'+str(info))
    if info.url:
      if not (info.url.startswith('http://') or info.url.startswith('https://')):
        return 'invalided url'
      else:
        url = info.url
        yt = YouTube(url)
        ret = {
          'title':yt.title,
          'videos':[],
        }
        for item in yt.streams.all():
          cur_item = {
            'filesize':item.filesize,
            'default_filename':item.default_filename,
            'includes_audio_track':item.includes_audio_track,
            'includes_video_track':item.includes_video_track,
            'is_adaptive':item.is_adaptive,
            'is_progressive':item.is_progressive,
          }
          ret['videos'].append(cur_item)
        return json.dumps(ret)


def start_new_download_progress(url):
#  get_tube(url)
  print(url)

#def get_youtube_video(url,
if __name__ == '__main__':
  app = web.application(urls,globals())
  app.run()
