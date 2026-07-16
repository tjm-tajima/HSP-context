# obj

- **種別**: ユーザー拡張命令
- **グループ**: オブジェクト制御命令
- **バージョン**: 3.3
- **更新日**: 2009/08/01
- **作者**: onitama
- **対応環境**: Win
- **備考**: obj.asをインクルードすること。

## 命令一覧

| 命令 | 概要 |
|---|---|
| [getobjsize](#getobjsize) | オブジェクトのサイズと位置取得 |
| [resizeobj](#resizeobj) | オブジェクトのサイズ変更 |
| [objgray](#objgray) | オブジェクトの使用可、不可設定 |
| [p_scrwnd](#p_scrwnd) | スクリーン座標系をウィンドウ座標系に変換 |

## 命令詳細

### getobjsize

オブジェクトのサイズと位置取得

**構文**
```
getobjsize p1, p2
```

**パラメータ**
- `p1`: オブジェクトのサイズ、位置を取得するための数値型配列変数
- `p2`: オブジェクトID

**説明**

オブジェクトのサイズと位置を取得します。
p2にはbuttonやlistviewなど取得するオブジェクトのIDを指定します。

p1にはオブジェクトのサイズ・位置が以下のように代入されます。
	p1(0)	幅
	p1(1)	高さ
	p1(2)	左上のx座標
	p1(3)	左上のy座標
	p1(4)	右下のx座標
	p1(5)	右下のy座標
各座標はウィンドウ座標系です。

**関連**: resizeobj

**サンプル**
```hsp
#include "obj.as"
	button "サンプル", *dummy
	getobjsize size, stat
	mes "ボタンの幅　：" + size(0)
	mes "ボタンの高さ：" + size(1)
*dummy
	stop
```

---

### resizeobj

オブジェクトのサイズ変更

**構文**
```
resizeobj p1, p2, p3
```

**パラメータ**
- `p1`: オブジェクトID
- `p2`: サイズ・位置が入った数値型配列変数
- `p3`: 位置・サイズを変更しないかどうかのフラグ

**説明**

IDp1のオブジェクトのサイズを変更します。
p2には幅,高さ,x座標,y座標の順に代入しておきます。

p3を1にすると位置を変えずにサイズだけ変更します。
p3を2にするとサイズを変えずに位置だけ変更します。

**関連**: getobjsize

**サンプル**
```hsp
#include "obj.as"
	button "width*2", *wx2
	button "height*2", *hx2
	input s, 100, 20
	ipt_id = stat		// オブジェクトIDを変数へ代入
	// 幅を40、高さを30にして(0, 80)に移動する
	s = 40, 30, 0, 80
	resizeobj ipt_id, s
	stop
*wx2
	; 幅を2倍にする
	getobjsize s, ipt_id
	s(0) *= 2
	resizeobj ipt_id, s
	stop
*hx2
	; 高さを2倍にする
	getobjsize s, ipt_id
	s(1) *= 2
	resizeobj ipt_id, s
	stop
```

---

### objgray

オブジェクトの使用可、不可設定

**構文**
```
objgray p1, p2
```

**パラメータ**
- `p1`: オブジェクトID
- `p2`: 使用可にするか不可にするかのフラグ

**説明**

buttonなどのオブジェクトを使用可にしたり、不可にしたりします。
p1にはbuttonやlistviewなどのIDを代入します。

p2を0にするとオブジェクトを使用できない状態にし、1にすると使用できる状態にします。
p2を-1にするとそのオブジェクトが使用可か不可かを調べます。

**サンプル**
```hsp
#include "obj.as"
	button "押せないボタン", *dummy
	objgray stat, 0
*dummy
	stop
```

---

### p_scrwnd

スクリーン座標系をウィンドウ座標系に変換

**構文**
```
p_scrwnd p1
```

**パラメータ**
- `p1`: スクリーン座標系が入った数値型配列変数

**説明**

スクリーン座標系をウィンドウ座標系に変換します。
p1(0)にx座標、p1(1)にy座標を代入しておきます。
描画対象となっているウィンドウを基準にします。

**サンプル**
```hsp
#include "obj.as"
	scr_pos = ginfo_mx, ginfo_my
	p_scrwnd scr_pos
	message  = "マウスポインタのスクリーン座標は" + ginfo_mx + "," + ginfo_my + "です。\n"
	message += "マウスポインタのウィンドウ座標は" + scr_pos(0) + "," + scr_pos(1) + "です。\n"
	message += "システム変数mousex,mouseyは" + mousex + "," + mousey + "です。"
	dialog message
	stop
```

---
