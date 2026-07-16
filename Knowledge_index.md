# HSP ナレッジ索引

このディレクトリ内の各 `.md` ファイル(HSPヘルプソース `.hs` から変換したもの)を、
「どのようなプログラムを作りたい時に、どのファイルを参照すればよいか」という観点で分類した索引です。

作りたいものに近いカテゴリを探し、リンク先のファイルで命令の詳細(構文・パラメータ・説明・サンプル)を確認してください。
1つのファイルが複数のカテゴリから参照されている場合があります。

---

## 1. 基本構文・制御フロー
条件分岐、繰り返し、サブルーチン、ラベルジャンプなど、プログラムの骨格を作りたい。
- [i_prog.md](src/i_prog.md) — if/else, for/next, repeat/loop, while/wend, gosub/return, switch/case, goto, onkey/onclick/onerror
- [sysval.md](src/sysval.md) — cnt, err, stat など制御フローで参照するシステム変数
<<<<<<< HEAD
- [syntax.md](src/syntax.md) — 使用できる演算子、基本構文など
=======
>>>>>>> a498351 (first commit)

## 2. マクロ・プリプロセッサ / 独自命令定義
独自の命令・関数を定義したい、外部ファイルやDLL関数を取り込みたい、条件コンパイルをしたい。
- [i_prep.md](src/i_prep.md) — #module/#global, #deffunc/#defcfunc, #define/#const, #include/#uselib, #if/#ifdef/#ifndef
- [ex_macro.md](src/ex_macro.md) — _debug, __file__, __line__, __hspver__ などの環境判定マクロ
- [hspdef.md](src/hspdef.md) — 標準定義マクロ(gmode_*, screen_*, font_*, and/or/xor/not, M_PI)

## 3. 変数・配列・メモリ操作
配列の作成、メモリバッファの直接操作、構造体的なモジュール変数を扱いたい。
- [i_mem.md](src/i_mem.md) — dim/sdim/ddim, memcpy/memset, mref, newmod/delmod, poke/peek/wpoke/lpoke
- [hspda.md](src/hspda.md) — vsave/vload(変数の一括保存/復元), getvarid/getvarname(変数ID操作)

## 4. 文字列処理・テキストデータ
文字列の分割・置換・検索・書式変換、複数行テキスト(メモリノート)の操作をしたい。
- [i_string.md](src/i_string.md) — strmid, instr, split, strrep, strf, notesel/noteget/noteadd/notefind
- [i_hsp3util.md](src/i_hsp3util.md) — note2array/array2note(配列⇔複数行文字列), arraysave/arrayload
- [hspinet.md](src/hspinet.md) — urlencode/urldecode, b64encode/b64decode, nkfcnv(文字コード変換)
- [form_decode.md](src/form_decode.md) — フォームエンコードされた文字列のデコード

## 5. 数値計算・数学関数・ベクトル演算
三角関数、対数、乱数、丸め処理、ベクトル演算を行いたい。
- [i_stdfunc.md](src/i_stdfunc.md) — int/double変換, rnd, sqrt, sin/cos/tan, powf, limit
- [hspmath.md](src/hspmath.md) — log2, asin/acos, sinh/cosh, round/floor/ceil, INT_MAX等の定数
- [hgimg_common.md](src/hgimg_common.md) — fvset/fvadd/fvouter/fvinner等のベクトル演算(hgimg3/hgimg4共通で使用可能)

## 6. 画面表示・2Dグラフィック描画
ウィンドウ作成、図形描画、画像の読み込み・コピー、色設定など基本的な2D画面処理をしたい。
- [i_graph.md](src/i_graph.md) — screen, cls, mes/print, color, boxf/circle/line, picload, celload/celput, gcopy/gzoom
- [hspext.md](src/hspext.md) — gfcopy(半透明合成), gfdec/gfinc(色演算コピー)
- [i_hsp3util.md](src/i_hsp3util.md) — gfade(画面フェード)

## 7. GUI部品(ボタン・入力欄・メニュー等)
ボタン、チェックボックス、リストボックス、入力欄、メニューバーを使ったダイアログ的なアプリを作りたい。
- [i_object.md](src/i_object.md) — button, input, chkbox, listbox, combox, mesbox, objprm/objsize/objenable
- [i_hsp3util.md](src/i_hsp3util.md) — statictext, scrollbar, progbar(スタティックテキスト/スクロールバー/プログレスバー)
- [mod_menu.md](src/mod_menu.md) — addmenu/applymenu(メニューバー作成)
- [mod_fontdlg.md](src/mod_fontdlg.md) — fontdlg(フォント選択ダイアログ)
- [mod_picfont.md](src/mod_picfont.md) — picfont/picfprt(画像素材を使ったフォント表示)
- [obj.md](src/obj.md) — getobjsize/resizeobj/objgray(配置済みオブジェクトのサイズ・可否操作)

## 8. キーボード・マウス・ゲームパッド入力
キー入力判定、マウス座標取得、ジョイスティック/ゲームパッド入力を扱いたい。
- [i_stdio.md](src/i_stdio.md) — getkey, mouse, stick
- [mod_joystick.md](src/mod_joystick.md) — joyGetPosEx, jstick(stickでは取得できない軸の入力)

## 9. ファイル・ディレクトリ操作
ファイルの読み書き、コピー、ディレクトリ一覧取得、属性/タイムスタンプ変更、圧縮をしたい。
- [i_file.md](src/i_file.md) — bload/bsave, dirlist, delete/mkdir/chdir, exist
- [hspext.md](src/hspext.md) — fxcopy/fxren/fxinfo/fxaget/fxtset(拡張ファイル操作), dirlist2(拡張ディレクトリ取得), lzcopy(圧縮解凍コピー)
- [zipfile.md](src/zipfile.md) — zipcompress/zipextract(ZIP圧縮・解凍)

## 10. サウンド・動画・マルチメディア再生
効果音・BGMの再生、動画再生(MCI)をしたい。
- [i_mmedia.md](src/i_mmedia.md) — mci, mmplay/mmload/mmstop/mmvol(wav/midi/avi等の汎用メディア再生)
- [hspmucom.md](src/hspmucom.md) — mucominit/mucomplay/mucomload(MUCOM88によるFM音源BGM再生)

## 11. ネットワーク通信
HTTP/FTP通信、JSON操作、ソケット通信をしたい。
- [hspinet.md](src/hspinet.md) — netrequest/netload(HTTP), ftpopen/ftpget(FTP), jsonopen/jsongets(JSON)
- [hspsock.md](src/hspsock.md) — sockopen/sockput/sockget/sockmake(低水準ソケットAPI)

## 12. データベース・CSV
ODBC経由でDBに接続したい、CSVファイルを解析したい。
- [hspdb.md](src/hspdb.md) — dbopen/dbsend/dbgets(ODBC接続)
- [hspda.md](src/hspda.md) — csvstr/csvfind/csvsel(CSV解析)

## 13. レジストリ・クリップボード・外部プロセス・シリアル通信
レジストリの読み書き、クリップボード転送、外部プロセスの実行・パイプ通信、シリアルポート通信をしたい。
- [hspext.md](src/hspext.md) — regkey/getreg/setreg(レジストリ), clipset/clipget(クリップボード), pipeexec/pipeget(パイプ付き実行), comopen/comput/comget(シリアルポート)

## 14. COMオブジェクト操作
Excel等のCOMオートメーションオブジェクトを操作したい。
- [i_com.md](src/i_com.md) — newcom/querycom/comevent/comevarg

## 15. システム変数・実行時状態の参照
マウス座標、ウィンドウID、エラーコード、ループカウンタなど実行時の状態値を知りたい。
- [sysval.md](src/sysval.md) — stat, cnt, err, mousex/mousey, ginfo_*, dir_cur/dir_exe等

## 16. マルチプラットフォーム2Dゲーム・スプライト (HSP3Dish)
スマホ等マルチプラットフォーム向け(HSP3Dish)にスプライトキャラクタを使った2Dゲームを作りたい。
- [sprite.md](src/sprite.md) — es_new/es_put/es_move/es_check(拡張スプライト命令一式)
- [hsp3dish.md](src/hsp3dish.md) — setreq/getreq(システムリクエスト), mtlist/mtinfo(タッチ入力), devinfo(デバイス情報)

## 17. 2D物理演算
物体の衝突判定・重力・跳ね返りなどの物理シミュレーションを組み込みたい。
- [obaq.md](src/obaq.md) — qaddpoly/qaddmodel(オブジェクト追加), qgravity(重力), qcollision/qgetcol(衝突判定), qpush/qblast(力を加える)

## 18. 3Dグラフィックス
3Dモデルの表示、カメラ・ライト設定、Xファイル/DXFの読み込み、パーティクル表現をしたい。
- [hgimg3.md](src/hgimg3.md) — 旧世代3Dエンジン。hgini(初期化), addbox/addxfile(モデル作成), event_*(イベント), dmm*(サウンド), newemit/hgemit(パーティクル)
- [hgimg4.md](src/hgimg4.md) — 新世代3Dエンジン。gpreset(初期化), gpload/gplight/gpcamera(ノード生成), gpaddanim(アニメーション), gppbind/gppapply(物理演算)
- [hgimg_common.md](src/hgimg_common.md) — hgimg3/hgimg4のどちらでも使える共通処理。setpos/setang/addpos等の座標操作、event_wait等のイベント登録、ベクトル演算

## 19. 画像処理(OpenCV連携)
画像のリサイズ・回転・顔認識、動画(AVI)の入出力など高度な画像処理をしたい。
- [hspcv.md](src/hspcv.md) — cvload/cvsave, cvresize/cvrotate, cvfacedetect/cvgetface, cvcapture(カメラ), cvmakeavi/cvopenavi

## 20. ハードウェア連携(Arduino・USB-IO・ジョイスティック)
Arduinoや外部USBデバイスとシリアル通信して入出力制御したい。
- [arduino.md](src/arduino.md) — arduino_init/pinmode/digitalWrite/analogRead(Arduino Firmata通信)
- [hspusbio.md](src/hspusbio.md) — uio_find/uio_out/uio_inp(USB-IOデバイス制御)
- [mod_joystick.md](src/mod_joystick.md) — ジョイスティック/ゲームパッド(8.も参照)

## 21. 印刷
プリンタへ印刷したい。
- [hspprint.md](src/hspprint.md) — enumprn(列挙), execprn(印刷実行), prndialog(設定ダイアログ)

## 22. HSPスクリプトの実行エンジン化・コンパイル・パッケージング
他アプリにHSPスクリプトエンジンを組み込みたい、スクリプトを動的にコンパイル・実行ファイル化したい。
- [hsp3imp.md](src/hsp3imp.md) — hspini/hspexec(HSP3IMP.DLLによる他アプリへの組み込み実行)
- [hspcmp.md](src/hspcmp.md) — hsc_ini/hsc_comp(コンパイル), pack_make/pack_exe(実行ファイル・DPM作成), hsc3_make/hsc3_run

## 23. HSPスクリプトエディタ拡張ツール開発
HSPの標準スクリプトエディタと連携する外部ツール・プラグインを作りたい。
- [hsedsdk.md](src/hsedsdk.md) — hsed_gettext/hsed_settext(テキスト取得・変更), hsed_undo/hsed_redo, hsed_getver

## 24. その他の補助機能
- [hsptv.md](src/hsptv.md) — HSPTV(スコアランキングサービス)へのデータ送受信
- [mod_rss.md](src/mod_rss.md) — rssload(RSSフィードの読み込み)

---

## 全ファイル一覧(五十音/アルファベット順)

| ファイル | 種別/グループ | 内容 |
|---|---|---|
| [arduino.md](src/arduino.md) | ユーザー定義命令 | Arduino Firmataとのシリアル通信 |
| [ex_macro.md](src/ex_macro.md) | マクロ | 環境判定用の標準マクロ(_debug, __file__等) |
| [form_decode.md](src/form_decode.md) | ユーザー定義命令 | フォームエンコード文字列のデコード |
| [hgimg3.md](src/hgimg3.md) | 拡張命令 | 3Dグラフィックスエンジン(旧世代) |
| [hgimg4.md](src/hgimg4.md) | 拡張命令 | 3Dグラフィックスエンジン(新世代) |
| [hgimg_common.md](src/hgimg_common.md) | 拡張命令 | hgimg3/hgimg4共通のオブジェクト操作・ベクトル演算 |
| [hsedsdk.md](src/hsedsdk.md) | ユーザー拡張命令 | HSPスクリプトエディタ連携ツール開発 |
| [hsp3dish.md](src/hsp3dish.md) | 拡張命令 | マルチプラットフォーム(HSP3Dish)システムAPI |
| [hsp3imp.md](src/hsp3imp.md) | 拡張命令 | HSP3IMP.DLLによるスクリプトエンジン組み込み |
| [hspcmp.md](src/hspcmp.md) | 拡張命令 | コンパイラ制御・実行ファイルパッケージング |
| [hspcv.md](src/hspcv.md) | 拡張命令 | OpenCVによる画像処理 |
| [hspda.md](src/hspda.md) | 拡張命令 | CSV解析、変数の一括保存/復元 |
| [hspdb.md](src/hspdb.md) | 拡張命令 | ODBCデータベース接続 |
| [hspdef.md](src/hspdef.md) | システム定義マクロ | 標準定義マクロ・演算子 |
| [hspext.md](src/hspext.md) | 拡張命令 | レジストリ/クリップボード/シリアル/ファイル操作等 |
| [hspinet.md](src/hspinet.md) | 拡張命令 | HTTP/FTP通信、JSON、エンコード変換 |
| [hspmath.md](src/hspmath.md) | ユーザー定義マクロ | 拡張数学関数・定数 |
| [hspmucom.md](src/hspmucom.md) | 拡張命令 | MUCOM88 FM音源BGM再生 |
| [hspprint.md](src/hspprint.md) | 拡張命令 | プリンタ印刷 |
| [hspsock.md](src/hspsock.md) | 拡張命令 | 低水準ソケット通信 |
| [hsptv.md](src/hsptv.md) | HSPTV操作命令 | HSPTVスコアランキング連携 |
| [hspusbio.md](src/hspusbio.md) | ユーザー拡張命令 | USB-IOデバイス制御 |
| [i_com.md](src/i_com.md) | 内蔵命令 | COMオブジェクト操作 |
| [i_file.md](src/i_file.md) | 内蔵命令 | ファイル・ディレクトリ操作 |
| [i_graph.md](src/i_graph.md) | 内蔵命令 | 2Dグラフィック描画・ウィンドウ制御 |
| [i_hsp3util.md](src/i_hsp3util.md) | 拡張命令 | GUI部品拡張、配列⇔文字列変換、画面フェード |
| [i_mem.md](src/i_mem.md) | 内蔵命令 | 配列・メモリバッファ操作 |
| [i_mmedia.md](src/i_mmedia.md) | 内蔵命令 | マルチメディア(MCI)再生 |
| [i_object.md](src/i_object.md) | 内蔵命令 | GUIオブジェクト(ボタン等) |
| [i_prep.md](src/i_prep.md) | 内蔵命令 | プリプロセッサ命令(#deffunc等) |
| [i_prog.md](src/i_prog.md) | 内蔵命令 | 制御構文(if/for/gosub等) |
| [i_stdfunc.md](src/i_stdfunc.md) | 内蔵関数 | 基本数値関数(int/rnd/sqrt等) |
| [i_stdio.md](src/i_stdio.md) | 内蔵命令 | キー・マウス入力、デバッグ、ソート |
| [i_string.md](src/i_string.md) | 内蔵命令 | 文字列・メモリノート操作 |
| [mod_fontdlg.md](src/mod_fontdlg.md) | ユーザー拡張命令 | フォント選択ダイアログ |
| [mod_joystick.md](src/mod_joystick.md) | ユーザー拡張命令 | ジョイスティック入力 |
| [mod_menu.md](src/mod_menu.md) | ユーザー拡張命令 | メニューバー作成 |
| [mod_picfont.md](src/mod_picfont.md) | ユーザー定義命令 | 画像素材フォント表示 |
| [mod_rss.md](src/mod_rss.md) | ユーザー定義命令 | RSS読み込み |
| [obaq.md](src/obaq.md) | 拡張命令 | 2D物理演算(OBAQ) |
| [obj.md](src/obj.md) | ユーザー拡張命令 | GUIオブジェクトのサイズ・座標補助操作 |
| [sprite.md](src/sprite.md) | 拡張命令 | HSP3Dish向け拡張スプライト命令 |
| [sysval.md](src/sysval.md) | HSPシステム変数 | 実行時状態を参照するシステム変数一覧 |
| [zipfile.md](src/zipfile.md) | 拡張命令 | ZIP圧縮・解凍 |
