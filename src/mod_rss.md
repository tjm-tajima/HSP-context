# mod_rss

- **種別**: ユーザー定義命令
- **グループ**: 入出力制御命令
- **バージョン**: 3.3
- **更新日**: 2009/08/01
- **作者**: onitama
- **URL**: http://hsp.tv/
- **対応環境**: Win / Cli / Let
- **備考**: mod_rss.asをインクルードすること。

## 命令一覧

| 命令 | 概要 |
|---|---|
| [rssload](#rssload) | XMLパーサー(MSXML)を使用してRSSを読み込む |

## 命令詳細

### rssload

XMLパーサー(MSXML)を使用してRSSを読み込む

**構文**
```
rssload p1, p2, "path", p3
```

**パラメータ**
- `p1=変数`: RSSの内容を代入する文字列型配列変数
- `p2=変数`: リンク先を代入する文字列型配列変数
- `"path"`: URLまたはファイルパス
- `p3=0～(5)`: 読み込むRSSフィールドの数

**説明**

XMLパーサー(MSXML)を使用してRSSを読み込みます。

結果はp1およびp2に代入されます。p1およびp2は自動的に文字列型配列変数として初期化されます。

p3には読み込むRSSフィールドの数を指定します。p3を省略した場合は5つ読み込みます。

RSSの読み込みに成功すると、システム変数statに0が返ります。
取得に失敗した場合はstatに1が、指定したURLまたはファイルパスがRSSのものではなかった場合はstatに2が返ります。

**サンプル**
```hsp
#include "mod_rss.as"

	// RSSのURL（HSPWiKiのRSS）
	url = "http://quasiquote.org/hspwiki/?c=rss"
	// RSSのロード
	rssload desc, link, url, 6
	if stat == 1 : dialog "取得に失敗しました。" : end
	if stat == 2 : dialog "RSSではありません。"  : end

	// 内容を表示
	mes "RSSの内容を表示します。"
	mes url
	mes "----------------------------------------------------------------"
	foreach desc
		mes ""  +cnt + ":" + desc(cnt)
		mes "    (" + link(cnt) + ")"
	loop

	stop
```

---
