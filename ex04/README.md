# 第4回
## 逃げろ！こうかとん（ex04/dodge_bomb.py）
### ゲーム概要
- ex04/dodge_bomb.pyを実行すると，1600x900のスクリーンに草原が描画され，こうかとん
を移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
### 追加機能
- こうかとんが爆弾と接触すると新しいウィンドウで逃げた時間が表示され、続けるか聞いてくる
- こうかとんが爆弾と接触するとこうかとんが泣く絵になる
- 爆弾の速度を2倍にした
### ToDo（実装しようと思ったけど時間がなかった）
- [ ] 着弾するとこうかとん画像が切り替わる
- [ ] 爆弾を複数個にする
- [ ] 時間とともに爆弾が加速するor大きくなる
- [ ] 同一ウィンドウで続けるか聞き、keyを押すことで選択するようにしたかった　(「"""」でコメントアウトしている部分)
- [ ] ↑が出来なかったためtkinterで聞いているが再スタートはできない
### メモ