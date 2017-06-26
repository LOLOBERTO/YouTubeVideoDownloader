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
- `Clone or download the zip: https://github.com/lohriialo/YouTubeVideoDownloader/archive/master.zip`
- `Go to dist folder`
- `Run 'YouTube Video Downloader.exe'`

# Modify and extend it further, requiremments:
- `Python 3.x`
- `PyQt4: https://sourceforge.net/projects/pyqt/files/PyQt4/`
- `pyuic4`
- `http://www.pyinstaller.org/`

# Convert .ui to .py with pyuic4
cmd: pyuic4 <inputpath to file.ui> -o <outputpath to file.py>

# Compile the app to executable using pyInstaller
cmd: pyinstaller <path to appplication main YouTubeDownloader.py> --onedir --onefile --name "YouTube Video Downloader" --windowed --noconsole
