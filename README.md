# YouTubeVideoDownloader
YouTubeVideoDownloader provides a UI to directly download videos from a video link or a playlist link.

It is an extension of the popular commandline video downloader "youtube-dl" https://github.com/rg3/youtube-dl
You can download videos from YouTube and many other video sites. For a list of supported sites, see: https://github.com/rg3/youtube-dl/blob/master/docs/supportedsites.md

Following download quality are supported:
 - `360p`
 - `480p`
 - `720p`
 - `1080p`
 - `2K`
 - `4K`
 - `8K`
 
# How to use:
- `Download zip` https://github.com/lohriialo/YouTubeVideoDownloader/blob/master/dist/YouTubeVideoDownloader.zip
- `Unzip "YouTubeVideoDownloader.zip"`
- `Run 'YouTube Video Downloader.exe'`

![alt text](https://github.com/lohriialo/YouTubeVideoDownloader/blob/master/Capture.PNG)

# Modify and extend it further, requiremments:
- `Python 3.x`
- `PyQt4: https://sourceforge.net/projects/pyqt/files/PyQt4/`
- `pyuic4`
- `http://www.pyinstaller.org/`

# Convert .ui to .py with pyuic4
- `pyuic4 <inputpath to file.ui> -o <outputpath to file.py>`

# Compile the app to executable using pyInstaller
- `pyinstaller <path to appplication main YouTubeDownloader.py> --onedir --onefile --name "YouTube Video Downloader" --windowed --noconsole`


# MIT License

# Copyright (c) 2017 Lohrii Alo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
