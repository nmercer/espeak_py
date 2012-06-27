cription**: Python module to convert text to MP3 files.

**Dependencies**: linux distro, espeak, lame

**Example**:
```python
#Creates /home/hello.mp3 that says "Hello, World!" at a faster speed than default.

foo = espeak_py.init("/home/")

speak_string = "Hello, World!"
options = {"speed":120}
file_name = "hello"

foo.say(speak_string, {"speed":120}, file_name)
```

**Options**:

{speed: INT, amp : INT, pitch : INT, voice : STRING}


Voices on your system can be seen by running "espeak --voices".
