import os
import sys
import subprocess
import argparse
import tkinter as tk
from tkinter import filedialog

# ffmpegのパスを指定
ffmpeg_path = os.path.join("ffmpeg", "ffmpeg.exe")
print(f"FFmpeg : {ffmpeg_path}")

def compress_videos(input_folder, definition, codec, qpcrf, crf, audio_bitrate, profile, height=None, single_file=None):
    i = 0

    # 入力フォルダー内の全ての動画ファイルを処理
    files_to_process = [single_file] if single_file else os.listdir(input_folder)
    for filename in files_to_process:
        i += 1
        print(i, "個目の動画を圧縮します")

        # 対応する拡張子のファイルのみ処理
        if filename.endswith((".mp4", ".avi", ".mov", ".mkv", "MP4", "MOV", "m2t", "mts")):
            subfolder_name = "圧縮済み"

            # 元動画を読み込む
            input_file = os.path.join(input_folder, filename)

            # 出力先サブディレクトリを作成
            output_subfolder = os.path.join(input_folder, subfolder_name)
            os.makedirs(output_subfolder, exist_ok=True)  # サブディレクトリが存在しない場合は作成

            # 圧縮後のファイルパスを設定
            output_file = os.path.join(output_subfolder, f"{os.path.splitext(filename)[0]}.mp4")

            # FFmpegで動画を圧縮
            if definition == '1':
                subprocess.run([
                    ffmpeg_path, '-y', '-i', input_file, '-c:v', codec,
                    '-profile:v', profile, '-pix_fmt', 'yuv420p', qpcrf, crf,
                    '-c:a', 'aac', '-b:a', audio_bitrate, output_file
                ], check=True)
            else:
                subprocess.run([
                    ffmpeg_path, '-y', '-i', input_file, '-vf', f"scale=-2:{height}", '-c:v', codec,
                    '-profile:v', profile, '-pix_fmt', 'yuv420p', qpcrf, crf,
                    '-c:a', 'aac', '-b:a', audio_bitrate, output_file
                ], check=True)

            # 圧縮後の動画ファイルに対して、作成日時と更新日時を元動画と同じに設定
            os.utime(output_file, (os.path.getctime(input_file), os.path.getmtime(input_file)))

def main():
    parser = argparse.ArgumentParser(description="動画再圧縮スクリプト")
    parser.add_argument('path', nargs='?', help="動画が含まれるフォルダーのパス")
    parser.add_argument('resolution', nargs='?', help="解像度オプション (1-9 またはカスタム高さ)")
    parser.add_argument('encode_type', nargs='?', help="エンコードタイプ (1-4)")
    parser.add_argument('-no', '-n', action='store_true', help="最終プロンプトをスキップして終了")
    parser.add_argument('-o', '--only', dest='only', help="単一ファイルのみ圧縮")

    args = parser.parse_args()

    if args.path and args.resolution and args.encode_type:
        folder_selected = args.path
        definition = args.resolution
        enc = args.encode_type
    else:
        # フォルダ選択ダイアログの表示
        root = tk.Tk()
        root.withdraw()  # メインウィンドウを隠す
        folder_selected = filedialog.askdirectory()
        root.destroy()

        if not folder_selected:
            print("フォルダが選択されませんでした")
            sys.exit()

        os.system('cls')
        print(f"選択されたフォルダ: {folder_selected}\n")

        definition = input("解像度を選択してください\n1:元の解像度を維持\n2:144p 3:240p 4:360p 5:480p 6:720p 7:1080p 8:1440p 9:2160p(4K)\n数字:(自動)x(入力した解像度)に設定\n")
        enc = input("エンコード方式を選択してください\n1:libx264,crf20 2:libx264,crf15 3:h264_nvenc,qp24 4:h264_nvenc,qp19\n")

    # 解像度の設定
    if definition == "1":
        print("元の解像度を維持します\n")
        height = None
    elif definition == "2":
        print("144pでエンコードします")
        height = '144'
    elif definition == "3":
        print("240pでエンコードします")
        height = '240'
    elif definition == "4":
        print("360pでエンコードします")
        height = '360'
    elif definition == "5":
        print("480pでエンコードします")
        height = '480'
    elif definition == "6":
        print("720pでエンコードします")
        height = '720'
    elif definition == "7":
        print("1080pでエンコードします")
        height = '1080'
    elif definition == "8":
        print("1440pでエンコードします")
        height = '1440'
    elif definition == "9":
        print("2160p(4K)でエンコードします")
        height = '2160'
    else:
        print("入力した解像度でエンコードします\n")
        height = definition  # 横解像度

    # エンコード方式の設定
    if enc == "1":
        print("libx264 crf20でエンコードします")
        codec = 'libx264'
        qpcrf = '-crf'
        crf = '20'
        audio_bitrate = '128k'
        profile = 'high'
    elif enc == "2":
        print("libx264 crf15でエンコードします")
        codec = 'libx264'
        qpcrf = '-crf'
        crf = '15'
        audio_bitrate = '128k'
        profile = 'high'
    elif enc == "3":
        print("h264_nvenc qp24でエンコードします")
        codec = 'h264_nvenc'
        qpcrf = '-qp'
        crf = '24'
        audio_bitrate = '128k'
        profile = 'high'
    elif enc == "4":
        print("h264_nvenc qp19でエンコードします")
        codec = 'h264_nvenc'
        qpcrf = '-qp'
        crf = '19'
        audio_bitrate = '128k'
        profile = 'high'
    else:
        print("範囲外の数字が選択されました")
        sys.exit()

    # 動画の圧縮を実行
    compress_videos(folder_selected, definition, codec, qpcrf, crf, audio_bitrate, profile, height, single_file=args.only)

    print("全ての動画ファイルの圧縮が完了しました")

    # 最終プロンプトをスキップして終了
    if args.no:
        print("プログラムを終了します")
        sys.exit()

    # 他のフォルダーの動画も圧縮するか確認
    while True:
        q = input("他のフォルダーの動画も圧縮しますか？[y/n]\n")
        if q == "y":
            main()
        elif q == "n":
            print("プログラムを終了します")
            sys.exit()
        else:
            print("y、n以外の文字が入力されました")

if __name__ == "__main__":
    main()