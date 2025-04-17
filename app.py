from flask import Flask, request, render_template
import yt_dlp
import os

app = Flask(__name__)  # Corrected here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form['video_url']
    video_quality = request.form['video_quality']
    print("You sent:", video_url)

    # Create downloads folder if not exists
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    ydl_opts = {
        'format': f'bestvideo[height<={video_quality}]+bestaudio/best/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return "✅ Video downloaded successfully!"
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__== '__main__':
    app.run(debug=True)