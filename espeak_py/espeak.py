import subprocess

class Espeak(object):
    def __init__(self, filepath=None, debug=False):
        self.debug = debug

        if filepath:
            self.filepath = filepath
        else:
            self.filepath = ""

        self.default_options = {"amp":100,
                                "speed":100,
                                "pitch":50,
                                "voice":"en/en-us"}

    def say(self, text, options, filename):
        self._execute(text, self._make_options(options), filename)

    def _make_options(self, options):
        return dict(self.default_options.items() + options.items())

    def _execute(self, text, options, filename):
        proc = subprocess.Popen(self._make_call(text,options,filename), shell=True)
        wait = proc.wait()
       
    def _make_call(self, text, options, filename):
        espeak = "espeak -a%s -s%s -p%s -v'%s' '%s' --stdout" % \
            (options['amp'], options['speed'], options['pitch'], options['voice'], text)

        lame = "|lame -S -b32 - %s%s.mp3" % (self.filepath, filename)

        if self.debug == True:
            print "%s %s" % (espeak, lame)

        return "%s %s" % (espeak, lame)
