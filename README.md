# Flagolor （コーデ投稿アプリ）
ここから使えます<br>
※今のところHerokuの仕様で画像表示ができていません<br>
https://flagolor.herokuapp.com/post_outfit/
## コンセプト
国旗×ファッション<br>
* 国旗を覚えたい
* 無難な色の服ばかり着がちな人に, カラフルなファッションを楽しんでもらいたい

## どんなアプリか
* "今週の国旗" で指定された国旗をイメージしたコーディネートの写真を投稿する
* みんなが投稿したコーデを見ることができる
  * 国旗は毎週変わります
* お気に入りのユーザーをフォローできる
* お気に入りの投稿を保存できる


## 使い方
1. トップページから新規ユーザー登録をして, ログインしてください.
    * ログインなしでも閲覧できます.
    * 投稿, いいね, お気に入り登録などの機能は使えません.
    * ログイン後は, 自分の投稿は一覧に表示されません. マイページからご覧ください.

<img src="https://user-images.githubusercontent.com/76393580/167838161-8d32ffc7-4948-48d1-a5f3-2db15fc6c639.png" width="500px">

2. ログイン後は, 右上のユーザー名のリンクから "マイページ" に飛べるようになります.
    * ここから投稿やプロフィール編集, お気に入りに登録した投稿の閲覧ができます.

<img src="https://user-images.githubusercontent.com/76393580/167838877-595cf1ac-0d3c-49cb-828c-e50fe832e7fc.png" width="500px">

3. 投稿写真をクリックすると, 詳細を見ることができます.
    * ♡でいいね, 📁でお気に入り登録ができます.
    * お気に入り登録した投稿は, マイページの "お気に入り" のリンクから飛べます.
    * "フォロー" ボタンでそのユーザーをフォローできます.
    * マイページの "フォロー", "フォロワー" から確認できます.
<img src="https://user-images.githubusercontent.com/76393580/167839096-594fcc2f-49fe-4783-bc41-10c53ac3c87e.png" width="500px">


## 使用技術
* Django
