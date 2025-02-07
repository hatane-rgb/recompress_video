# recompress_video
 **ver.beta1.1b**
 指定したフォルダー内の動画を一括で再圧縮してくれるやつ

<br>

## 注意事項
 ### 必須なもの
  **Python**
  → 何を思ったのかPythonで書いた

 ### ないと一部機能しないもの
  **NVENCに対応したNVIDIA製GPU**
  → ないとハードウェアエンコードができない

## ライセンス
 [FFmpegのライセンス](/license/FFmpeg.txt)

<br>

## ディレクトリ構成
 **ffmpeg** FFmpegが入ってるフォルダー<br>
 └ **ffmpeg.exe** FFmpeg本体<br>
  **license** ライセンス系のテキストファイルが入ってるフォルダー<br>
 └ **FFmpeg.txt** FFmpegのGPLライセンス<br>
 **.gitattributes** 結局これなんなの【github歴3年にあるまじき発言】<br>
 **icon.ico** アイコン(仮)<br>
 **recompress_video.exe** 本体<br>
 **recompress_video.py** Pythonのコード(cmd使ってこいつから実行することもできる)<br>
 **recompress_video.spec** はじめてexeファイル作ったのでわたしもわかりません(設定ファイルだとかなんとか)<br>
 **readme.md** this<br>

## 使い方
 1.recompress_video.exeを開く<br>
 2.フォルダー選択のウィンドウが出てくるので圧縮させたい動画があるフォルダーを選択<br>
 3.解像度(1:元の解像度 2～9:プリセット解像度 数字:(自動)x(入力した解像度))を選択
 4.エンコード方式(1:ソフトウェアエンコード 2:ハードウェアエンコード)を選択<br>
 5.待つ<br>
 6.おわり(y:別の動画を圧縮 n:終了)<br>

<br>

## 仕様
 ### 今のところ対応している拡張子
 mp4、mov、avi、mkv<br>
 (ソースコードいじくれば他の拡張子も読み込めるよ)<br>

<br>

 ### ハード/ソフト共通部分
  ファイル名：圧縮元動画と同じ<br>
  拡張子：mp4<br>
  更新日時：圧縮元動画と同じ<br>

 ### ソフトウェアエンコード
  映像コーデック：libx264<br>
  解像度：圧縮元動画と同じ<br>
  fps：圧縮元動画と同じ<br>
  品質：crf 20<br>
  音声コーデック：aac<br>
  サンプリング数：48000Hz<br>
  音声ビットレート：128kbps<br>

 ### ハードウェアエンコード
  映像コーデック：h264_nvenc<br>
  解像度：圧縮元動画と同じ<br>
  fps：圧縮元動画と同じ<br>
  品質：qp 24<br>
  音声コーデック：aac<br>
  サンプリング数：48000Hz<br>
  音声ビットレート：128kbps<br>
  
<br><br><br>

### めも
notベータではGUI化したり画質調整を細かくできるようにしたい
作成日時を圧縮元動画と同じにできないんだけどなんで
