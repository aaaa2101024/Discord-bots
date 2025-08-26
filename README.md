# 作成した Discord Bot 置き場

## 1. hello

紛れもないテスト用 Bot. とくに言うことはないです. 

## 2. RandomPay

友人 T 氏が作ってたスクリプトを Discord のコマンドで使えたら面白そうと思って作成しました. 
内容は, 某バーコード決済アプリの URL と, 自然数を入力すると, 偽物の URl が大量生成され, おみくじを開催できるというものです. 

## 3. 野獣先輩

`doyoulikeyaju`と`messageyaju`の二つのコマンドがあり, どちらも`sure!`を回答した場合にはランダムな画像を, `nop.`の場合はランダムな語録を送信します. 
その他テスト用で作ったコマンドが付属してたり

構成図
```
├── del.txt             // gemeniに生成させた語録NG集
├── goroku.txt          // geminiに生成させた語録集
├── icon.jpg            // discordアプリのアイコン
├── icon.png            // discordアプリのアイコン(未使用)
├── imageFilePath.txt   // 画像のファイルパスたち
├── images              // 画像
│   ├── YAJU.gif        // YAJU&U
│   ├── inm.gif         // やりますねえ！
│   ├── ko↑ko↓.gif      // こ↑こ↓   
│   ├── paisenn.png     // 先輩
│   └── power.png       // 目力先輩
├── messageYaju.py      // botプログラム本体
└── test.py             // いろいろ動かせるかのテストで作ったbot
```

## 4. ping

discordのメンバーに対して, pingメッセージを送ることができます. 
~~メンションをたくさん送れて嬉しいね！！！~~