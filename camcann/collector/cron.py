from django_cron import CronJobBase, Schedule
from .models import *
import subprocess
import time
import os
import serial
import re
from channels import Group

class SaveCSV(CronJobBase):
    RUN_EVERY_MINS = 5

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'collector.SaveCSV'

    def do(self):
        f = open("data.csv", "a")
        data = Data.objects.all()
        for i in data:
            f.write(str(data.Timestamp) + "," + data.Gender + "," + data.Age + "," + data.Frame_shape)
        f.close()

class PlayAD(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'collector.PLAYAD'

    def do(self):
        p = None
        FNULL = open(os.devnull,"w")
        while True:
            queue = Queue.objects.filter(played=False)
            for i in queue:
                print("PLAYING TARGETED VIDEO",i.ad.video_file)
                p = subprocess.Popen(["vlc", i.ad.video_file, "--play-and-exit","--fullscreen"],stdout=FNULL,stderr=FNULL)
                p.wait()
                i.played = True
                i.save()
            if len(queue) == 0:
                time.sleep(0.1)
                #toplay = Ads.objects.all().order_by("?").first()
                #print("PLAYING RANDOM VIDEO",toplay.video_file)
                #p = subprocess.Popen(["vlc", toplay.video_file, "--play-and-exit","--fullscreen"],stdout=FNULL,stderr=FNULL)
                #p.wait()

class ReadTAG(CronJobBase):
    RUN_EVERY_MINS = 1


    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'collector.ReadTAG'
    tag_lastupdate = ""

    def do(self):
        current_state = {}
        current_count = {}
        ser = serial.Serial('/dev/ttyACM0')
        while True:
            time.sleep(0.01)
            for tag in current_state.keys():
                if current_state[tag] == "1":
                    current_count[tag] += 1
                    time.sleep(0.1)

                    if current_count[tag] > 20:
                        col = Tag.objects.get(tag_id=tag)
                        ch = TagHistory.objects.create(tag=col, action="1")
                        ch.save()
                        current_state[tag] = "-1"
                        current_count[tag] = 0
                        Group('data').send({'text': tag+"_1"})


            if ser.in_waiting:
                line = ser.readline()
                print(line)
                match = re.search('([\d]+[_][\d])',line.decode('utf-8'))
                if match:
                    tag = match.group(1)
                    if self.tag_lastupdate != tag:
                        tag_split = tag.split("_")

                        if tag_split[0] not in current_state.keys():
                            current_state[tag_split[0]] = "-1"
                            current_count[tag_split[0]] = 0
                        if current_state[tag_split[0]] == "-1" and tag_split[1] == "0":
                            col = Tag.objects.get(tag_id=tag_split[0])
                            ch = TagHistory.objects.create(tag=col,action=tag_split[1])
                            ch.save()
                            Group('data').send({'text': tag_split[0] + "_0"})
                        elif tag_split[1] == "0":
                            current_state[tag_split[0]] = "0"
                            current_count[tag_split[0]] = 0
                        elif tag_split[1] == "1":
                            current_state[tag_split[0]] = "1"
                            current_count[tag_split[0]] = 0
                        self.tag_lastupdate = tag