# recompress_video
 **ver.beta1.1**
 指定したフォルダー内の動画を一括で再圧縮してくれるやつ

<br>

## 注意事項
 ### 必須なもの
  **Python**
  →何を思ったのかPythonで書いた

 ### ないと一部機能しないもの
  **NVENCに対応したNVIDIA製GPU**
  →ないとハードウェアエンコードができない

## ライセンス
 [FFmpegのライセンス](/license/FFmpeg.txt)

<br>

## ディレクトリ構成
 **ffmpeg** FFmpegが入ってるフォルダー<br>
 └**ffmpeg.exe** FFmpeg本体<br>
  **license** ライセンス系のテキストファイルが入ってるフォルダー<br>
 └**FFmpeg.txt** FFmpegのGPLライセンス<br>
 **.gitattributes** 結局これなんなの【github歴3年にあるまじき発言】<br>
 **icon.ico** アイコン(仮)<br>
 **recompress_video.exe** 本体<br>
 **recompress_video.py** Pythonのコード(cmd使ってこいつから実行することもできる)<br>
 **recompress_video.spec** はじめてexeファイル作ったのでわたしもわかりません(設定ファイルだとかなんとか)<br>
 **りどみ.md** This<br>

## 使い方
 1.recompress_videdo.exeを開く<br>
 2.圧縮させたい動画があるフォルダーを選択<br>
 3.エンコード方式(1:ソフトウェアエンコード 2:ハードウェアエンコード)を選択<br>
 4.待つ<br>
 5.おわり(Enterキーを押せば閉じるよ)<br>

<br>

## 仕様
 ### 今のところ対応している拡張子
 mp4、mov、avi、mkv
 (ソースコードいじくれば他の拡張子も読み込めるよ)

 ### 共通部分
  ファイル名：圧縮元動画と同じ
  拡張子：mp4
  更新日時：圧縮元動画と同じ

 ### ソフトウェアエンコード
  映像コーデック：libx264
  解像度：圧縮元動画と同じ
  fps：圧縮元動画と同じ
  品質：crf 20
  音声コーデック：aac
  サンプリング数：48000Hz
  音声ビットレート：128kbps

 ### ハードウェアエンコード
  映像コーデック：h264_nvenc
  解像度：圧縮元動画と同じ
  fps：圧縮元動画と同じ
  品質：qp 24
  音声コーデック：aac
  サンプリング数：48000Hz
  音声ビットレート：128kbps
  
<br><br><br>

### めも
notベータではGUI化したり画質調整を細かくできるようにしたい
作成日時を圧縮元動画と同じにできないんだけどなんで
