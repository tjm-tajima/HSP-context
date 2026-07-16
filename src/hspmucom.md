# hspmucom

- **種別**: 拡張命令
- **グループ**: 拡張サウンド出力制御命令
- **バージョン**: 3.6
- **更新日**: 2020/01/14
- **作者**: onitama
- **URL**: http://hsp.tv/
- **対応環境**: Win
- **備考**: hspmucom.asをインクルードすること。

## 命令一覧

| 命令 | 概要 |
|---|---|
| [mucominit](#mucominit) | MUCOM88初期化 |
| [mucombye](#mucombye) | MUCOM88を解放 |
| [mucomreset](#mucomreset) | MUCOM88をリセット |
| [mucomplay](#mucomplay) | 音楽の再生 |
| [mucomstop](#mucomstop) | 再生の停止 |
| [mucomfade](#mucomfade) | フェードアウト再生 |
| [mucomload](#mucomload) | 音楽データ読み込み |
| [mucomloadpcm](#mucomloadpcm) | PCMデータ読み込み |
| [mucomloadvoice](#mucomloadvoice) | FM音色データ読み込み |
| [mucomtag](#mucomtag) | タグデータの取得 |
| [mucomcomp](#mucomcomp) | MMLのコンパイル |
| [mucommml](#mucommml) | MMLのコンパイル |
| [mucomloadtag](#mucomloadtag) | タグデータの読み込み |
| [mucomres](#mucomres) | MUCOM88実行結果を取得 |
| [mucomstat](#mucomstat) | MUCOM88のステータス取得 |
| [mucomsetvolume](#mucomsetvolume) | MUCOM88ボリューム設定 |
| [mucomgetchdata](#mucomgetchdata) | 演奏情報の取得 |

## 命令詳細

### mucominit

MUCOM88初期化

**構文**
```
mucominit p1, option
```

**パラメータ**
- `p1(0)`: ウインドウハンドル
- `option(0)`: 初期化オプション

**説明**

MUCOM88の初期化を行います。
MUCOM88の各種機能を使用するためには、最初に初期化を行っておく必要があります。
p1パラメーターは、サウンドドライバーが使用するウインドウのハンドルを指定します。
p1を省略または0を指定した場合は、現在アクティブなウインドウが対象となります。
通常は、hwnd(HSPのウインドウハンドル)を指定してください。
optionパラメーターは、以下の値を指定することができます。
```
   値   : 内容
 ---------------------------------------------------------------
    +1  : FM音源のシミュレート(fmgen)を無効にする
    +2  : SCCIを有効にする(scci.dllが必要です)
```
SCCIを有効にした場合は、scci.dllを経由した外部機器上でのFM音源コントロールが可能です。
詳しくは、MUCOM88のマニュアルを参照してください。
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucombye

---

### mucombye

MUCOM88を解放

**構文**
```
mucombye
```

**パラメータ**
- なし

**説明**

MUCOM88の解放処理を行います。
MUCOM88が持つすべてのリソースや割り込みを終了します。
MUCOM88の使用を終了する時に呼び出してください。
onexit命令により、アプリケーション終了時に必ず呼び出す必要があるので注意してください。

**関連**: mucombye

---

### mucomreset

MUCOM88をリセット

**構文**
```
mucomreset option
```

**パラメータ**
- `option(0)`: リセットオプション

**説明**

MUCOM88をリセットします。
演奏中の音楽や音色のデータも含めてすべてリセットされます。
音楽の再生やMMLのコンパイル時には、最初にリセットを行う必要があります。
optionパラメーターは、以下の値を指定することができます。
```
   ラベル                 : 内容
 ---------------------------------------------------------------
   MUCOM_RESET_PLAYER       音楽プレイヤーとしてMUCOM88をリセット
   MUCOM_RESET_COMPILE      MMLコンパイラとしてMUCOM88をリセット
   MUCOM_RESET_EXTFILE      MMLコンパイラ初期化時に内部ファイルを参照しない
```
リセット時には、必ず音楽プレイヤー(MUCOM_RESET_PLAYER)か、MMLコンパイラ(MUCOM_RESET_COMPILE)のどちらかを選択する必要があります。(MMLコンパイル後に音楽を再生する場合は、MMLコンパイラとしてリセットした後、音楽プレイヤーとして再度リセットする必要があります。)
MUCOM_RESET_EXTFILEは、MUCOM88が使用するPC-8801用ドライバファイル(muc88,msub等)を外部ファイルとして読み込むためのオプションです。通常は、指定する必要はありません。
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomload, mucomcomp

---

### mucomplay

音楽の再生

**構文**
```
mucomplay p1
```

**パラメータ**
- `p1(0)`: バンクNo.

**説明**

指定されたバンクNo.の音楽を再生します。
最初に、mucomload命令によりMUCOM88音楽データ(.mub)を読み込んでおく必要があります。
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomload, mucomstop

---

### mucomstop

再生の停止

**構文**
```
mucomstop p1
```

**パラメータ**
- `p1(0)`: 停止オプション

**説明**

mucomplay命令により再生された音楽を停止します。
通常は、p1の停止オプションは0か省略して構いません。
p1に$1000を指定した場合は、ドライバを含めた強制的な停止処理を行います。
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomplay, mucomfade

---

### mucomfade

フェードアウト再生

**構文**
```
mucomfade p1
```

**パラメータ**
- `p1(0)`: フェード速度

**説明**

mucomplay命令により再生された音楽をフェードアウトします。
※この命令は現在正しく使用できないためサポート外となります
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomplay

---

### mucomload

音楽データ読み込み

**構文**
```
mucomload "filename",p1
```

**パラメータ**
- `"filename"`: MUCOM88音楽データファイル(.mub)
- `p1(0)`: バンクNo.

**説明**

MUCOM88音楽データ(.mub)を読み込みます。
p1で読み込む先のバンクNo.(0～15)を指定することで、"filename"のファイルを読み込み再生の準備を行います。
MUCOM88音楽データ(.mub)は、あらかじめ音楽ツール(MUCOM88Win)で作成するか、MMLファイル(.muc)をコンパイルして生成する必要があります。
mucomload命令を使用する際には、最初に、mucomreset命令により音楽プレイヤーとしてMUCOM88をリセットしておく必要があります。
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomreset, mucomplay

---

### mucomloadpcm

PCMデータ読み込み

**構文**
```
mucomloadpcm "filename"
```

**パラメータ**
- `"filename"`: MUCOM88PCMデータファイル(.bin)

**説明**

デフォルトで使用されるMUCOM88PCMデータファイル(.bin)を読み込みます。
PCMデータファイルは、MMLコンパイル時にPCMを無指定だった際に参照されます。
特に指定する必要のない場合は、「mucomloadpcm ""」(無指定)を記述しておいてください。
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomcomp

---

### mucomloadvoice

FM音色データ読み込み

**構文**
```
mucomloadvoice "filename"
```

**パラメータ**
- `"filename"`: MUCOM88FM音色データファイル(.dat)

**説明**

デフォルトで使用されるMUCOM88FM音色データファイル(.dat)を読み込みます。
FM音色データファイルは、MMLコンパイル時に音色ファイルが無指定だった際に参照されます。
通常はMMLから自動的に参照されるため、記述する必要はありません。
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomcomp

---

### mucomtag

タグデータの取得

**構文**
```
mucomtag var,"tagname"
```

**パラメータ**
- `var`: 取得されたデータが代入される変数
- `"tagname"`: タグ文字列

**説明**

mucomload命令により読み込まれたMUCOM88音楽データの中で定義されているタグを取得します。
"tagname"によりタグ文字列を指定することで、そのタグ文字列に対応した定義内容が変数に代入されます。
「mucomtag a,"title"」と記述した場合は、変数aに"title"タグの内容が代入されます。
タグ文字列を空文字("")に指定した場合は、すべての定義テーブルを変数に代入します。
エラーが発生した場合は、変数には空文字("")が代入され、システム変数statに0以外が代入されます。

**関連**: mucomload

---

### mucomcomp

MMLのコンパイル

**構文**
```
mucomcomp "mmlfile","outfile",option
```

**パラメータ**
- `"mmlfile"`: 読み込まれるMUCOM88 MMLファイル(.muc)
- `"outfile"`: 出力されるMUCOM88音楽データファイル(.mub)
- `option(0)`: コンパイルオプション

**説明**

MUCOM88の形式で記述されたMMLファイル(.muc)をコンパイルして、MUCOM88音楽データファイル(.mub)を出力します。
optionパラメーターは、以下の値を指定することができます。
```
   値   : 内容
 ---------------------------------------------------------------
    0   : 通常のMUCOM88コンパイルを行う
    +1  : #voiceタグを無視する
```
mucomcomp命令を使用する際には、最初に、mucomreset命令によりMMLコンパイラとしてMUCOM88をリセットしておく必要があります。
コンパイル結果のメッセージをmucomres命令により取得することができます。
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomres, mucommml

---

### mucommml

MMLのコンパイル

**構文**
```
mucommml var,option
```

**パラメータ**
- `var`: MMLが格納された変数
- `option(0)`: コンパイルオプション

**説明**

MUCOM88の形式で記述されたMMLの文字列を直接コンパイルします。
コンパイルした結果は、音楽バッファ0に格納され、ファイルを介さずにコンパイルから演奏を行うことが可能です。
optionパラメーターは、mucomcomp命令と同様のものが使用できます。
mucommml命令を使用する際には、最初に、mucomreset命令によりMMLコンパイラとしてMUCOM88をリセットしておく必要があります。
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomres, mucomcomp

---

### mucomloadtag

タグデータの読み込み

**構文**
```
mucomloadtag var,"mmlfile"
```

**パラメータ**
- `var`: 取得されたデータが代入される変数
- `"mmlfile"`: 読み込まれるMUCOM88 MMLファイル(.muc)

**説明**

MUCOM88の形式で記述されたMMLファイル(.muc)から、定義されたタグ情報のみを取り出して変数に代入します。
コンパイルすることなく、タグ情報だけを取り出したい時に使用することができます。
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomload

---

### mucomres

MUCOM88実行結果を取得

**構文**
```
mucomres var
```

**パラメータ**
- `var`: 取得されたデータが代入される変数

**説明**

mucomcomp命令によるコンパイル結果のメッセージを取得します。
MUCOM88が出力したメッセージバッファの内容をすべて文字列として変数に代入します。
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomcomp

---

### mucomstat

MUCOM88のステータス取得

**構文**
```
mucomstat var,option
```

**パラメータ**
- `var`: 取得されたデータが代入される変数
- `option(0)`: 取得オプション

**説明**

MUCOM88再生時の内部ステータスを取得して変数に代入します。
最初に、mucomreset命令により音楽プレイヤーとしてMUCOM88をリセットしておく必要があります。
取得される内容は、optionパラメーターにより指定されます。
optionパラメーターは、以下の値を指定することができます。取得される数値はすべて整数型となります。
```
   ラベル                 : 内容
 ---------------------------------------------------------------
   MUCOM_STATUS_PLAYING     演奏中フラグ (停止=0/演奏中=1)
   MUCOM_STATUS_INTCOUNT    割り込みカウント(トータル)
   MUCOM_STATUS_PASSTICK    ストリーム再生にかかった負荷(ms)
   MUCOM_STATUS_MAJORVER    メジャーバージョンコード
   MUCOM_STATUS_MINORVER    マイナーバージョンコード
   MUCOM_STATUS_COUNT       割り込みカウント
   MUCOM_STATUS_MAXCOUNT    カウントの最大数(*)
   MUCOM_STATUS_MUBSIZE     音楽データのサイズ(*)
   MUCOM_STATUS_MUBRATE     音楽データのメモリ使用率(%)(*)
   MUCOM_STATUS_BASICSIZE   MMLデータのサイズ(*)
   MUCOM_STATUS_BASICRATE   MMLデータのメモリ使用率(%)(*)

(*) コンパイル後のみ取得可能
```
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomplay, mucomcomp

---

### mucomsetvolume

MUCOM88ボリューム設定

**構文**
```
mucomsetvolume fmvol, ssgvol
```

**パラメータ**
- `fmvol(0)`: FM音源のボリューム設定
- `ssgvol(0)`: PSG音源のボリューム設定

**説明**

MUCOM88でシミュレートされる各音源の音量を+-方向に調整します。標準値は 0です。
約 1/2 dBの単位を整数で指定してください。有効範囲の上限は 20(10dB)となります。
SCCI使用時には、ボリューム設定は反映されません。
エラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomplay

---

### mucomgetchdata

演奏情報の取得

**構文**
```
mucomgetchdata var, ch
```

**パラメータ**
- `var`: 取得されたデータが代入される変数
- `ch(0)`: チャンネルNo.(0～10)

**説明**

MUCOM88プレイヤーの演奏情報をチャンネルごとに取得します。
chパラメーターにチャンネルNo.(0～10)を指定することで、現在の状態をvarで指定した変数に代入します。
変数は配列変数として設定され、それぞれの配列要素にステータスが返ります。
```
   配列要素            : 内容
 ---------------------------------------------------------------
   MUCOM_CHDATA_LENGTH   音長
   MUCOM_CHDATA_VNUM     音色No.(内部インデックス値)
   MUCOM_CHDATA_WADR     演奏中のデータアドレス1
   MUCOM_CHDATA_TADR     演奏中のデータアドレス2
   MUCOM_CHDATA_VOL      ボリューム(内部値)
   MUCOM_CHDATA_ALG      アルゴリズム値
   MUCOM_CHDATA_CH       チャンネルNo.
   MUCOM_CHDATA_DETUNE   デチューン値
   MUCOM_CHDATA_TLLFO    TLLFO値
   MUCOM_CHDATA_REVERB   リバーブパラメーター
   MUCOM_CHDATA_QUANTIZE クオンタイズ値
   MUCOM_CHDATA_LFODELAY LFOパラメーター
   MUCOM_CHDATA_LFOCOUNT LFOパラメーター
   MUCOM_CHDATA_LFODIFF  LFOパラメーター
   MUCOM_CHDATA_LFOPEAK  LFOパラメーター
   MUCOM_CHDATA_FNUM1    設定されているFNUM値1
   MUCOM_CHDATA_FNUM2    設定されているFNUM値2
   MUCOM_CHDATA_FLAG     演奏フラグ1
   MUCOM_CHDATA_CODE     コード値
   MUCOM_CHDATA_FLAG2    演奏フラグ2
   MUCOM_CHDATA_PAN      パン設定値
   MUCOM_CHDATA_KEYON    キーオンフラグ
   MUCOM_CHDATA_VNUMORIG 音色No.
   MUCOM_CHDATA_VOLORIG  ボリューム
```
たとえば、「mucomgetchdata a,0」と記述した場合は、チャンネル0(A)の状態が変数aに代入されます。
その後、「a(MUCOM_CHDATA_VNUMORIG)」で演奏中の音色No.を参照することができます。
最初に、mucomreset命令により音楽プレイヤーとしてMUCOM88をリセットしておく必要があります。
mucomgetchdata命令でエラーが発生した場合は、システム変数statに0以外が代入されます。

**関連**: mucomplay

---
