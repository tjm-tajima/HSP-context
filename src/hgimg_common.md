# hgimg4

- **種別**: 拡張命令
- **バージョン**: 3.6
- **更新日**: 2021/01/18
- **作者**: onitama / onitama
- **URL**: http://www.onionsoft.net/
- **対応環境**: Win
- **動作条件**: HGIMG4DXはDirectX9、HGIMG4はOpenGL3.1環境で動作
- **備考**: hgimg4dx.asまたはhgimg4.asをインクルードすること。
- **補足**: この命令群は hgimg3.as と hgimg4.as/hgimg4dx.as のどちらと組み合わせても使用できる、オブジェクト操作の共通処理です(HGIMG4専用ではありません)。

## 命令一覧

| 命令 | 概要 |
|---|---|
| [fvseti](#fvseti) | 整数値からベクトル設定 |
| [fvset](#fvset) | ベクトル設定 |
| [fvadd](#fvadd) | ベクトル加算 |
| [fvsub](#fvsub) | ベクトル減算 |
| [fvmul](#fvmul) | ベクトル乗算 |
| [fvdiv](#fvdiv) | ベクトル除算 |
| [fvdir](#fvdir) | ベクトル回転 |
| [fvface](#fvface) | 座標から角度を得る |
| [fvmin](#fvmin) | ベクトルの要素を最小値で切り詰める |
| [fvmax](#fvmax) | ベクトルの要素を最大値で切り詰める |
| [fvouter](#fvouter) | ベクトル外積 |
| [fvinner](#fvinner) | ベクトル内積 |
| [fvunit](#fvunit) | ベクトル正規化 |
| [fsin](#fsin) | サインを求める |
| [fcos](#fcos) | コサインを求める |
| [fsqr](#fsqr) | 平方根を求める |
| [str2fv](#str2fv) | 文字列をベクトルに変換 |
| [fv2str](#fv2str) | ベクトルを文字列に変換 |
| [str2f](#str2f) | 文字列を小数値に変換 |
| [f2str](#f2str) | 小数値を文字列に変換 |
| [delobj](#delobj) | オブジェクトの削除 |
| [setpos](#setpos) | posグループ情報を設定 |
| [setang](#setang) | angグループ情報を設定 |
| [setangr](#setangr) | angグループ情報を設定 |
| [setscale](#setscale) | scaleグループ情報を設定 |
| [setdir](#setdir) | dirグループ情報を設定 |
| [setwork](#setwork) | workグループ情報を設定 |
| [addpos](#addpos) | posグループ情報を加算 |
| [addang](#addang) | angグループ情報を加算 |
| [addangr](#addangr) | angグループ情報を加算 |
| [addscale](#addscale) | scaleグループ情報を加算 |
| [adddir](#adddir) | dirグループ情報を加算 |
| [addwork](#addwork) | workグループ情報を加算 |
| [getpos](#getpos) | posグループ情報を取得 |
| [getscale](#getscale) | scaleグループ情報を取得 |
| [getdir](#getdir) | dirグループ情報を取得 |
| [getwork](#getwork) | workグループ情報を取得 |
| [getposi](#getposi) | posグループ情報を整数で取得 |
| [getscalei](#getscalei) | scaleグループ情報を整数で取得 |
| [getdiri](#getdiri) | dirグループ情報を整数で取得 |
| [getworki](#getworki) | workグループ情報を整数で取得 |
| [selpos](#selpos) | 移動座標をMOC情報に設定 |
| [selang](#selang) | 回転角度をMOC情報に設定 |
| [selscale](#selscale) | スケールをMOC情報に設定 |
| [seldir](#seldir) | 移動量をMOC情報に設定 |
| [selwork](#selwork) | オブジェクトワークをMOC情報に設定 |
| [objset3](#objset3) | MOC情報を設定 |
| [objsetf3](#objsetf3) | MOC情報を設定 |
| [objadd3](#objadd3) | MOC情報を加算 |
| [objaddf3](#objaddf3) | MOC情報を加算 |
| [objadd3r](#objadd3r) | MOC情報を加算 |
| [objset3r](#objset3r) | MOC情報を設定 |
| [setobjmode](#setobjmode) | オブジェクトのモード設定 |
| [setcoli](#setcoli) | オブジェクトのコリジョン設定 |
| [getcoli](#getcoli) | オブジェクトのコリジョン判定 |
| [getobjcoli](#getobjcoli) | オブジェクトのグループ取得 |
| [setobjrender](#setobjrender) | オブジェクトのレンダリンググループ設定 |
| [findobj](#findobj) | オブジェクト検索 |
| [nextobj](#nextobj) | 次のオブジェクト検索 |
| [setborder](#setborder) | オブジェクト有効範囲設定 |
| [selmoc](#selmoc) | MOC情報を設定 |
| [objgetfv](#objgetfv) | MOC情報を取得 |
| [objsetfv](#objsetfv) | MOC情報を設定 |
| [objaddfv](#objaddfv) | MOC情報を加算 |
| [objexist](#objexist) | オブジェクトIDが有効か調べる |
| [event_wait](#event_wait) | 待ち時間イベントを追加 |
| [event_jump](#event_jump) | ジャンプイベントを追加 |
| [event_prmset](#event_prmset) | パラメーター設定イベントを追加 |
| [event_prmon](#event_prmon) | パラメータービット設定イベントを追加 |
| [event_prmoff](#event_prmoff) | パラメータービット消去イベントを追加 |
| [event_setpos](#event_setpos) | posグループ設定イベントを追加 |
| [event_setang](#event_setang) | angグループ設定イベントを追加 |
| [event_setangr](#event_setangr) | angグループ設定イベントを追加 |
| [event_setscale](#event_setscale) | scaleグループ設定イベントを追加 |
| [event_setdir](#event_setdir) | dirグループ設定イベントを追加 |
| [event_setwork](#event_setwork) | workグループ設定イベントを追加 |
| [event_pos](#event_pos) | posグループ変化イベントを追加 |
| [event_ang](#event_ang) | angグループ変化イベントを追加 |
| [event_angr](#event_angr) | angグループ変化イベントを追加 |
| [event_scale](#event_scale) | scaleグループ変化イベントを追加 |
| [event_dir](#event_dir) | dirグループ変化イベントを追加 |
| [event_work](#event_work) | workグループ変化イベントを追加 |
| [event_addpos](#event_addpos) | posグループ加算イベントを追加 |
| [event_addang](#event_addang) | angグループ加算イベントを追加 |
| [event_addangr](#event_addangr) | angグループ加算イベントを追加 |
| [event_addscale](#event_addscale) | scaleグループ加算イベントを追加 |
| [event_adddir](#event_adddir) | dirグループ加算イベントを追加 |
| [event_addwork](#event_addwork) | workグループ加算イベントを追加 |
| [setevent](#setevent) | オブジェクトにイベントを設定 |
| [delevent](#delevent) | イベントリストを削除 |
| [newevent](#newevent) | イベントリストを作成 |
| [getang](#getang) | angグループ情報を取得 |
| [getangr](#getangr) | angグループ情報を取得 |
| [event_delobj](#event_delobj) | オブジェクト削除イベントを追加 |

## 命令詳細

### fvseti

整数値からベクトル設定

- **グループ**: 拡張画面制御命令

**構文**
```
fvseti fv,x,y,z
```

**パラメータ**
- `fv      = FV値が代入される変数名`
- `(x,y,z) = 整数値`

**説明**

(x,y,z)で指定された整数値をベクトルとしてFV値に代入する。

**関連**: fvset, fvadd, fvsub, fvmul, fvdiv, fvdir, fvmin, fvmax, fvouter, fvinner, fvface, fvunit

---

### fvset

ベクトル設定

- **グループ**: 拡張画面制御命令

**構文**
```
fvset fv,x,y,z
```

**パラメータ**
- `fv      = FV値が代入される変数名`
- `(x,y,z) = 計算値(実数値)`

**説明**

(x,y,z)で指定された小数値(X,Y,Z)をベクトルとしてFV値に代入する。

**関連**: fvseti, fvadd, fvsub, fvmul, fvdiv, fvdir, fvmin, fvmax, fvouter, fvinner, fvface, fvunit

---

### fvadd

ベクトル加算

- **グループ**: 拡張画面制御命令

**構文**
```
fvadd fv,x,y,z
```

**パラメータ**
- `fv      = FV値が代入されている変数名`
- `(x,y,z) = 計算値(実数値)`

**説明**

(x,y,z)で指定された小数値(X,Y,Z)をFV値に加算する。

**関連**: fvseti, fvset, fvsub, fvmul, fvdiv, fvmin, fvmax

---

### fvsub

ベクトル減算

- **グループ**: 拡張画面制御命令

**構文**
```
fvsub fv,x,y,z
```

**パラメータ**
- `fv      = FV値が代入されている変数名`
- `(x,y,z) = 計算値(実数値)`

**説明**

(x,y,z)で指定された小数値(X,Y,Z)をFV値から減算する。

**関連**: fvseti, fvset, fvadd, fvmul, fvdiv, fvmin, fvmax

---

### fvmul

ベクトル乗算

- **グループ**: 拡張画面制御命令

**構文**
```
fvmul fv,x,y,z
```

**パラメータ**
- `fv      = FV値が代入されている変数名`
- `(x,y,z) = 計算値(実数値)`

**説明**

(x,y,z)で指定された小数値(X,Y,Z)をFV値に並列で乗算する。

**関連**: fvseti, fvset, fvadd, fvsub, fvdiv, fvmin, fvmax

---

### fvdiv

ベクトル除算

- **グループ**: 拡張画面制御命令

**構文**
```
fvdiv fv,x,y,z
```

**パラメータ**
- `fv      = FV値が代入されている変数名`
- `(x,y,z) = 計算値(実数値)`

**説明**

(x,y,z)で指定された小数値(X,Y,Z)をFV値に並列で除算する。

**関連**: fvseti, fvset, fvadd, fvsub, fvmul, fvmin, fvmax

---

### fvdir

ベクトル回転

- **グループ**: 拡張画面制御命令

**構文**
```
fvdir fv,x,y,z
```

**パラメータ**
- `fv      = FV値が代入されている変数名`
- `(x,y,z) = 回転角度(実数値)`

**説明**

fvで指定された変数に格納されているFV値をX,Y,Z角度として、
小数値(X,Y,Z)で指定されたベクトルを回転させた結果を、変数fvに代入します。

**関連**: fvset, fvdir, fvface

---

### fvface

座標から角度を得る

- **グループ**: 拡張画面制御命令

**構文**
```
fvface fv,x,y,z
```

**パラメータ**
- `fv      = FV値が代入されている変数名`
- `(x,y,z) = X,Y,Z座標値(実数値)`

**説明**

fvで指定された変数に格納されているベクトル(FV値)を基点とするX,Y,Z座標から、指定されたX,Y,Z座標を直線で見るためのX,Y,Z回転角度を求めて変数fvに代入します。

**関連**: fvset, fvdir

---

### fvmin

ベクトルの要素を最小値で切り詰める

- **グループ**: 拡張画面制御命令

**構文**
```
fvmin fv,x,y,z
```

**パラメータ**
- `fv      = FV値が代入されている変数名`
- `(x,y,z) = 比較値(実数値)`

**説明**

fvで指定された変数に格納されているFV値の各要素を、パラメーターで指定された値(X,Y,Z)が最小値になるように切り詰めます。
FV値の各要素に対して最小値を適用する場合に使用します。

**関連**: fvseti, fvset, fvadd, fvsub, fvmul, fvdiv, fvmax

---

### fvmax

ベクトルの要素を最大値で切り詰める

- **グループ**: 拡張画面制御命令

**構文**
```
fvmax fv,x,y,z
```

**パラメータ**
- `fv      = FV値が代入されている変数名`
- `(x,y,z) = 比較値(実数値)`

**説明**

fvで指定された変数に格納されているFV値の各要素を、パラメーターで指定された値(X,Y,Z)が最大値になるように切り詰めます。
FV値の各要素に対して最大値を適用する場合に使用します。

**関連**: fvseti, fvset, fvadd, fvsub, fvmul, fvdiv, fvmin

---

### fvouter

ベクトル外積

- **グループ**: 拡張画面制御命令

**構文**
```
fvouter fv,x,y,z
```

**パラメータ**
- `fv      = FV値が代入されている変数名`
- `(x,y,z) = 演算するベクトル値(実数値)`

**説明**

fvで指定された変数に格納されているFV値と、小数値(X,Y,Z)で指定するベクトルの外積を求めて代入します。

**関連**: fvseti, fvset, fvinner

---

### fvinner

ベクトル内積

- **グループ**: 拡張画面制御命令

**構文**
```
fvinner fv,x,y,z
```

**パラメータ**
- `fv      = FV値が代入されている変数名`
- `(x,y,z) = 演算するベクトル値(実数値)`

**説明**

fvで指定された変数に格納されているFV値と、小数値(X,Y,Z)で指定するベクトルの内積を求めてfv.0に代入します。

**関連**: fvseti, fvset, fvouter

---

### fvunit

ベクトル正規化

- **グループ**: 拡張画面制御命令

**構文**
```
fvunit fv
```

**パラメータ**
- `fv      = FV値が代入されている変数名`

**説明**

fvで指定された変数に格納されているベクトル(FV値)を正規化します。

**関連**: fvseti, fvset

---

### fsin

サインを求める

- **グループ**: 拡張画面制御命令

**構文**
```
fsin fval,frot
```

**パラメータ**
- `fval    = 実数値が代入される変数名`
- `frot    = 回転角度(ラジアン)`

**説明**

frotで指定された角度のサイン値をfvalで指定した変数に代入します。
角度の単位はラジアン(2π=360度)になります。

**関連**: fcos, fsqr, froti

---

### fcos

コサインを求める

- **グループ**: 拡張画面制御命令

**構文**
```
fcos fval,frot
```

**パラメータ**
- `fval    = 実数値が代入される変数名`
- `frot    = 回転角度(ラジアン)`

**説明**

frotで指定された角度のコサイン値をfvalで指定した変数に代入します。
角度の単位はラジアン(2π=360度)になります。

**関連**: fsin, fsqr, froti

---

### fsqr

平方根を求める

- **グループ**: 拡張画面制御命令

**構文**
```
fsqr fval,fprm
```

**パラメータ**
- `fval    = 実数値が代入される変数名`
- `fprm    = 演算に使われる値(実数)`

**説明**

fprmで指定された値の平方根をfvalで指定した変数に代入します。

**関連**: fsin, fcos, froti

---

### str2fv

文字列をベクトルに変換

- **グループ**: 拡張画面制御命令

**構文**
```
str2fv fv,"x,y,z"
```

**パラメータ**
- `fv      = FV値が代入される変数名`
- `"x,y,z" = 「,」で区切られた実数値が格納された文字列`

**説明**

"x,y,z"で指定された文字列情報を「,」で区切られたX,Y,Z小数値として読み出し、fvで指定された変数に格納します。
それぞれの項目が正しく数値として認識できない(不正な)文字列があった場合には、それ以降の項目も含めて0.0が代入されます。

**関連**: fv2str, str2f, f2str, f2i

---

### fv2str

ベクトルを文字列に変換

- **グループ**: 拡張画面制御命令

**構文**
```
fv2str fv
```

**パラメータ**
- `fv      = FV値が代入されている変数名`

**説明**

fvで指定された変数に格納されているベクトル(FV値)を文字列に変換してシステム変数refstrに結果を返します。

**関連**: str2fv, str2f, f2str, f2i

---

### str2f

文字列を小数値に変換

- **グループ**: 拡張画面制御命令

**構文**
```
str2f fval,"fval"
```

**パラメータ**
- `fval    = 実数値が代入される変数名`
- `"fval"  = 実数値が格納された文字列`

**説明**

"fval"で指定された文字列情報を小数値として読み出し、fvalで指定された変数に格納します。

**関連**: fv2str, str2fv, f2str, f2i

---

### f2str

小数値を文字列に変換

- **グループ**: 拡張画面制御命令

**構文**
```
f2str sval,fval
```

**パラメータ**
- `sval    = 文字列が代入される変数名`
- `fval    = 変換元の実数値`

**説明**

fvalで指定された小数値を文字列に変換して、valで指定された文字列型の変数に結果を返します。

**関連**: fv2str, str2fv, str2f, f2i

---

### delobj

オブジェクトの削除

- **グループ**: 拡張画面制御命令

**構文**
```
delobj ObjID
```

**パラメータ**
- `ObjID`: オブジェクトID

**説明**

指定されたオブジェクトを削除します。

**関連**: regobj

---

### setpos

posグループ情報を設定

- **グループ**: 拡張画面制御命令

**構文**
```
setpos id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 設定する値 (デフォルト=0)

**説明**

オブジェクトの持つパラメーターを設定します。
posグループ(表示座標)に(x,y,z)で指定された値を設定します。
(x,y,z)には、実数または整数値を指定することができます。

**関連**: setang, setangr, setscale, setdir, setefx, setwork

---

### setang

angグループ情報を設定

- **グループ**: 拡張画面制御命令

**構文**
```
setang id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 設定する値 (デフォルト=0)

**説明**

オブジェクトの持つパラメーターを設定します。
angグループ(表示角度)に(x,y,z)で指定された値を設定します。
(x,y,z)には、実数または整数値を指定することができます。
角度の単位はラジアンになります。
(回転する順番はX->Y->Zとなります。他の順番で回転させるための、setangy、setangz命令が用意されています。)
整数で角度を設定するためのsetangr命令も用意されています。

**関連**: setpos, setangr, setscale, setdir, setefx, setwork

---

### setangr

angグループ情報を設定

- **グループ**: 拡張画面制御命令

**構文**
```
setangr id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 設定する値 (デフォルト=0)

**説明**

オブジェクトの持つパラメーターを設定します。
angグループ(表示角度)に(x,y,z)で指定された値を設定します。
(x,y,z)には、実数または整数値を指定することができます。
角度の単位は整数で0～255で一周する値を使用します。
ラジアンで角度を設定するためのsetang命令も用意されています。

**関連**: setpos, setang, setscale, setdir, setefx, setwork

---

### setscale

scaleグループ情報を設定

- **グループ**: 拡張画面制御命令

**構文**
```
setscale id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 設定する値 (デフォルト=0)

**説明**

オブジェクトの持つパラメーターを設定します。
scaleグループ(表示倍率)に(x,y,z)で指定された値を設定します。
(x,y,z)には、実数または整数値を指定することができます。

**関連**: setpos, setang, setangr, setdir, setefx, setwork

---

### setdir

dirグループ情報を設定

- **グループ**: 拡張画面制御命令

**構文**
```
setdir id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 設定する値 (デフォルト=0)

**説明**

オブジェクトの持つパラメーターを設定します。
dirグループ(移動ベクトル)に(x,y,z)で指定された値を設定します。
(x,y,z)には、実数または整数値を指定することができます。
移動ベクトルに登録された値は、オブジェクトの自動移動モード(OBJ_MOVE)時に参照されます。

**関連**: setpos, setang, setangr, setscale, setefx, setwork

---

### setwork

workグループ情報を設定

- **グループ**: 拡張画面制御命令

**構文**
```
setwork id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 設定する値 (デフォルト=0)

**説明**

オブジェクトの持つパラメーターを設定します。
workグループ(ワーク値)に(x,y,z)で指定された値を設定します。
(x,y,z)には、実数または整数値を指定することができます。

**関連**: setpos, setang, setangr, setscale, setdir, setefx, setwork2

---

### addpos

posグループ情報を加算

- **グループ**: 拡張画面制御命令

**構文**
```
addpos id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 加算する値 (デフォルト=0)

**説明**

オブジェクトの持つパラメーターを設定します。
posグループ(表示座標)に(x,y,z)で指定された値を設定します。
(x,y,z)には、実数または整数値を指定することができます。

**関連**: addang, addangr, addscale, adddir, addefx, addwork

---

### addang

angグループ情報を加算

- **グループ**: 拡張画面制御命令

**構文**
```
addang id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 加算する値 (デフォルト=0)

**説明**

オブジェクトの持つパラメーターを設定します。
angグループ(表示角度)に(x,y,z)で指定された値を加算します。
(x,y,z)には、実数または整数値を指定することができます。
角度の単位はラジアンになります。
整数で角度を設定するためのsetangr命令も用意されています。

**関連**: addpos, addangr, addscale, adddir, addefx, addwork

---

### addangr

angグループ情報を加算

- **グループ**: 拡張画面制御命令

**構文**
```
addangr id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 加算する値 (デフォルト=0)

**説明**

オブジェクトの持つパラメーターを設定します。
angグループ(表示角度)に(x,y,z)で指定された値を加算します。
(x,y,z)には、実数または整数値を指定することができます。
角度の単位は整数で0～255で一周する値を使用します。
ラジアンで角度を設定するためのsetang命令も用意されています。

**関連**: addpos, addang, addscale, adddir, addefx, addwork

---

### addscale

scaleグループ情報を加算

- **グループ**: 拡張画面制御命令

**構文**
```
addscale id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 加算する値 (デフォルト=0)

**説明**

オブジェクトの持つパラメーターを設定します。
scaleグループ(表示倍率)に(x,y,z)で指定された値を加算します。
(x,y,z)には、実数または整数値を指定することができます。

**関連**: addpos, addang, addangr, adddir, addefx, addwork

---

### adddir

dirグループ情報を加算

- **グループ**: 拡張画面制御命令

**構文**
```
adddir id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 加算する値 (デフォルト=0)

**説明**

オブジェクトの持つパラメーターを設定します。
dirグループ(移動ベクトル)に(x,y,z)で指定された値を加算します。
(x,y,z)には、実数または整数値を指定することができます。

**関連**: addpos, addang, addangr, addscale, addefx, addwork

---

### addwork

workグループ情報を加算

- **グループ**: 拡張画面制御命令

**構文**
```
addwork id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 加算する値 (デフォルト=0)

**説明**

オブジェクトの持つパラメーターを設定します。
workグループ(ワーク値)に(x,y,z)で指定された値を加算します。
(x,y,z)には、実数または整数値を指定することができます。

**関連**: addpos, addang, addangr, addscale, adddir, addefx

---

### getpos

posグループ情報を取得

- **グループ**: 拡張画面制御命令

**構文**
```
getpos id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 取得する変数

**説明**

オブジェクトの持つパラメーターを取得します。
posグループ(表示座標)の内容が(x,y,z)で指定された変数に代入されます。
(x,y,z)は、実数型の変数として設定されます。
命令の最後に「i」を付加することで、整数値として値を取得することができます。

**関連**: getposi, getang, getangr, getscale, getdir, getefx, getwork

---

### getscale

scaleグループ情報を取得

- **グループ**: 拡張画面制御命令

**構文**
```
getscale id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 取得する変数

**説明**

オブジェクトの持つパラメーターを取得します。
scaleグループ(表示倍率)の内容が(x,y,z)で指定された変数に代入されますます。
(x,y,z)は、実数型の変数として設定されます。
命令の最後に「i」を付加することで、整数値として値を取得することができます。

**関連**: getscalei, getpos, getang, getangr, getdir, getefx, getwork

---

### getdir

dirグループ情報を取得

- **グループ**: 拡張画面制御命令

**構文**
```
getdir id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 取得する変数

**説明**

オブジェクトの持つパラメーターを取得します。
dirグループ(移動ベクトル)の内容が(x,y,z)で指定された変数に代入されます。
(x,y,z)は、実数型の変数として設定されます。
命令の最後に「i」を付加することで、整数値として値を取得することができます。

**関連**: getdiri, getpos, getang, getangr, getscale, getefx, getwork

---

### getwork

workグループ情報を取得

- **グループ**: 拡張画面制御命令

**構文**
```
getwork id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 取得する変数

**説明**

オブジェクトの持つパラメーターを取得します。
workグループ(ワーク値)の内容が(x,y,z)で指定された変数に代入されます。
(x,y,z)は、実数型の変数として設定されます。
命令の最後に「i」を付加することで、整数値として値を取得することができます。

**関連**: getworki, getpos, getang, getangr, getscale, getdir, getefx

---

### getposi

posグループ情報を整数で取得

- **グループ**: 拡張画面制御命令

**構文**
```
getposi id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 取得する変数

**説明**

オブジェクトの持つパラメーターを取得します。
posグループ(表示座標)の内容が(x,y,z)で指定された変数に代入されます。
(x,y,z)は、整数型の変数として設定されます。

**関連**: getpos, getangi, getangri, getscalei, getdiri, getefxi, getworki

---

### getscalei

scaleグループ情報を整数で取得

- **グループ**: 拡張画面制御命令

**構文**
```
getscalei id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 取得する変数

**説明**

オブジェクトの持つパラメーターを取得します。
scaleグループ(表示倍率)の内容が(x,y,z)で指定された変数に代入されますます。
(x,y,z)は、整数型の変数として設定されます。

**関連**: getscale, getposi, getangi, getangri, getdiri, getefxi, getworki

---

### getdiri

dirグループ情報を整数で取得

- **グループ**: 拡張画面制御命令

**構文**
```
getdiri id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 取得する変数

**説明**

オブジェクトの持つパラメーターを取得します。
dirグループ(移動ベクトル)の内容が(x,y,z)で指定された変数に代入されます。
(x,y,z)は、整数型の変数として設定されます。

**関連**: getdir, getposi, getangi, getangri, getscalei, getefxi, getworki

---

### getworki

workグループ情報を整数で取得

- **グループ**: 拡張画面制御命令

**構文**
```
getworki id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 取得する変数

**説明**

オブジェクトの持つパラメーターを取得します。
workグループ(ワーク値)の内容が(x,y,z)で指定された変数に代入されます。
(x,y,z)は、整数型の変数として設定されます。

**関連**: getwork, getposi, getangi, getangri, getscalei, getdiri, getefxi

---

### selpos

移動座標をMOC情報に設定

- **グループ**: 拡張画面制御命令

**構文**
```
selpos id
```

**パラメータ**
- `id`: オブジェクトID

**説明**

MOC設定命令の対象となるMOCグループをpos(座標)に設定します
idは、オブジェクトIDとなります。

**関連**: selmoc, selang, selscale, seldir, selefx, selcam, selcpos, selcang, selcint

---

### selang

回転角度をMOC情報に設定

- **グループ**: 拡張画面制御命令

**構文**
```
selang id
```

**パラメータ**
- `id`: オブジェクトID

**説明**

MOC設定命令の対象となるMOCグループをang(回転角度)に設定します
idは、オブジェクトIDとなります。

**関連**: selmoc, selpos, selscale, seldir, selefx, selcam, selcpos, selcang, selcint

---

### selscale

スケールをMOC情報に設定

- **グループ**: 拡張画面制御命令

**構文**
```
selscale id
```

**パラメータ**
- `id`: オブジェクトID

**説明**

MOC設定命令の対象となるMOCグループをscale(スケール)に設定します
idは、オブジェクトIDとなります。

**関連**: selmoc, selpos, selang, selefx, seldir, selcam, selcpos, selcang, selcint

---

### seldir

移動量をMOC情報に設定

- **グループ**: 拡張画面制御命令

**構文**
```
seldir id
```

**パラメータ**
- `id`: オブジェクトID

**説明**

MOC設定命令の対象となるMOCグループをdir(移動量)に設定します
idは、オブジェクトIDとなります。

**関連**: selmoc, selpos, selang, selscale, selefx, selcam, selcpos, selcang, selcint

---

### selwork

オブジェクトワークをMOC情報に設定

- **グループ**: 拡張画面制御命令

**構文**
```
selwork id
```

**パラメータ**
- `id`: オブジェクトID

**説明**

MOC設定命令の対象となるMOCグループをwork(ワーク)に設定します
idは、オブジェクトIDとなります。

**関連**: selmoc, selpos, selang, selscale, selefx, selcam, selcpos, selcang, selcint

---

### objset3

MOC情報を設定

- **グループ**: 拡張画面制御命令

**構文**
```
objset3 x,y,z
```

**パラメータ**
- `x`: 設定する値
- `y`: 設定する値2
- `z`: 設定する値3

**説明**

MOC情報を設定します。
オフセット番号0から3つのパラメータが対象になります。

**関連**: objset3, objadd3, objset3r, objsetf3, objaddf3

---

### objsetf3

MOC情報を設定

- **グループ**: 拡張画面制御命令

**構文**
```
objsetf3 fx,fy,fz
```

**パラメータ**
- `fx`: 設定する値(実数値)
- `fy`: 設定する値2(実数値)
- `fz`: 設定する値3(実数値)

**説明**

MOC情報を設定します。
オフセット番号0から3つのパラメータが対象になります。

**関連**: objset3, objadd3, objset3r, objsetf3, objaddf3

---

### objadd3

MOC情報を加算

- **グループ**: 拡張画面制御命令

**構文**
```
objadd3 x,y,z
```

**パラメータ**
- `x`: 加算する値
- `y`: 加算する値2
- `z`: 加算する値3

**説明**

MOC情報に設定されている値にx,y,zを加算します。
オフセット番号0から3つのパラメータが対象になります。

**関連**: objset3, objadd3r, objset3r, objsetf3, objaddf3

---

### objaddf3

MOC情報を加算

- **グループ**: 拡張画面制御命令

**構文**
```
objaddf3 fx,fy,fz
```

**パラメータ**
- `fx`: 加算する値(実数値)
- `fy`: 加算する値2(実数値)
- `fz`: 加算する値3(実数値)

**説明**

MOC情報に設定されている値にfx,fy,fzを加算します。
オフセット番号0から3つのパラメータが対象になります。

**関連**: objset3, objadd3, objset3r, objsetf3, objaddf3

---

### objadd3r

MOC情報を加算

- **グループ**: 拡張画面制御命令

**構文**
```
objadd3r ofs,fx,fy,fz
```

**パラメータ**
- `ofs`: MOCのオフセット番号
- `fx`: 加算する値(整数角度値)
- `fy`: 加算する値2(整数角度値)
- `fz`: 加算する値3(整数角度値)

**説明**

MOC情報に設定されている値にfx,fy,fzを加算します。
ただし整数値(256で１回転)をラジアン単位に変換したパラメーターを加算します。
角度を指定するパラメーター以外では正常な値にならないので注意してください。

**関連**: objset3, objadd3, objset3r, objsetf3, objaddf3

---

### objset3r

MOC情報を設定

- **グループ**: 拡張画面制御命令

**構文**
```
objset3r x,y,z
```

**パラメータ**
- `x`: 設定する値
- `y`: 設定する値2
- `z`: 設定する値3

**説明**

MOC情報に角度情報を設定します。
オフセット番号0から3つのパラメータが対象になります。
整数値(256で１回転)をラジアン単位に変換してパラメーターを書き込みます。
角度を指定するパラメーター以外では正常な値にならないので注意してください。

**関連**: objset3, objadd3, objset3r, objsetf3, objaddf3

---

### setobjmode

オブジェクトのモード設定

- **グループ**: 拡張画面制御命令

**構文**
```
setobjmode ObjID,mode,sw
```

**パラメータ**
- `ObjID`: オブジェクトID
- `mode`: モード値
- `sw`: 設定スイッチ

**説明**

指定されたオブジェクトのモードを変更します。
モード値は、regobj命令で指定するものと同様です。
swは、以下のように動作します。
```
	sw = 0 : 指定したモード値を追加
	sw = 1 : 指定したモード値を削除
	sw = 2 : 指定したモード値だけを設定
```

**関連**: regobj, setobjmodel

---

### setcoli

オブジェクトのコリジョン設定

- **グループ**: 拡張画面制御命令

**構文**
```
setcoli id,mygroup,enegroup
```

**パラメータ**
- `id`: オブジェクトID
- `mygroup`: 自分が属するグループ値
- `enegroup`: 衝突を検出する対象となるグループ値

**説明**

オブジェクトに対してコリジョングループ情報を設定します。
コリジョングループ値は、1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768の中から1つだけを選択可能です。

**関連**: getcoli, findobj, nextobj

---

### getcoli

オブジェクトのコリジョン判定

- **グループ**: 拡張画面制御命令

**構文**
```
getcoli val,id,distance
```

**パラメータ**
- `val`: 結果が代入される変数名
- `id`: オブジェクトID
- `distance`: 衝突を検出する範囲(実数値)

**説明**

指定したオブジェクトが持つコリジョン情報をもとに、そのオブジェクトが衝突している別なオブジェクトのIDを調べます。
distanceは、衝突する範囲(半径)を実数値で指定します。
衝突が検出された場合は、変数にオブジェクトIDが代入されます。
何も衝突が検出されなかった場合は、-1が代入されます。
^
HGIMG4では、distanceにマイナス値を指定した場合、3Dモデルが持つ衝突範囲(バウンディングボックス)にdistanceを掛けた値をもとに衝突検出を行ないます。
たとえば、-1.5を指定した場合は、衝突範囲を1.5倍に拡大した状態で、衝突検出が行なわれます。また、より正確な衝突の情報を作成するために、gppcontact命令を使用することが可能です。

**関連**: setcoli, findobj, nextobj, gppcontact

---

### getobjcoli

オブジェクトのグループ取得

- **グループ**: 拡張画面制御命令

**構文**
```
getobjcoli var,id,group
```

**パラメータ**
- `var`: 結果が代入される変数名
- `id(0)`: オブジェクトID
- `group(0)`: グループID

**説明**

指定したオブジェクトが所属するグループ値(コリジョングループなど)を取得し、varで指定された変数に代入します。
グループ値は、以下のものになります。
```
グループID   内容
---------------------------------------
  0          コリジョングループ(setcoliで設定)
  1          衝突対象グループ(setcoliで設定)
  2          レンダリンググループ(setobjrenderで設定)
  3          ライティンググループ(setobjrenderで設定)
```

**関連**: setcoli, getcoli, setobjrender

---

### setobjrender

オブジェクトのレンダリンググループ設定

- **グループ**: 拡張画面制御命令

**構文**
```
setobjrender id,rendergroup,lightgroup
```

**パラメータ**
- `id(0)`: オブジェクトID
- `rendergroup(1)`: レンダリンググループ値
- `lightgroup(1)`: ライティンググループ値

**説明**

オブジェクトに対してレンダリンググループ、ライティンググループ情報を設定します。
レンダリンググループ値は、カメラからレンダリングした際に表示のON/OFFを設定するための値です。カメラが持つレンダリンググループ値と同一である場合は、表示が有効となります。
通常は、オブジェクト、カメラともにグループ1が設定されています。特定のカメラからの表示のみ表示を無効にしたい場合などに利用できます。
ライティンググループ値は、特定のライトに対して有効/無効を切り替えるものです。ライトが持つライティンググループ値と異なる場合は、ライトが無効となります。

それぞれのグループ値は、1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768の中から任意のビットを組み合わせて指定可能です。

**関連**: setcoli, getobjcoli

---

### findobj

オブジェクト検索

- **グループ**: 拡張画面制御命令

**構文**
```
findobj exmode,group
```

**パラメータ**
- `exmode(0)`: 検索を除外するモード
- `group(0)`: 検索対象コリジョングループ値

**説明**

有効なオブジェクトを列挙します。
コリジョングループ値を指定した場合は、特定のコリジョングループに属するオブジェクトだけを検索します。
コリジョングループ値が0の場合は、すべてのオブジェクトが検索対象となります。
最初にfindobjを実行して、次にnextobj命令で該当するオブジェクトを検索することができます。
また、exmodeで指定したモード(regobjで指定するモード値と同じ)は検索から除外されます。

**関連**: setcoli, nextobj

---

### nextobj

次のオブジェクト検索

- **グループ**: 拡張画面制御命令

**構文**
```
nextobj val
```

**パラメータ**
- `val`: 結果が代入される変数名

**説明**

findobj命令で指定された条件をもとにオブジェクトを検索します。
検索されると、変数にオブジェクトIDが代入されます。
検索対象がなくなった時には-1が代入されます。

**関連**: setcoli, findobj

---

### setborder

オブジェクト有効範囲設定

- **グループ**: 拡張画面制御命令

**構文**
```
setborder fx,fy,fz,option
```

**パラメータ**
- `( fx,fy,fz )`: ボーダー領域の設定値(実数値)
- `option(0)`: 設定オプション(0～2)

**説明**

ボーダー領域(オブジェクト有効範囲)を設定します。
optionパラメーターにより、( fx,fy,fz )に設定する内容が変わります。
optionパラメーターを省略するか、または0の場合は、
( 0,0,0 )を中心にした、( fx,fy,fz )サイズの立方体がボーダー領域となります。
optionパラメーターが1の場合は、( fx,fy,fz )の座標を数値が小さい側のボーダー領域として設定します。
optionパラメーターが2の場合は、( fx,fy,fz )の座標を数値が大きい側のボーダー領域として設定します。

**関連**: regobj, setobjmode

---

### selmoc

MOC情報を設定

- **グループ**: 拡張画面制御命令

**構文**
```
selmoc id, mocofs
```

**パラメータ**
- `id`: オブジェクトID
- `mocofs`: MOCのグループ指定

**説明**

MOC設定命令の対象となるMOCグループを指定します。
idは、オブジェクトIDとなります。
通常は、selpos,selang,selscale,seldir命令をお使いください。

**関連**: selpos, selang, selscale, seldir, selcam, selcpos, selcang, selcint

---

### objgetfv

MOC情報を取得

- **グループ**: 拡張画面制御命令

**構文**
```
objgetfv fv
```

**パラメータ**
- `fv      = FV値が代入される変数名`

**説明**

MOCに設定されている値を変数fvに代入します。

**関連**: objsetfv, fvset, fvadd, fvsub, fvmul, fvdiv

---

### objsetfv

MOC情報を設定

- **グループ**: 拡張画面制御命令

**構文**
```
objsetfv fv
```

**パラメータ**
- `fv      = FV値が代入されている変数名`

**説明**

変数fvの内容をMOCに設定します。

**関連**: objgetfv, fvset, fvadd, fvsub, fvmul, fvdiv

---

### objaddfv

MOC情報を加算

- **グループ**: 拡張画面制御命令

**構文**
```
objaddfv fv
```

**パラメータ**
- `fv      = FV値が代入されている変数名`

**説明**

変数fvの内容をMOCに加算します。

**関連**: objgetfv, fvset, fvadd, fvsub, fvmul, fvdiv

---

### objexist

オブジェクトIDが有効か調べる

- **グループ**: 拡張画面制御命令

**構文**
```
objexist p1
```

**パラメータ**
- `p1(0)`: オブジェクトID

**説明**

p1で指定されたオブジェクトIDが有効であるか調べます。
オブジェクトIDが有効(登録済み)の場合は、システム変数statに0が代入されます。
オブジェクトIDが無効(未登録)の場合は、システム変数statに-1が代入されます。

**関連**: regobj, delobj

---

### event_wait

待ち時間イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_wait id,p1
```

**パラメータ**
- `id`: イベントID
- `p1(0)`: 待ち時間(フレーム)

**説明**

idで指定しているイベントIDに、待ち時間イベントを追加します。
待ち時間イベントは、p1で指定されたフレーム数だけ次のイベントに進むことを保留します。

**関連**: newevent, setevent

---

### event_jump

ジャンプイベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_jump id,p1,p2
```

**パラメータ**
- `id`: イベントID
- `p1(0)`: ジャンプ先のイベント番号
- `p2(0)`: ジャンプ無視の確率(%)

**説明**

idで指定しているイベントIDに、ジャンプイベントを追加します。
ジャンプイベントは、指定されたイベント番号から実行を続けることを指示します。
イベントリストの中でのgoto命令にあたります。
p1で指定するイベント番号は、イベントに追加された順番に0,1,2…と数えたものになります。
p2で、ジャンプ無視の確率(%)を設定することができます。
0または省略された場合は、必ず(無条件)でジャンプを行ないます。
それ以外の場合は、乱数をもとに1～100%の確率でジャンプを行ない、
ジャンプしなかった場合は次のイベントに進みます。

**関連**: newevent, setevent

---

### event_prmset

パラメーター設定イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_prmset id,p1,p2
```

**パラメータ**
- `id`: イベントID
- `p1(0)`: パラメーターID(PRMSET_*)
- `p2(0)`: 設定される値

**説明**

idで指定しているイベントIDに、パラメーター設定イベントを追加します。
パラメーター設定イベントは、p1で指定されたパラメーターIDにp2の値を設定します。
(それまでに設定されていた内容は消去されます)
パラメーターIDには、以下の名前を使用することができます。
```
パラメーターID   内容
---------------------------------------
PRMSET_MODE      動作モード
PRMSET_FLAG      存在フラグ
PRMSET_SHADE     シェーディングモード
PRMSET_TIMER     タイマー
PRMSET_MYGROUP   コリジョングループ値
PRMSET_COLGROUP  対象グループ値
```

**関連**: event_prmon, event_prmoff, newevent, setevent

---

### event_prmon

パラメータービット設定イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_prmon id,p1,p2
```

**パラメータ**
- `id`: イベントID
- `p1(0)`: パラメーターID(PRMSET_*)
- `p2(0)`: 設定されるビット

**説明**

idで指定しているイベントIDに、パラメータービット設定イベントを追加します。
パラメータービット設定イベントは、p1で指定されたパラメーターIDにp2のビットを設定します。
(それまでに設定されていた内容は保持されたまま、新しい値のビットだけが有効になります)
パラメーターIDの詳細については、event_prmset命令を参照してください。

**関連**: event_prmset, event_prmoff, newevent, setevent

---

### event_prmoff

パラメータービット消去イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_prmoff id,p1,p2
```

**パラメータ**
- `id`: イベントID
- `p1(0)`: パラメーターID(PRMSET_*)
- `p2(0)`: 消去されるビット

**説明**

idで指定しているイベントIDに、パラメータービット消去イベントを追加します。
パラメータービット消去イベントは、p1で指定されたパラメーターIDから、
p2のビットだけを消去します。
パラメーターIDの詳細については、event_prmset命令を参照してください。

**関連**: event_prmset, event_prmon, newevent, setevent

---

### event_setpos

posグループ設定イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_setpos id,x1,y1,z1,x2,y2,z2
```

**パラメータ**
- `id`: イベントID
- `(x1,y1,z1)`: 設定される値(下限値)
- `(x2,y2,z2)`: 設定される値(上限値)

**説明**

idで指定しているイベントIDに、グループ設定イベントを追加します。
グループ設定イベントは、オブジェクトが持っているパラメーターを設定します。
(x1,y1,z1)と(x2,y2,z2)を指定すると、それぞれの範囲内にある値を乱数で作成します。
(x2,y2,z2)を省略して、(x1,y1,z1)だけを指定した場合はそのまま値が設定されます。

**関連**: event_setang, event_setangr, event_setscale, event_setdir, event_setefx, event_setwork, newevent, setevent

---

### event_setang

angグループ設定イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_setang id,x1,y1,z1,x2,y2,z2
```

**パラメータ**
- `id`: イベントID
- `(x1,y1,z1)`: 設定される値(下限値)
- `(x2,y2,z2)`: 設定される値(上限値)

**説明**

idで指定しているイベントIDに、グループ設定イベントを追加します。
グループ設定イベントは、オブジェクトが持っているパラメーターを設定します。
(x1,y1,z1)と(x2,y2,z2)を指定すると、それぞれの範囲内にある値を乱数で作成します。
(x2,y2,z2)を省略して、(x1,y1,z1)だけを指定した場合はそのまま値が設定されます。

**関連**: event_setpos, event_setangr, event_setscale, event_setdir, event_setefx, event_setwork, newevent, setevent

---

### event_setangr

angグループ設定イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_setangr id,x1,y1,z1,x2,y2,z2
```

**パラメータ**
- `id`: イベントID
- `(x1,y1,z1)`: 設定される値(下限値)
- `(x2,y2,z2)`: 設定される値(上限値)

**説明**

idで指定しているイベントIDに、グループ設定イベントを追加します。
グループ設定イベントは、オブジェクトが持っているパラメーターを設定します。
(x1,y1,z1)と(x2,y2,z2)を指定すると、それぞれの範囲内にある値を乱数で作成します。
(x2,y2,z2)を省略して、(x1,y1,z1)だけを指定した場合はそのまま値が設定されます。

**関連**: event_setpos, event_setang, event_setscale, event_setdir, event_setefx, event_setwork, newevent, setevent

---

### event_setscale

scaleグループ設定イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_setscale id,x1,y1,z1,x2,y2,z2
```

**パラメータ**
- `id`: イベントID
- `(x1,y1,z1)`: 設定される値(下限値)
- `(x2,y2,z2)`: 設定される値(上限値)

**説明**

idで指定しているイベントIDに、グループ設定イベントを追加します。
グループ設定イベントは、オブジェクトが持っているパラメーターを設定します。
(x1,y1,z1)と(x2,y2,z2)を指定すると、それぞれの範囲内にある値を乱数で作成します。
(x2,y2,z2)を省略して、(x1,y1,z1)だけを指定した場合はそのまま値が設定されます。

**関連**: event_setpos, event_setang, event_setangr, event_setdir, event_setefx, event_setwork, newevent, setevent

---

### event_setdir

dirグループ設定イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_setdir id,x1,y1,z1,x2,y2,z2
```

**パラメータ**
- `id`: イベントID
- `(x1,y1,z1)`: 設定される値(下限値)
- `(x2,y2,z2)`: 設定される値(上限値)

**説明**

idで指定しているイベントIDに、グループ設定イベントを追加します。
グループ設定イベントは、オブジェクトが持っているパラメーターを設定します。
(x1,y1,z1)と(x2,y2,z2)を指定すると、それぞれの範囲内にある値を乱数で作成します。
(x2,y2,z2)を省略して、(x1,y1,z1)だけを指定した場合はそのまま値が設定されます。

**関連**: event_setpos, event_setang, event_setangr, event_setscale, event_setefx, event_setwork, newevent, setevent

---

### event_setwork

workグループ設定イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_setwork id,x1,y1,z1,x2,y2,z2
```

**パラメータ**
- `id`: イベントID
- `(x1,y1,z1)`: 設定される値(下限値)
- `(x2,y2,z2)`: 設定される値(上限値)

**説明**

idで指定しているイベントIDに、グループ設定イベントを追加します。
グループ設定イベントは、オブジェクトが持っているパラメーターを設定します。
(x1,y1,z1)と(x2,y2,z2)を指定すると、それぞれの範囲内にある値を乱数で作成します。
(x2,y2,z2)を省略して、(x1,y1,z1)だけを指定した場合はそのまま値が設定されます。

**関連**: event_setpos, event_setang, event_setangr, event_setscale, event_setdir, event_setefx, newevent, setevent

---

### event_pos

posグループ変化イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_pos id,frame,x1,y1,z1,sw
```

**パラメータ**
- `id`: イベントID
- `frame`: 変化までのフレーム数
- `(x1,y1,z1)`: 設定される値
- `sw(1)`: 補間オプション

**説明**

idで指定しているイベントIDに、グループ変化イベントを追加します。
グループ変化イベントは、オブジェクトが持っているパラメーターの時間による変化を設定します。
frameで指定したフレーム数が経過した時に(x1,y1,z1)の値になります。
swの補間オプションは、以下の値を指定することができます。
```
	sw = 0 : リニア補間(絶対値)
	sw = 1 : スプライン補間(絶対値)
	sw = 2 : リニア補間(相対値)
	sw = 3 : スプライン補間(相対値)
```
swを省略した場合には、絶対値スプラインが設定されます。
swの値に16を加算した場合は、(x1,y1,z1)で設定される値の替わりにオブジェクトが持つworkグループの値を使用して変化を設定します。

**関連**: event_ang, event_angr, event_scale, event_dir, event_efx, event_work, newevent, setevent

---

### event_ang

angグループ変化イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_ang id,frame,x1,y1,z1,sw
```

**パラメータ**
- `id`: イベントID
- `frame`: 変化までのフレーム数
- `(x1,y1,z1)`: 設定される値
- `sw(0)`: 補間オプション

**説明**

idで指定しているイベントIDに、グループ変化イベントを追加します。
グループ変化イベントは、オブジェクトが持っているパラメーターの時間による変化を設定します。
frameで指定したフレーム数が経過した時に(x1,y1,z1)の値になります。
swの補間オプションは、以下の値を指定することができます。
```
	sw = 0 : リニア補間(絶対値)
	sw = 1 : スプライン補間(絶対値)
	sw = 2 : リニア補間(相対値)
	sw = 3 : スプライン補間(相対値)
```
swを省略した場合には、絶対値リニアが設定されます。
swの値に16を加算した場合は、(x1,y1,z1)で設定される値の替わりにオブジェクトが持つworkグループの値を使用して変化を設定します。
(角度の指定は、setang命令と同様で、回転する順番はX->Y->Zとなります。他の順番で回転させるための、event_angy、event_angz命令が用意されています。)

**関連**: event_pos, event_angr, event_scale, event_dir, event_efx, event_work, newevent, setevent

---

### event_angr

angグループ変化イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_angr id,frame,x1,y1,z1
```

**パラメータ**
- `id`: イベントID
- `frame`: 変化までのフレーム数
- `(x1,y1,z1)`: 設定される値

**説明**

idで指定しているイベントIDに、グループ変化イベントを追加します。
グループ変化イベントは、オブジェクトが持っているパラメーターの時間による変化を設定します。
frameで指定したフレーム数が経過した時に(x1,y1,z1)の値になります。
swの補間オプションは、以下の値を指定することができます。
```
	sw = 0 : リニア補間(絶対値)
	sw = 1 : スプライン補間(絶対値)
	sw = 2 : リニア補間(相対値)
	sw = 3 : スプライン補間(相対値)
```
swを省略した場合には、絶対値リニアが設定されます。
swの値に16を加算した場合は、(x1,y1,z1)で設定される値の替わりにオブジェクトが持つworkグループの値を使用して変化を設定します。

**関連**: event_pos, event_ang, event_scale, event_dir, event_efx, event_work, newevent, setevent

---

### event_scale

scaleグループ変化イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_scale id,frame,x1,y1,z1,sw
```

**パラメータ**
- `id`: イベントID
- `frame`: 変化までのフレーム数
- `(x1,y1,z1)`: 設定される値
- `sw(0)`: 補間オプション

**説明**

idで指定しているイベントIDに、グループ変化イベントを追加します。
グループ変化イベントは、オブジェクトが持っているパラメーターの時間による変化を設定します。
frameで指定したフレーム数が経過した時に(x1,y1,z1)の値になります。
swの補間オプションは、以下の値を指定することができます。
```
	sw = 0 : リニア補間(絶対値)
	sw = 1 : スプライン補間(絶対値)
	sw = 2 : リニア補間(相対値)
	sw = 3 : スプライン補間(相対値)
```
swを省略した場合には、絶対値リニアが設定されます。
swの値に16を加算した場合は、(x1,y1,z1)で設定される値の替わりにオブジェクトが持つworkグループの値を使用して変化を設定します。

**関連**: event_pos, event_ang, event_angr, event_dir, event_efx, event_work, newevent, setevent

---

### event_dir

dirグループ変化イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_dir id,frame,x1,y1,z1,sw
```

**パラメータ**
- `id`: イベントID
- `frame`: 変化までのフレーム数
- `(x1,y1,z1)`: 設定される値
- `sw(0)`: 補間オプション

**説明**

idで指定しているイベントIDに、グループ変化イベントを追加します。
グループ変化イベントは、オブジェクトが持っているパラメーターの時間による変化を設定します。
frameで指定したフレーム数が経過した時に(x1,y1,z1)の値になります。
swの補間オプションは、以下の値を指定することができます。
```
	sw = 0 : リニア補間(絶対値)
	sw = 1 : スプライン補間(絶対値)
	sw = 2 : リニア補間(相対値)
	sw = 3 : スプライン補間(相対値)
```
swを省略した場合には、絶対値リニアが設定されます。
swの値に16を加算した場合は、(x1,y1,z1)で設定される値の替わりにオブジェクトが持つworkグループの値を使用して変化を設定します。

**関連**: event_pos, event_ang, event_angr, event_scale, event_efx, event_work, newevent, setevent

---

### event_work

workグループ変化イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_work id,frame,x1,y1,z1,sw
```

**パラメータ**
- `id`: イベントID
- `frame`: 変化までのフレーム数
- `(x1,y1,z1)`: 設定される値
- `sw(0)`: 補間オプション

**説明**

idで指定しているイベントIDに、グループ変化イベントを追加します。
グループ変化イベントは、オブジェクトが持っているパラメーターの時間による変化を設定します。
frameで指定したフレーム数が経過した時に(x1,y1,z1)の値になります。
swの補間オプションは、以下の値を指定することができます。
```
	sw = 0 : リニア補間(絶対値)
	sw = 1 : スプライン補間(絶対値)
	sw = 2 : リニア補間(相対値)
	sw = 3 : スプライン補間(相対値)
```
swを省略した場合には、絶対値リニアが設定されます。

**関連**: event_pos, event_ang, event_angr, event_scale, event_dir, event_efx, newevent, setevent

---

### event_addpos

posグループ加算イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_addpos id,x,y,z
```

**パラメータ**
- `id`: イベントID
- `(x,y,z)`: 加算される値

**説明**

idで指定しているイベントIDに、グループ加算イベントを追加します。
グループ加算イベントは、オブジェクトが持っているパラメーターに(x,y,z)の値を加算します。

**関連**: event_addang, event_addangr, event_addscale, event_adddir, event_addefx, event_addwork, newevent, setevent

---

### event_addang

angグループ加算イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_addang id,x,y,z
```

**パラメータ**
- `id`: イベントID
- `(x,y,z)`: 加算される値

**説明**

idで指定しているイベントIDに、グループ加算イベントを追加します。
グループ加算イベントは、オブジェクトが持っているパラメーターに(x,y,z)の値を加算します。

**関連**: event_addpos, event_addangr, event_addscale, event_adddir, event_addefx, event_addwork, newevent, setevent

---

### event_addangr

angグループ加算イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_addangr id,x,y,z
```

**パラメータ**
- `id`: イベントID
- `(x,y,z)`: 加算される値

**説明**

idで指定しているイベントIDに、グループ加算イベントを追加します。
グループ加算イベントは、オブジェクトが持っているパラメーターに(x,y,z)の値を加算します。

**関連**: event_addpos, event_addang, event_addscale, event_adddir, event_addefx, event_addwork, newevent, setevent

---

### event_addscale

scaleグループ加算イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_addscale id,x,y,z
```

**パラメータ**
- `id`: イベントID
- `(x,y,z)`: 加算される値

**説明**

idで指定しているイベントIDに、グループ加算イベントを追加します。
グループ加算イベントは、オブジェクトが持っているパラメーターに(x,y,z)の値を加算します。

**関連**: event_addpos, event_addang, event_addangr, event_adddir, event_addefx, event_addwork, newevent, setevent

---

### event_adddir

dirグループ加算イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_adddir id,x,y,z
```

**パラメータ**
- `id`: イベントID
- `(x,y,z)`: 加算される値

**説明**

idで指定しているイベントIDに、グループ加算イベントを追加します。
グループ加算イベントは、オブジェクトが持っているパラメーターに(x,y,z)の値を加算します。

**関連**: event_addpos, event_addang, event_addangr, event_addscale, event_addefx, event_addwork, newevent, setevent

---

### event_addwork

workグループ加算イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_addwork id,x,y,z
```

**パラメータ**
- `id`: イベントID
- `(x,y,z)`: 加算される値

**説明**

idで指定しているイベントIDに、グループ加算イベントを追加します。
グループ加算イベントは、オブジェクトが持っているパラメーターに(x,y,z)の値を加算します。

**関連**: event_addpos, event_addang, event_addangr, event_addscale, event_adddir, event_addefx, newevent, setevent

---

### setevent

オブジェクトにイベントを設定

- **グループ**: 拡張画面制御命令

**構文**
```
setevent p1,p2,p3
```

**パラメータ**
- `p1(0)`: オブジェクトID
- `p2(0)`: イベントID
- `p3(-1)`: イベントスロットID

**説明**

p1で指定したオブジェクトにp2のイベントを適用します。
あらかじめ、決まった流れの処理(イベント)を登録したイベントリストを用意しておく必要があります。
^
setevent命令によって設定されるイベントは、オブジェクト１つあたり４つまで同時に適用することが可能です。
p3にイベントを設定するためのイベントスロットID(0から3まで)を指定することができます。
p3を省略するか、-1を指定した場合には0から順番に空いているイベントスロットIDが使用されます。
オブジェクトに設定されたイベントを削除する場合には、p3にイベントスロットIDを指定して、p2をマイナス値にしてください。
^
イベントの設定に成功した場合には、システム変数statに設定されたイベントスロットIDが代入されます。
イベントの設定に失敗すると、システム変数statに-1が代入されます。

**関連**: newevent

---

### delevent

イベントリストを削除

- **グループ**: 拡張画面制御命令

**構文**
```
delevent p1
```

**パラメータ**
- `p1`: イベントID

**説明**

p1で指定したイベントリストを削除します。

**関連**: newevent

---

### newevent

イベントリストを作成

- **グループ**: 拡張画面制御命令

**構文**
```
newevent p1
```

**パラメータ**
- `p1`: イベントIDが代入される変数名

**説明**

新しいイベントIDを取得し、p1で指定した変数に代入します。
^
新しくイベントを作成する場合には、必ずnewevent命令でイベントIDを取得しておく必要があります。
次に、「event_」で始まるイベントリスト追加命令によって多彩な動作を登録しておくことができます。
一度取得されたイベントIDは、シーンのリセット(hgreset命令)が行なわれるか、
またはdelevent命令によってイベントリストが削除されるまでは保持されます。
^
こうしてできたイベントは、setevent命令によっていつでもオブジェクトに対して適用することができます。

**関連**: delevent, setevent

---

### getang

angグループ情報を取得

- **グループ**: 拡張画面制御命令

**構文**
```
getang id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 取得する変数

**説明**

オブジェクトの持つパラメーターを取得します。
angグループ(表示角度)の内容が(x,y,z)で指定された変数に代入されます。
(x,y,z)は、実数型の変数として設定されます。
命令の最後に「i」を付加することで、整数値として値を取得することができます。

**関連**: getangi, getpos, getangr, getscale, getdir, getefx, getwork

---

### getangr

angグループ情報を取得

- **グループ**: 拡張画面制御命令

**構文**
```
getangr id,x,y,z
```

**パラメータ**
- `id`: オブジェクトID
- `(x,y,z)`: 取得する変数

**説明**

オブジェクトの持つパラメーターを取得します。
angグループ(表示角度)の内容が(x,y,z)で指定された変数に代入されます。
(x,y,z)は、整数型の変数として設定されます。
角度の単位は整数で0～255で一周する値を使用します。

**関連**: getpos, getang, getscale, getdir, getefx, getwork

---

### event_delobj

オブジェクト削除イベントを追加

- **グループ**: 拡張画面制御命令

**構文**
```
event_delobj id
```

**パラメータ**
- `id`: イベントID

**説明**

idで指定しているイベントIDに、オブジェクト削除イベントを追加します。
オブジェクト削除イベントは、現在イベントを実行しているオブジェクトそのものを削除する命令です。

**関連**: event_regobj, newevent, setevent

---
