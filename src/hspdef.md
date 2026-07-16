# hspdef

- **種別**: システム定義マクロ
- **グループ**: 標準定義マクロ
- **バージョン**: 3.6
- **更新日**: 2019/04/09
- **作者**: onitama
- **対応環境**: Win / Mac / Cli
- **備考**: このマクロはhspdef.as内で定義されています。

## 命令一覧

| 命令 | 概要 |
|---|---|
| [gmode_sub](#gmode_sub) | 色減算合成コピーモード |
| [gmode_add](#gmode_add) | 色加算合成コピーモード |
| [gmode_gdi](#gmode_gdi) | 通常のコピーモード |
| [gmode_rgb0](#gmode_rgb0) | 透明色付きコピーモード |
| [gmode_mem](#gmode_mem) | メモリ間コピーモード |
| [gmode_alpha](#gmode_alpha) | 半透明合成コピーモード |
| [gmode_rgb0alpha](#gmode_rgb0alpha) | 透明色付き半透明合成コピーモード |
| [gmode_pixela](#gmode_pixela) | ピクセルアルファブレンドコピーモード |
| [objinfo_mode](#objinfo_mode) | モードおよびオプションデータを取得 |
| [objinfo_bmscr](#objinfo_bmscr) | オブジェクトが配置されているBMSCR構造体のポインタを取得 |
| [objinfo_hwnd](#objinfo_hwnd) | ウィンドウオブジェクトのハンドルを取得 |
| [screen_normal](#screen_normal) | 通常のウィンドウを作成 |
| [screen_palette](#screen_palette) | パレットモードのウィンドウを作成 |
| [screen_hide](#screen_hide) | 非表示のウィンドウを作成 |
| [screen_fixedsize](#screen_fixedsize) | サイズ固定ウィンドウを作成 |
| [screen_tool](#screen_tool) | ツールウィンドウを作成 |
| [screen_frame](#screen_frame) | 深い縁のあるウィンドウを作成 |
| [font_normal](#font_normal) | 通常のスタイルでフォント設定 |
| [font_bold](#font_bold) | 太文字でフォント設定 |
| [font_italic](#font_italic) | イタリック体でフォント設定 |
| [font_underline](#font_underline) | 下線付きでフォント設定 |
| [font_strikeout](#font_strikeout) | 打ち消し線付きでフォント設定 |
| [font_antialias](#font_antialias) | アンチエイリアスでフォント設定 |
| [objmode_normal](#objmode_normal) | HSP標準フォントを設定 |
| [objmode_guifont](#objmode_guifont) | デフォルトGUIフォントを設定 |
| [objmode_usefont](#objmode_usefont) | font命令で選択されているフォントを設定 |
| [objmode_usecolor](#objmode_usecolor) | objcolor命令で選択されている色を設定 |
| [msgothic](#msgothic) | MSゴシックフォント |
| [msmincho](#msmincho) | MS明朝フォント |
| [and](#and) | 論理積(演算子) |
| [or](#or) | 論理和(演算子) |
| [xor](#xor) | 排他的論理和(演算子) |
| [not](#not) | 否定(演算子) |
| [M_PI](#m_pi) | 円周率 |
| [rad2deg](#rad2deg) | ラジアンを度に変換 |
| [deg2rad](#deg2rad) | 度をラジアンに変換 |

## 命令詳細

### gmode_sub

色減算合成コピーモード

**構文**
```
gmode_sub
```

**パラメータ**
- なし

**説明**

gmodeの第1引数に指定することで、画面コピーモードを色減算合成コピーモードに設定できます。

**関連**: gmode, gmode_rgb0, gmode_mem, gmode_alpha, gmode_add, gmode_gdi, gmode_rgb0alpha, gmode_pixela

**サンプル**
```hsp
	screen 1 : picload dir_exe + "/sample/demo/logop.bmp"
	img_width = ginfo_winx
	img_height = ginfo_winy
	gsel 0
	color       : boxf img_width / 5, 0, img_width  * 2 / 5, ginfo_winy
	color 255   : boxf img_width * 2 / 5, 0, img_width * 3 / 5, ginfo_winy
	color ,255  : boxf img_width * 3 / 5, 0, img_width * 4 / 5, ginfo_winy
	color ,,255 : boxf img_width * 4 / 5, 0, img_width, ginfo_winy
	gmode gmode_sub, img_width, img_height, 256
	gcopy 1, 0, 0
	stop
```

---

### gmode_add

色加算合成コピーモード

**構文**
```
gmode_add
```

**パラメータ**
- なし

**説明**

gmodeの第1引数に指定することで、画面コピーモードを色加算合成コピーモードに設定できます。

**関連**: gmode, gmode_rgb0, gmode_mem, gmode_alpha, gmode_sub, gmode_gdi, gmode_rgb0alpha, gmode_pixela

**サンプル**
```hsp
	screen 1 : picload dir_exe + "/sample/demo/logop.bmp"
	img_width = ginfo_winx
	img_height = ginfo_winy
	gsel 0
	color       : boxf img_width / 5, 0, img_width  * 2 / 5, ginfo_winy
	color 255   : boxf img_width * 2 / 5, 0, img_width * 3 / 5, ginfo_winy
	color ,255  : boxf img_width * 3 / 5, 0, img_width * 4 / 5, ginfo_winy
	color ,,255 : boxf img_width * 4 / 5, 0, img_width, ginfo_winy
	gmode gmode_add, img_width, img_height, 256
	gcopy 1, 0, 0
	stop
```

---

### gmode_gdi

通常のコピーモード

**構文**
```
gmode_gdi
```

**パラメータ**
- なし

**説明**

gmodeの第1引数に指定することで、画面コピーモードを通常のコピーモードに設定できます。
省略しても同じ結果が得られますので、省略しても構いません。

**関連**: gmode, gmode_rgb0, gmode_mem, gmode_alpha, gmode_add, gmode_sub, gmode_rgb0alpha, gmode_pixela

**サンプル**
```hsp
	buffer 1 : picload dir_exe + "/sample/demo/logop.bmp"
	img_width = ginfo_winx
	img_height = ginfo_winy
	gsel 0
	gmode gmode_gdi
	gcopy 1, 0, 0, img_width, img_height
	stop
```

---

### gmode_rgb0

透明色付きコピーモード

**構文**
```
gmode_rgb0
```

**パラメータ**
- なし

**説明**

gmodeの第1引数に指定することで、画面コピーモードを透明色付きコピーモードに設定できます。

**関連**: gmode, gmode_sub, gmode_mem, gmode_alpha, gmode_add, gmode_gdi, gmode_rgb0alpha, gmode_pixela

**サンプル**
```hsp
	screen 1 : picload dir_exe + "/sample/demo/logop.bmp"
	img_width = ginfo_winx
	img_height = ginfo_winy
	gsel 0
	gmode gmode_rgb0, img_width, img_height
	gcopy 1, 0, 0
	stop
```

---

### gmode_mem

メモリ間コピーモード

**構文**
```
gmode_mem
```

**パラメータ**
- なし

**説明**

gmodeの第1引数に指定することで、画面コピーモードをメモリ間コピーモードに設定できます。

**関連**: gmode, gmode_rgb0, gmode_sub, gmode_alpha, gmode_add, gmode_gdi, gmode_rgb0alpha, gmode_pixela

**サンプル**
```hsp
	screen 1 : picload dir_exe + "/sample/demo/logop.bmp"
	img_width = ginfo_winx
	img_height = ginfo_winy
	gsel 0
	gmode gmode_mem, img_width, img_height
	gcopy 1, 0, 0
	stop
```

---

### gmode_alpha

半透明合成コピーモード

**構文**
```
gmode_alpha
```

**パラメータ**
- なし

**説明**

gmodeの第1引数に指定することで、画面コピーモードを半透明合成コピーモードに設定できます。

**関連**: gmode, gmode_rgb0, gmode_mem, gmode_sub, gmode_add, gmode_gdi, gmode_rgb0alpha, gmode_pixela

**サンプル**
```hsp
	screen 1 : picload dir_exe + "/sample/demo/logop.bmp"
	img_width = ginfo_winx
	img_height = ginfo_winy
	gsel 0
	color       : boxf img_width / 5, 0, img_width  * 2 / 5, ginfo_winy
	color 255   : boxf img_width * 2 / 5, 0, img_width * 3 / 5, ginfo_winy
	color ,255  : boxf img_width * 3 / 5, 0, img_width * 4 / 5, ginfo_winy
	color ,,255 : boxf img_width * 4 / 5, 0, img_width, ginfo_winy
	gmode gmode_alpha, img_width, img_height, 128
	gcopy 1, 0, 0
	stop
```

---

### gmode_rgb0alpha

透明色付き半透明合成コピーモード

**構文**
```
gmode_rgb0alpha
```

**パラメータ**
- なし

**説明**

gmodeの第1引数に指定することで、画面コピーモードを透明色付き半透明合成コピーモードに設定できます。

**関連**: gmode, gmode_rgb0, gmode_mem, gmode_alpha, gmode_add, gmode_gdi, gmode_sub, gmode_pixela

**サンプル**
```hsp
	screen 1 : picload dir_exe + "/sample/demo/logop.bmp"
	img_width = ginfo_winx
	img_height = ginfo_winy
	gsel 0
	color   0,   0,   0 : boxf img_width / 5, 0, img_width  * 2 / 5, ginfo_winy
	color 255,   0,   0 : boxf img_width * 2 / 5, 0, img_width * 3 / 5, ginfo_winy
	color   0, 255,   0 : boxf img_width * 3 / 5, 0, img_width * 4 / 5, ginfo_winy
	color   0,   0, 255 : boxf img_width * 4 / 5, 0, img_width, ginfo_winy
	gmode gmode_rgb0alpha, img_width, img_height, 128
	color 0, 0, 0
	gcopy 1, 0, 0
	stop
```

---

### gmode_pixela

ピクセルアルファブレンドコピーモード

**構文**
```
gmode_pixela
```

**パラメータ**
- なし

**説明**

gmodeの第1引数に指定することで、画面コピーモードをピクセルアルファブレンドコピーモードに設定できます。

**関連**: gmode, gmode_rgb0, gmode_mem, gmode_alpha, gmode_add, gmode_gdi, gmode_rgb0alpha, gmode_sub

**サンプル**
```hsp
	screen 1 : picload dir_exe + "/sample/demo/logop.bmp"
	img_width = ginfo_winx
	img_height = ginfo_winy
	screen 1, img_width * 2, img_height : picload dir_exe + "/sample/demo/logop.bmp", 1
	repeat img_width
		hsvcolor cnt * 192 / ( img_width  ), 255, 255
		line img_width + cnt, img_height, img_width + cnt, 0
	loop
	gsel 0
	gmode gmode_pixela, img_width, img_height, 128
	gcopy 1, 0, 0
	stop
```

---

### objinfo_mode

モードおよびオプションデータを取得

**構文**
```
objinfo_mode(p1)
```

**パラメータ**
- `p1=0～`: ウィンドウオブジェクトID

**説明**

指定したウィンドウオブジェクトのモードおよびオプションデータを返します。

**関連**: objinfo, objinfo_hwnd, objinfo_bmscr

**サンプル**
```hsp
	button goto "sample", *dummy
	info = objinfo_mode( stat )
	mes "mode : " + ( info & 0xffff )
	mes "option : " + ( info >> 16 & 0xffff )

*dummy
	stop
```

---

### objinfo_bmscr

オブジェクトが配置されているBMSCR構造体のポインタを取得

**構文**
```
objinfo_bmscr(p1)
```

**パラメータ**
- `p1=0～`: ウィンドウオブジェクトID

**説明**

指定したウィンドウオブジェクトが配置されているBMSCR構造体のポインタを返します。

**関連**: objinfo, objinfo_mode, objinfo_hwnd

**サンプル**
```hsp
	button goto "sample", *dummy
	p_bmscr = objinfo_bmscr( stat )
	mes "objectが配置されているBMSCR構造体のポインタ : " + p_bmscr
	mref bmscr, 67
	mes "mrefで得られる値（" + varptr( bmscr ) + "）と同等"

*dummy
	stop
```

---

### objinfo_hwnd

ウィンドウオブジェクトのハンドルを取得

**構文**
```
objinfo_hwnd(p1)
```

**パラメータ**
- `p1=0～`: ウィンドウオブジェクトID

**説明**

指定したウィンドウオブジェクトのハンドルを返します。

**関連**: objinfo, objinfo_mode, objinfo_bmscr

**サンプル**
```hsp
	button goto "sample", *dummy
	obj_hwnd = objinfo_hwnd( stat )
	mes "ウィンドウオブジェクトのハンドル : " + obj_hwnd

*dummy
	stop
```

---

### screen_normal

通常のウィンドウを作成

**構文**
```
screen_normal
```

**パラメータ**
- なし

**説明**

screen命令の第4引数に指定することで、通常のウィンドウを作成できます。
省略しても同じ結果が得られますので、省略しても構いません。

**関連**: screen, screen_palette, screen_hide, screen_fixedsize, screen_tool, screen_frame

**サンプル**
```hsp
// ウィンドウID0の通常のウィンドウを作成
	screen 0, 640, 480, screen_normal

// 省略しても同じ結果が得られる
	screen 1, 320, 240
	stop
```

---

### screen_palette

パレットモードのウィンドウを作成

**構文**
```
screen_palette
```

**パラメータ**
- なし

**説明**

screen命令の第4引数に指定することで、パレットモードのウィンドウを作成できます。
他のマクロと組み合わせて指定する場合は、その和または論理和を指定してください。

**関連**: screen, screen_normal, screen_hide, screen_fixedsize, screen_tool, screen_frame

**サンプル**
```hsp
// ウィンドウID0のウィンドウをパレットモードで作成
	screen 0, 640, 480, screen_palette
	stop
```

---

### screen_hide

非表示のウィンドウを作成

**構文**
```
screen_hide
```

**パラメータ**
- なし

**説明**

screen命令の第4引数に指定することで、非表示のウィンドウを作成できます。
他のマクロと組み合わせて指定する場合は、その和または論理和を指定してください。

**関連**: screen, screen_normal, screen_palette, screen_fixedsize, screen_tool, screen_frame

**サンプル**
```hsp
// ウィンドウID0のウィンドウを非表示で作成
	screen 0, 640, 480, screen_hide
	stop
```

---

### screen_fixedsize

サイズ固定ウィンドウを作成

**構文**
```
screen_fixedsize
```

**パラメータ**
- なし

**説明**

screen命令の第4引数に指定することで、サイズ固定のウィンドウを作成できます。
他のマクロと組み合わせて指定する場合は、その和または論理和を指定してください。

**関連**: screen, screen_normal, screen_palette, screen_hide, screen_tool, screen_frame

**サンプル**
```hsp
// ウィンドウID0のウィンドウをサイズ固定で作成
	screen 0, 640, 480, screen_fixedsize
	stop
```

---

### screen_tool

ツールウィンドウを作成

**構文**
```
screen_tool
```

**パラメータ**
- なし

**説明**

screen命令の第4引数に指定することで、ツールウィンドウを作成できます。
他のマクロと組み合わせて指定する場合は、その和または論理和を指定してください。

**関連**: screen, screen_normal, screen_palette, screen_hide, screen_fixedsize, screen_frame

**サンプル**
```hsp
// ウィンドウID0のツールウィンドウを作成
	screen 0, 640, 480, screen_tool
	stop
```

---

### screen_frame

深い縁のあるウィンドウを作成

**構文**
```
screen_frame
```

**パラメータ**
- なし

**説明**

screen命令の第4引数に指定することで、深い縁のあるウィンドウを作成できます。
他のマクロと組み合わせて指定する場合は、その和または論理和を指定してください。

**関連**: screen, screen_normal, screen_palette, screen_hide, screen_fixedsize, screen_tool

**サンプル**
```hsp
// ウィンドウIDの深い縁のあるウィンドウを作成
	screen 0, 640, 480, screen_frame
	stop
```

---

### font_normal

通常のスタイルでフォント設定

**構文**
```
font_normal
```

**パラメータ**
- なし

**説明**

font命令の第3引数に指定することで、通常のスタイルでフォントを設定することができます。
省略しても同じ結果が得られますので、省略しても構いません。

**関連**: font, font_bold, font_italic, font_underline, font_strikeout, font_antialias

**サンプル**
```hsp
// サイズ12のMSゴシックを設定
	font msgothic, 24, font_normal
	mes "サイズ24のMSゴシック（通常のスタイル）"

// 省略しても同じ結果が得られる
	font msgothic, 24
	mes "サイズ24のMSゴシック（通常のスタイル）"
	stop
```

---

### font_bold

太文字でフォント設定

**構文**
```
font_bold
```

**パラメータ**
- なし

**説明**

font命令の第3引数に指定することで、太文字のフォントを設定することができます。
他のマクロと組み合わせて指定する場合は、その和または論理和を指定してください。

**関連**: font, font_normal, font_italic, font_underline, font_strikeout, font_antialias

**サンプル**
```hsp
// サイズ24のMSゴシックを設定
	font msgothic, 24, font_normal
	mes "サイズ24のMSゴシック（通常のスタイル）"

// サイズ24で太文字のMSゴシックを設定
	font msgothic, 24, font_bold
	mes "サイズ24のMSゴシック（太文字）"
	stop
```

---

### font_italic

イタリック体でフォント設定

**構文**
```
font_italic
```

**パラメータ**
- なし

**説明**

font命令の第3引数に指定することで、イタリック体のフォントを設定することができます。
他のマクロと組み合わせて指定する場合は、その和または論理和を指定してください。

**関連**: font, font_normal, font_bold, font_underline, font_strikeout, font_antialias

**サンプル**
```hsp
// サイズ24のMSゴシックを設定
	font msgothic, 24, font_normal
	mes "サイズ24のMSゴシック（通常のスタイル）"

// サイズ24でイタリック体MSmsゴシックを設定
	font msgothic, 24, font_italic
	mes "サイズ24のMSゴシック（イタリック体）"
	stop
```

---

### font_underline

下線付きでフォント設定

**構文**
```
font_underline
```

**パラメータ**
- なし

**説明**

font命令の第3引数に指定することで、下線付きのフォントを設定することができます。
他のマクロと組み合わせて指定する場合は、その和または論理和を指定してください。

**関連**: font, font_normal, font_bold, font_italic, font_strikeout, font_antialias

**サンプル**
```hsp
// サイズ24のMSゴシックを設定
	font msgothic, 24, font_normal
	mes "サイズ24のMSゴシック（通常のスタイル）"

// サイズ24で下線付きのMSゴシックを設定
	font msgothic, 24, font_underline
	mes "サイズ24のMSゴシック（下線付き）"
	stop
```

---

### font_strikeout

打ち消し線付きでフォント設定

**構文**
```
font_strikeout
```

**パラメータ**
- なし

**説明**

font命令の第3引数に指定することで、打ち消し線付きのフォントを設定することができます。
他のマクロと組み合わせて指定する場合は、その和または論理和を指定してください。

**関連**: font, font_normal, font_bold, font_italic, font_underline, font_antialias

**サンプル**
```hsp
// サイズ24のMSゴシックを設定
	font msgothic, 24, font_normal
	mes "サイズ24のMSゴシック（通常のスタイル）"

// サイズ24で打ち消し線付きのMSゴシックを設定
	font msgothic, 24, font_strikeout
	mes "サイズ24のMSゴシック（打ち消し線付き）"
	stop
```

---

### font_antialias

アンチエイリアスでフォント設定

**構文**
```
font_antialias
```

**パラメータ**
- なし

**説明**

font命令の第3引数に指定することで、アンチエイリアスのフォントを設定することができます。
他のマクロと組み合わせて指定する場合は、その和または論理和を指定してください。

**関連**: font, font_normal, font_bold, font_italic, font_underline, font_strikeout

**サンプル**
```hsp
// サイズ24のMSゴシックを設定
	font msgothic, 24, font_normal
	mes "サイズ24のMSゴシック（通常のスタイル）"

// サイズ24でアンチエイリアスのMSゴシックを設定
	font msgothic, 24, font_antialias
	mes "サイズ24のMSゴシック（アンチエイリアス）"
	stop
```

---

### objmode_normal

HSP標準フォントを設定

**構文**
```
objmode_normal
```

**パラメータ**
- なし

**説明**

objmode命令の第1引数に指定することで、オブジェクト制御命令で使用されるフォントをHSP標準フォントに設定することができます。
省略しても同じ結果が得られますので、省略しても構いません。

**関連**: objmode, objmode_guifont, objmode_usefont, objmode_usecolor

**サンプル**
```hsp
	s = "オブジェクト制御命令で使用されるフォントのサンプル"

// オブジェクト制御命令で使用されるフォントをHSP標準フォントに設定
	objmode objmode_normal
	mesbox s, ginfo_winx, ginfo_winy / 2

// 省略しても同じ結果が得られる
	objmode objmode_normal
	mesbox s, ginfo_winx, ginfo_winy / 2

	stop
```

---

### objmode_guifont

デフォルトGUIフォントを設定

**構文**
```
objmode_guifont
```

**パラメータ**
- なし

**説明**

objmode命令の第1引数に指定することで、オブジェクト制御命令で使用されるフォントをデフォルトGUIフォントに設定することができます。

**関連**: objmode, objmode_normal, objmode_usefont, objmode_usecolor

**サンプル**
```hsp
	s = "オブジェクト制御命令で使用されるフォントのサンプル"

// オブジェクト制御命令で使用されるフォントをデフォルトGUIフォントに設定
	objmode objmode_guifont
	mesbox s, ginfo_winx, ginfo_winy

	stop
```

---

### objmode_usefont

font命令で選択されているフォントを設定

**構文**
```
objmode_usefont
```

**パラメータ**
- なし

**説明**

objmode命令の第1引数に指定することで、オブジェクト制御命令で使用されるフォントをfont命令で選択されているフォントに設定することができます。

**関連**: objmode, objmode_normal, objmode_guifont, objmode_usecolor

**サンプル**
```hsp
	s = "オブジェクト制御命令で使用されるフォントのサンプル"

// オブジェクト制御命令で使用されるフォントをfont命令で選択されているフォントに設定
	objmode objmode_usefont

	font msmincho, 24
	mesbox s, ginfo_winx, ginfo_winy / 2

	font msgothic, 18, font_italic
	mesbox s, ginfo_winx, ginfo_winy / 2

	stop
```

---

### objmode_usecolor

objcolor命令で選択されている色を設定

**構文**
```
objmode_usecolor
```

**パラメータ**
- なし

**説明**

objmode命令の第1引数に指定することで、オブジェクト制御命令で使用される色をcolor命令、objcolor命令で指定されている色に設定することができます。

**関連**: objmode, objmode_normal, objmode_guifont, objmode_usefont

---

### msgothic

MSゴシックフォント

- **グループ**: システム変数

**構文**
```
msgothic
```

**パラメータ**
- なし

**説明**

MSゴシックを示すフォントを示すキーワードです。
font命令で指定するフォント名として使用することができます。

**関連**: msmincho, ;---------------------------------------------------------------------

---

### msmincho

MS明朝フォント

- **グループ**: システム変数

**構文**
```
msmincho
```

**パラメータ**
- なし

**説明**

MS明朝を示すフォントを示すキーワードです。
font命令で指定するフォント名として使用することができます。

**関連**: msgothic, ;---------------------------------------------------------------------

---

### and

論理積(演算子)

- **グループ**: 標準定義マクロ

**構文**
```
and
```

**パラメータ**
- なし

**説明**

論理積を示す演算子「&」と同様に使用することができるマクロです。

**関連**: or, xor, not, ;---------------------------------------------------------------------

---

### or

論理和(演算子)

- **グループ**: 標準定義マクロ

**構文**
```
or
```

**パラメータ**
- なし

**説明**

論理和を示す演算子「|」と同様に使用することができるマクロです。

**関連**: and, xor, not, ;---------------------------------------------------------------------

---

### xor

排他的論理和(演算子)

- **グループ**: 標準定義マクロ

**構文**
```
xor
```

**パラメータ**
- なし

**説明**

排他的論理和を示す演算子「^」と同様に使用することができるマクロです。

**関連**: and, or, not, ;---------------------------------------------------------------------

---

### not

否定(演算子)

- **グループ**: 標準定義マクロ

**構文**
```
not
```

**パラメータ**
- なし

**説明**

否定を示す演算子「!」と同様に使用することができるマクロです。

**関連**: and, or, xor, ;---------------------------------------------------------------------

---

### M_PI

円周率

- **グループ**: 数学定数

**構文**
```
M_PI
```

**パラメータ**
- なし

**説明**

円周率を表す定数です。3.14159265358979323846が定義されています。

**関連**: rad2deg, deg2rad, ;---------------------------------------------------------------------

---

### rad2deg

ラジアンを度に変換

**構文**
```
rad2deg(p1)
```

**パラメータ**
- `p1`: 度に変換する角度（ラジアン）

**説明**

角度の単位をラジアンから度へ変換します。
弧度法で表された角度を度数法での角度に変換するとも言えます。

**関連**: M_PI, deg2rad, ;---------------------------------------------------------------------

**サンプル**
```hsp
	tmp = M_PI
	mes str(tmp) + "ラジアンは" + rad2deg(tmp) + "°です。"
	stop
```

---

### deg2rad

度をラジアンに変換

**構文**
```
deg2rad(p1)
```

**パラメータ**
- `p1`: ラジアンに変換する角度（度）

**説明**

角度の単位を度からラジアンへ変換します。
度数法で表された角度を弧度法での角度に変換するとも言えます。

**関連**: M_PI, rad2deg

**サンプル**
```hsp
	tmp = 90
	mes str(tmp) + "°は" + deg2rad(tmp) + "ラジアンです。"
	stop
```

---
