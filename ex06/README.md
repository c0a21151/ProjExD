# 第6回
## 食べろ！にょろにょろ（ex06/mimizu.py）
### ゲーム概要
- ex06/mimizu.pyを実行すると，600x400のスクリーンに緑色のミミズと赤い餌が出現する。ミミズを操作して餌をゲットするゲーム。
- ミミズが壁にぶつかるとゲームオーバーで終了する
- ミミズが敵と3回接触するとゲームオーバーで終了する
### 操作方法
- 矢印キーでミミズを上下左右に移動する
### クリア条件
- 餌を3個ゲットする

### 自分が作った機能
- ライフが左上に表示される。敵は自分の担当ではないので、代わりに餌を取ったら1つ減るようにした。
- BGMを追加した。
- 餌をゲットした時とゲームオーバーになった時それぞれ異なるSEがなる。ゲームオーバーの時は終了すると鳴らないため、SEがなるように画面の動きを1秒停止する。

### 参考サイトのURL
- アイコン素材ダウンロードサイト「icooon-mono」 | 商用利用可能なアイコン素材が無料(フリー)ダウンロードできるサイト | 6000個以上のアイコン素材を無料でダウンロードできるサイト ICOOON MONO 
 https://icooon-mono.com/
- シューティングゲームにおけるBGMとSEの実装例【Pygame】 | グッドラックネットライフ 
 https://goodlucknetlife.com/python-shooting-bgm-se/
- フリー効果音素材「8bit_Down」ダウンロードページ｜フリーBGM DOVA-SYNDROME 
 https://dova-s.jp/se/download692.html
- ”残念”で検索した結果[1]｜効果音ラボ 
 https://soundeffect-lab.info/sound/search.php?s=%E6%AE%8B%E5%BF%B5