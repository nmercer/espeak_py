**Description**: Python module to convert text to MP3 files.

**Dependencies**: linux distro, espeak, lame

**Example**:
```python
#Creates /home/hello.mp3 that says "Hello, World!" at a faster speed then default.

foo = espeak_py.init("/home/")

speak_string = "Hello, World!"
options = {"speed":120}
file_name = "hello"

foo.say(speak_string, {"speed":120}, file_name)
```

**Options**:
speed - int
amp   - int
pitch - int
voice - string

Voices on your system can be seen by running "espeak --voices".
