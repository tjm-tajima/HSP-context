# hsedsdk

- **種別**: ユーザー拡張命令
- **グループ**: HSPスクリプトエディタ 外部ツール作成用
- **バージョン**: 3.6
- **更新日**: 2020/12/17
- **作者**: onitama
- **URL**: ; 関連 URL を記入
- **対応環境**: Win
- **備考**: hsedsdk.asをインクルードすること。

## 命令一覧

| 命令 | 概要 |
|---|---|
| [hsed_exist](#hsed_exist) | HSPスクリプトエディタの起動状態を取得 |
| [hsed_capture](#hsed_capture) | HSPスクリプトエディタのAPIウィンドウを捕捉 |
| [hsed_gettext](#hsed_gettext) | 編集中のテキストを取得 |
| [hsed_sendstr](#hsed_sendstr) | 文字列を貼り付け |
| [hsed_cancopy](#hsed_cancopy) | コピーの可否を取得 |
| [hsed_cut](#hsed_cut) | 指定したFootyから文字列を切り取る |
| [hsed_redo](#hsed_redo) | リドゥを行う |
| [hsed_undo](#hsed_undo) | アンドゥを行う |
| [hsed_indent](#hsed_indent) | インデントを行う |
| [hsed_unindent](#hsed_unindent) | アンインデントを行う |
| [hsed_uninitduppipe](#hsed_uninitduppipe) | パイプハンドルの解放 |
| [hsed_initduppipe](#hsed_initduppipe) | パイプハンドルの作成 |
| [hsed_getmajorver](#hsed_getmajorver) | メジャーバージョンを抽出 |
| [hsed_getminorver](#hsed_getminorver) | マイナーバージョンを抽出 |
| [hsed_getbetaver](#hsed_getbetaver) | ベータバージョンを抽出 |
| [hsed_getver](#hsed_getver) | スクリプトエディタのバージョンを取得 |
| [hsed_getwnd](#hsed_getwnd) | スクリプトエディタの各種ハンドルを取得 |
| [hsed_cnvverstr](#hsed_cnvverstr) | バージョンの数値を文字列に変換 |
| [hsed_selectall](#hsed_selectall) | テキストをすべて選択 |
| [hsed_gettextlength](#hsed_gettextlength) | テキストの文字列長を取得 |
| [hsed_getlines](#hsed_getlines) | テキストの行数を取得 |
| [hsed_getlinelength](#hsed_getlinelength) | 行の文字列長を取得 |
| [hsed_getlinecode](#hsed_getlinecode) | 改行コードを取得 |
| [hsed_copy](#hsed_copy) | 指定したFootyから文字列をコピー |
| [hsed_paste](#hsed_paste) | 指定したFootyへ文字列を貼り付け |
| [hsed_canpaste](#hsed_canpaste) | 貼り付けの可否を取得 |
| [hsed_canundo](#hsed_canundo) | アンドゥの可否を取得 |
| [hsed_canredo](#hsed_canredo) | リドゥの可否を取得 |
| [hsed_getmodify](#hsed_getmodify) | 変更フラグを取得 |
| [hsed_settext](#hsed_settext) | テキストを変更 |
| [hsed_getfootyid](#hsed_getfootyid) | タブのIDからFootyのIDを取得 |
| [hsed_gettabid](#hsed_gettabid) | FootyのIDからタブのIDを取得 |
| [hsed_gettabcount](#hsed_gettabcount) | タブ数の取得 |
| [hsed_getactfootyid](#hsed_getactfootyid) | アクティブなFootyのIDの取得 |
| [hsed_getacttabid](#hsed_getacttabid) | アクティブなタブのIDの取得 |
| [hsed_getpath](#hsed_getpath) | タブIDからファイルパスを取得 |

## 命令詳細

### hsed_exist

HSPスクリプトエディタの起動状態を取得

- **グループ**: 情報取得命令

**構文**
```
hsed_exist
```

**パラメータ**
- なし

**説明**

HSPスクリプトエディタが起動しているかチェックします。
起動していれば1が、起動していなければ0がシステム変数statに代入されます。

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_exist
	if ( stat ) {
		mes "HSPスクリプトエディタが起動しています。"
	} else {
		mes "HSPスクリプトエディタは起動していません。"
	}
	stop
```

---

### hsed_capture

HSPスクリプトエディタのAPIウィンドウを捕捉

- **グループ**: ハンドル取得命令

**構文**
```
hsed_capture
```

**パラメータ**
- なし

**説明**

hsedsdkモジュール内の変数hIFにHSPスクリプトエディタのAPIウィンドウのハンドルを代入します。
^
取得に成功した場合はシステム変数statに0が代入されます。
^
この命令はhsedsdk.as内で利用される命令であり、通常は利用する必要はありません。

**関連**: hsed_getwnd

---

### hsed_gettext

編集中のテキストを取得

- **グループ**: テキスト取得命令

**構文**
```
hsed_gettext p1, p2
```

**パラメータ**
- `p1`: テキストを代入する変数
- `p2`: 取得したいFootyのID

**説明**

HSPスクリプトエディタで編集しているテキストを取得し、p1に代入します。
^
取得に成功した場合はシステム変数statに0が代入されます。

**関連**: hsed_settext

**サンプル**
```hsp
#include "hsedsdk.as"
	nTabID = 0
	hsed_getfootyid nFootyID, nTabID
	if ( stat == 0 ) : hsed_gettext buf, nFootyID
	mesbox buf, ginfo_winx, ginfo_winy
	stop
```

---

### hsed_sendstr

文字列を貼り付け

- **グループ**: テキスト編集命令

**構文**
```
hsed_sendstr p1
```

**パラメータ**
- `p1`: スクリプトに挿入する文字列を格納した文字列型変数

**説明**

編集中のテキストにp1に格納した文字列を貼り付けます。

**関連**: hsed_settext

**サンプル**
```hsp
#include "hsedsdk.as"
	sIns = "スクリプトエディタに送る文字列"
	hsed_sendstr sIns
```

---

### hsed_cancopy

コピーの可否を取得

- **グループ**: 情報取得命令

**構文**
```
hsed_cancopy p1, p2
```

**パラメータ**
- `p1`: 結果を格納する変数
- `p2`: FootyのID

**説明**

コピーの可否を取得します。
指定されたFootyからクリップボードにコピーすることができる場合はp1に1が返ります。
^
実際にコピーや切り取りを行う場合はhsed_copyまたはhsed_cutを利用してください。

**関連**: hsed_copy, hsed_cut, hsed_canpaste

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_cancopy ret, idFooty
		if ( ret ) {
			mes "ID" + str( cnt ) + "のタブはコピーできます。"
		} else {
			mes "ID" + str( cnt ) + "のタブはコピーできません。"
		}
	loop
	stop
```

---

### hsed_cut

指定したFootyから文字列を切り取る

- **グループ**: クリップボード操作命令

**構文**
```
hsed_cut p1
```

**パラメータ**
- `p1`: 文字列を切り取るFootyのID

**説明**

指定したFootyへ文字列をクリップボードに切り取るよう要請します。
切り取りが行えるかどうかはhsed_cancopyで調べてください。

**関連**: hsed_cancopy, hsed_copy

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_cancopy ret, idFooty
		if ( ret ) {
			hsed_cut idFooty
			mes "ID" + str( cnt ) + "のタブから切り取りました。"
		}
	loop
	stop
```

---

### hsed_redo

リドゥを行う

- **グループ**: テキスト編集命令

**構文**
```
hsed_redo p1
```

**パラメータ**
- `p1`: リドゥを行うFootyのID

**説明**

指定したFootyに対してリドゥを行うように要請します。
リドゥが行えるかどうかはhsed_canredoで調べてください。

**関連**: hsed_undo, hsed_canredo

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_canredo ret, idFooty
		if ( ret ) {
			hsed_redo idFooty
			mes "ID" + idFooty + "のFootyをリドゥしました。"
		} else {
			mes "ID" + idFooty + "のFootyはリドゥできませんでした。"
		}
	loop
	stop
```

---

### hsed_undo

アンドゥを行う

- **グループ**: テキスト編集命令

**構文**
```
hsed_undo p1
```

**パラメータ**
- `p1`: アンドゥを行うFootyのID

**説明**

指定したFootyに対してアンドゥを行うように要請します。
アンドゥが行えるかどうかはhsed_canundoで調べてください。

**関連**: hsed_redo, hsed_canundo

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_canundo ret, idFooty
		if ( ret ) {
			hsed_undo idFooty
			mes "ID" + idFooty + "のFootyをアンドゥしました。"
		} else {
			mes "ID" + idFooty + "のFootyはアンドゥできませんでした。"
		}
	loop
	stop
```

---

### hsed_indent

インデントを行う

- **グループ**: テキスト編集命令

**構文**
```
hsed_indent p1
```

**パラメータ**
- `p1`: インデントを行うFootyのID

**説明**

Footyに対してインデントを行うように要請します。
インデントは選択範囲に対して行われます。

**関連**: hsed_unindent

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_selectall idFooty
		hsed_indent idFooty
	loop
	stop
```

---

### hsed_unindent

アンインデントを行う

- **グループ**: テキスト編集命令

**構文**
```
hsed_unindent p1
```

**パラメータ**
- `p1`: アンインデントを行うFootyのID

**説明**

Footyに対してアンインデントを行うように要請します。
アンインデントは選択範囲に対して行われます。

**関連**: hsed_indent

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_selectall idFooty
		hsed_unindent idFooty
	loop
	stop
```

---

### hsed_uninitduppipe

パイプハンドルの解放

- **グループ**: パイプ操作命令

**構文**
```
hsed_uninitduppipe
```

**パラメータ**
- なし

**説明**

; 解説文 を記入

**関連**: hsed_initduppipe

---

### hsed_initduppipe

パイプハンドルの作成

- **グループ**: パイプ操作命令

**構文**
```
hsed_initduppipe p1
```

**パラメータ**
- `p1`: 文字列の長さ

**説明**

; 解説文 を記入

**関連**: hsed_uninitduppipe

---

### hsed_getmajorver

メジャーバージョンを抽出

- **グループ**: バージョン抽出関数

**構文**
```
hsed_getmajorver(p1)
```

**パラメータ**
- `p1`: バージョンを表す整数値

**説明**

p1で指定されたバージョンからメジャー バージョンのみを抽出します。
ここで指定できる値は、hsed_getverにHGV_PUBLICVERもしくはHGV_PRIVATEVERを指定して取得したバージョンのみです。

**関連**: hsed_getver, hsed_getminorver, hsed_getbetaver

---

### hsed_getminorver

マイナーバージョンを抽出

- **グループ**: バージョン抽出関数

**構文**
```
hsed_getminorver(p1)
```

**パラメータ**
- `p1`: バージョンを表す整数値

**説明**

p1で指定されたバージョンからマイナー バージョンのみを抽出します。
ここで指定できる値は、hsed_getverにHGV_PUBLICVERもしくはHGV_PRIVATEVERを指定して取得したバージョンのみです。

**関連**: hsed_getver, hsed_getmajorver, hsed_getbetaver

---

### hsed_getbetaver

ベータバージョンを抽出

- **グループ**: バージョン抽出関数

**構文**
```
hsed_getbetaver(p1)
```

**パラメータ**
- `p1`: バージョンを表す整数値

**説明**

p1で指定されたバージョンからベータ バージョンのみを抽出します。
ここで指定できる値は、hsed_getverにHGV_PUBLICVERもしくはHGV_PRIVATEVERを指定して取得したバージョンのみです。

**関連**: hsed_getmajorver, hsed_getminorver, hsed_getver

---

### hsed_getver

スクリプトエディタのバージョンを取得

- **グループ**: 情報取得命令

**構文**
```
hsed_getver p1, p2
```

**パラメータ**
- `p1`: 結果を格納する変数
- `p2`: バージョンの種類を指定するための整数値

**説明**

p2で指定された種類のエディタのバージョンを取得し、p1に代入します。
取得に失敗した場合は、原則としてp1に-1を代入します。ただし、p2にHGV_HSPCMPVERが指定されていた場合は、"Error"を代入します。
^
statに代入される値は以下の通りです。
0: 取得に成功
1: エディタが見つからなかった
2: パイプが作れなかった
3: エディタが正しい値を返せなかった(p2が正しくない場合含む)
^
p2に指定する値は以下の通りです。HGV_で始まる定数を用いても、括弧内の数字を用いても構いません。
html{
<table border="1"><tr><th>HGV_PUBLICVER(0)</th>
<td>パブリック バージョン(エディタ公開時点での次のバージョン)。
16進数で<ul><li>下から4桁メジャー バージョン</li><li>下から3桁目マイナー バージョン</li></ul>を表します。(例:Ver3.6beta3→$0003603)<br />
hsed_getmajorver(), hsed_getminorver(), hsed_getbetaver()で各値を取得できます。<br />
また、hsed_cnvverstrで、文字列に変換することも可能です。</td></tr>
<tr><th>HGV_PRIVATEVER(1)</th>
<td>プライベート バージョン。HGV_PUBLICBERと同じ形式です。</td></tr>
<tr><th>HGV_HSPCMPVER(2)</th>
<td>hspcmp.dllからhsc_verで取得したバージョン(文字列)が代入されます。</td></tr>
<tr><th>HGV_FOOTYVER(3)</th>
<td>FootyからGetFootyVerで取得したバージョンが代入されます。
バージョンを100倍した数値が返ります。(例:Ver3.6→0x3600)</td></tr>
<tr><th nowrap>HGV_FOOTYBETAVER(4)</th>
<td>FootyからGetFootyBetaVerで取得したバージョンが代入されます。
ベータ バージョンがそのまま代入されます。
ベータ バージョンではない場合は0が代入されます。</td></tr>
</table>
}html

**関連**: hsed_getmajorver, hsed_getminorver, hsed_getbetaver

---

### hsed_getwnd

スクリプトエディタの各種ハンドルを取得

- **グループ**: ハンドル取得命令

**構文**
```
hsed_getwnd p1, p2, p3
```

**パラメータ**
- なし

**説明**

p2で指定された種類のエディタのウィンドウ ハンドルを取得し、p1に代入します。
p2でHGW_EDITを指定した場合は、p3でFootyのIDを指定する必要があります。
取得に失敗した場合は、p1に0を代入します。

statに代入される値は以下の通りです。
0: 取得に成功
1: エディタが見つからなかった
2: エディタが正しい値を返せなかった(p2が正しくない場合含む)

p2に指定する値は以下の通りです。HGW_で始まる定数を用いても、括弧内の数字を用いても構いません。
HGW_MAIN(0): メイン ウィンドウ
HGW_CLIENT(1): クライアント ウィンドウ
HGW_TAB(2): タブ ウィンドウ
HGW_EDIT(3): Footy ウィンドウ
HGW_TOOLBAR(4): ツールバー
HGW_STATUSBAR(5): ステータスバー

**関連**: hsed_capture

---

### hsed_cnvverstr

バージョンの数値を文字列に変換

- **グループ**: バージョン変換命令

**構文**
```
hsed_cnvverstr p1
```

**パラメータ**
- `p1`: バージョンを表す整数値

**説明**

p1で指定されたバージョンを文字列に変換し、refstrに代入します。"(メジャーバージョン).(マイナーバージョン)"の形式です。ただし、ベータバージョンの場合は末尾に"b(ベータバージョン)"が加えられます。
ここで指定できる値は、hsed_getverにHGV_PUBLICVERもしくはHGV_PRIVATEVERを指定して取得したバージョンのみです。

---

### hsed_selectall

テキストをすべて選択

- **グループ**: テキスト編集命令

**構文**
```
hsed_selectall p1
```

**パラメータ**
- `p1`: テキストを選択するFootyのID

**説明**

Footyに対してテキストをすべて選択するように要請します。

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_selectall idFooty
	loop
	stop
```

---

### hsed_gettextlength

テキストの文字列長を取得

- **グループ**: 情報取得命令

**構文**
```
hsed_gettextlength p1, p2
```

**パラメータ**
- `p1`: 文字列長を代入する変数
- `p2`: 文字列長を取得するFootyのID

**説明**

テキストの文字列長を取得し、p1へ代入します。

**関連**: hsed_getlinelength

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_gettextlength lText, idFooty
		mes "ID" + idFooty + "のFootyの文字列長は" + lText + "です。"
	loop
	stop
```

---

### hsed_getlines

テキストの行数を取得

- **グループ**: 情報取得命令

**構文**
```
hsed_getlines p1, p2
```

**パラメータ**
- `p1`: 行数を代入する変数
- `p2`: 行数を取得するFootyのID

**説明**

テキストの行数をp1に代入します。コメント行や空行も1行としてカウントされます。

**関連**: hsed_getlinelength

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	lText = ""
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_getlines nLines, idFooty
		mes "ID" + idFooty + "のFootyの行数は" + nLines + "です。"
	loop
	stop
```

---

### hsed_getlinelength

行の文字列長を取得

- **グループ**: 情報取得命令

**構文**
```
hsed_getlinelength p1, p2, p3
```

**パラメータ**
- `p1`: 文字列長を代入する変数
- `p2`: 文字列長を取得するFootyのID
- `p3`: 文字列長を取得する行の番号（1～）

**説明**

テキストのp3行目の文字列長を取得し、p1へ代入します。

**関連**: hsed_getlines, hsed_gettextlength

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_getlinelength lLine, idFooty, 1
		mes "ID" + idFooty + "のFootyの1行目の文字列長は" + lLine + "です。"
	loop
	stop
```

---

### hsed_getlinecode

改行コードを取得

- **グループ**: 情報取得命令

**構文**
```
hsed_getlinecode p1, p2
```

**パラメータ**
- なし

**説明**

; 解説文 を記入

**関連**: ; 関連項目 を記入

---

### hsed_copy

指定したFootyから文字列をコピー

- **グループ**: クリップボード操作命令

**構文**
```
hsed_copy p1
```

**パラメータ**
- `p1`: 文字列をコピーするFootyのID

**説明**

指定したFootyへ文字列をクリップボードにコピーするよう要請します。
コピーが行えるかどうかはhsed_cancopyで調べてください。

**関連**: hsed_cancopy, hsed_cut

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		if ( stat == 0 ) {
			hsed_cancopy ret, idFooty
			if ( ret ) {
				hsed_copy idFooty
				mes "ID" + str( cnt ) + "のタブからコピーしました。"
			}
		}
	loop
	stop
```

---

### hsed_paste

指定したFootyへ文字列を貼り付け

- **グループ**: クリップボード操作命令

**構文**
```
hsed_paste p1
```

**パラメータ**
- `p1`: 文字列を貼り付けるFootyのID

**説明**

指定したFootyへ文字列をクリップボードから貼り付けるよう要請します。
貼り付けが行えるかどうかはhsed_canpasteで調べてください。

**関連**: hsed_canpaste

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	hsed_canpaste ret
	if ( ret ) {
		repeat nTabs
			hsed_getfootyid idFooty, cnt
			if ( stat == 0 ) {
				hsed_paste idFooty
				mes "ID" + str( cnt ) + "のタブへ貼り付けました。"
			}
		loop
	} else {
		mes "貼り付けできません。"
	}
	stop
```

---

### hsed_canpaste

貼り付けの可否を取得

- **グループ**: 情報取得命令

**構文**
```
hsed_canpaste p1
```

**パラメータ**
- `p1`: 結果を格納する変数

**説明**

貼り付けの可否を取得します。
クリップボードから貼り付けすることができる場合はp1に1が返ります。
^
実際に貼り付けを行う場合はhsed_pasteを利用してください。

**関連**: hsed_paste, hsed_cancopy

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	hsed_canpaste ret
	if ( ret ) {
		mes "貼り付けできます。"
	} else {
		mes "貼り付けできません。"
	}
	stop
```

---

### hsed_canundo

アンドゥの可否を取得

- **グループ**: 情報取得命令

**構文**
```
hsed_canundo p1, p2
```

**パラメータ**
- `p1`: 結果を格納する変数
- `p2`: FootyのID

**説明**

指定したFootyのアンドゥの可否を取得します。
アンドゥが可能ならばp1に1が返ります。
^
実際にアンドゥを行う場合はhsed_undoを利用してください。

**関連**: hsed_undo, hsed_canredo

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_canundo ret, idFooty
		if ( ret ) {
			hsed_undo idFooty
			mes "ID" + idFooty + "のFootyをアンドゥしました。"
		} else {
			mes "ID" + idFooty + "のFootyはアンドゥできませんでした。"
		}
	loop
	stop
```

---

### hsed_canredo

リドゥの可否を取得

- **グループ**: 情報取得命令

**構文**
```
hsed_canredo p1, p2
```

**パラメータ**
- `p1`: 結果を格納する変数
- `p2`: FootyのID

**説明**

指定したFootyのリドゥの可否を取得します。
リドゥが可能ならばp1に1が返ります。
^
実際にリドゥを行う場合はhsed_redoを利用してください。

**関連**: hsed_redo, hsed_canundo

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_canredo ret, idFooty
		if ( ret ) {
			hsed_redo idFooty
			mes "ID" + idFooty + "のFootyをリドゥしました。"
		} else {
			mes "ID" + idFooty + "のFootyはリドゥできませんでした。"
		}
	loop
	stop
```

---

### hsed_getmodify

変更フラグを取得

- **グループ**: 情報取得命令

**構文**
```
hsed_getmodify p1, p2
```

**パラメータ**
- `p1`: 結果を格納する変数
- `p2`: FootyのID

**説明**

指定したFootyの変更フラグを取得します。
変更されていればp1には1が返ります。

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getfootyid idFooty, cnt
		hsed_getmodify ret, idFooty
		if ( ret ) {
			mes "ID" + idFooty + "のFootyは変更されています。"
		} else {
			mes "ID" + idFooty + "のFootyは変更されていません。"
		}
	loop
	stop
```

---

### hsed_settext

テキストを変更

- **グループ**: テキスト編集命令

**構文**
```
hsed_settext p1, p2
```

**パラメータ**
- `p1`: 変更したいFootyのID
- `p2`: 変更するテキスト

**説明**

HSPスクリプトエディタで編集中のテキストをp2に変更します。
^
変更に成功した場合はシステム変数statに0が代入されます。

**関連**: hsed_gettext, hsed_sendstr

**サンプル**
```hsp
#include "hsedsdk.as"
	nTabID = 0
	hsed_getfootyid nFootyID, nTabID
	if ( stat == 0 ) : hsed_settext nFootyID, "変更されたテキスト"
	stop
```

---

### hsed_getfootyid

タブのIDからFootyのIDを取得

- **グループ**: 情報取得命令

**構文**
```
hsed_getfootyid p1, p2
```

**パラメータ**
- `p1`: FootyのIDを代入する変数
- `p2`: タブのID

**説明**

; 解説文 を記入

**関連**: hsed_getactfootyid, hsed_gettabid, hsed_getacttabid

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTab
	repeat nTab
		hsed_getfootyid idFooty, cnt
		mes str( cnt ) + "番目のFootyのIDは" + idFooty + "です。"
	loop
	stop
```

---

### hsed_gettabid

FootyのIDからタブのIDを取得

- **グループ**: 情報取得命令

**構文**
```
hsed_gettabid p1, p2
```

**パラメータ**
- `p1`: タブのIDを代入する変数
- `p2`: FootyのID

**説明**

; 解説文 を記入

**関連**: hsed_getacttabid, hsed_getfootyid, hsed_getactfootyid

---

### hsed_gettabcount

タブ数の取得

- **グループ**: 情報取得命令

**構文**
```
hsed_gettabcount p1
```

**パラメータ**
- `p1`: タブ数を代入する変数

**説明**

HSPスクリプトエディタのエディタ部上部に表示されているタブ数を取得してp1に代入します。
^
取得に成功した場合はシステム変数statに0が代入されます。

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTab
	if ( stat == 0 ) : mes "HSPスクリプトエディタのタブ数は" + nTab + "です。"
```

---

### hsed_getactfootyid

アクティブなFootyのIDの取得

- **グループ**: 情報取得命令

**構文**
```
hsed_getactfootyid p1
```

**パラメータ**
- `p1`: FootyのIDを代入する変数

**説明**

HSPスクリプトエディタのアクティブなタブに表示されているFootyのIDを取得してp1に代入します。
^
取得に成功した場合はシステム変数statに0が代入されます。
^
取得に失敗した場合はシステム変数statに1が代入され、p1に-1が代入されます。

**関連**: hsed_getacttabid, hsed_gettabid, hsed_getfootyid

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_getactfootyid idFooty
	if ( stat == 0 ) : mes "アクティブなFootyのIDは" + idFooty + "です。"
```

---

### hsed_getacttabid

アクティブなタブのIDの取得

- **グループ**: 情報取得命令

**構文**
```
hsed_getacttabid p1
```

**パラメータ**
- `p1`: タブのIDを代入する変数

**説明**

HSPスクリプトエディタのアクティブなタブのIDを取得してp1に代入します。
^
取得に成功した場合はシステム変数statに0が代入されます。
^
取得に失敗した場合はシステム変数statに1が代入され、p1に-1が代入されます。

**関連**: hsed_getactfootyid, hsed_getfootyid, hsed_gettabid

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_getactfootyid idTab
	if ( stat == 0 ) : mes "アクティブなタブのIDは" + idTab + "です。"
```

---

### hsed_getpath

タブIDからファイルパスを取得

- **グループ**: 情報取得命令

**構文**
```
hsed_getpath p1, p2
```

**パラメータ**
- `p1`: ファイルパスを代入する変数
- `p2`: タブのID

**説明**

HSPスクリプトエディタで開いているファイルのパス名を取得し、p1に代入します。
^
取得に成功した場合はシステム変数statに0が代入されます。

**サンプル**
```hsp
#include "hsedsdk.as"
	hsed_gettabcount nTabs
	if ( stat ) {
		dialog "HSPエディタが見つかりません。", 1
		end
	}
	repeat nTabs
		hsed_getpath path, cnt
		if stat == 0 {
			mes "ID" + cnt + "のタブのファイルパスは\""+path+"\"です。"
		}
	loop
	stop
```

---
