# arduino

- **種別**: ユーザー定義命令
- **グループ**: 拡張入出力制御命令
- **バージョン**: 3.5
- **更新日**: 2016/07/01
- **作者**: onitama
- **URL**: http://hsp.tv/
- **対応環境**: Win
- **備考**: arduino.asをインクルードすること。

## 命令一覧

| 命令 | 概要 |
|---|---|
| [arduino_init](#arduino_init) | arduino通信の初期化 |
| [arduino_bye](#arduino_bye) | arduino通信の終了 |
| [arduino_exec](#arduino_exec) | arduino受信処理の実行 |
| [delay](#delay) | 時間待ち |
| [pinmode](#pinmode) | ピンのモード設定 |
| [digitalWrite](#digitalwrite) | デジタルデータの出力 |
| [analogWrite](#analogwrite) | アナログデータの出力 |
| [digitalRead](#digitalread) | デジタルデータの読み出し |
| [analogRead](#analogread) | アナログデータの読み出し |
| [analogReport](#analogreport) | アナログデータの読み出し設定 |
| [digitalReport](#digitalreport) | デジタルデータの読み出し設定 |
| [analogInterval](#analoginterval) | アナログデータの読み出し間隔設定 |

## 命令詳細

### arduino_init

arduino通信の初期化

**構文**
```
arduino_init port, baud
```

**パラメータ**
- `port=0～(0)`: COMポート番号
- `baud=0～(0)`: 通信ボーレート

**説明**

USBを経由したarduinoデバイスとのシリアル通信を初期化します。
初期化の結果が、システム変数statに反映されます。
statが0の場合は、初期化が正常に終了したことを示します。
それ以外の場合は、エラーが発生しています。エラーが発生した場合は、変数arduino_errorにエラーメッセージが格納されます。

arduino.asがサポートする命令を使用する際には、最初に必ずarduino_initを呼び出して下さい。
arduino_init命令には、COMポート番号とボーレートのパラメーターを正しく指定する必要があります。
Arduino IDEで通信を行なっているCOMポート番号、及びfirmataで使用しているボーレート(通常は57600)を適切に記述してください。

**関連**: arduino_bye, arduino_exec

---

### arduino_bye

arduino通信の終了

**構文**
```
arduino_bye
```

**パラメータ**
- なし

**説明**

arduinoデバイスとのシリアルポートの解放を行ない通信を終了します。

**関連**: arduino_init, arduino_exec

---

### arduino_exec

arduino受信処理の実行

**構文**
```
arduino_exec
```

**パラメータ**
- なし

**説明**

USBを経由したarduinoデバイスとの受信処理を実行します。
結果が、システム変数statに反映されます。statが0の場合は、初期化が正常に終了したことを示します。
それ以外の場合は、エラーが発生しています。エラーが発生した場合は、変数arduino_errorにエラーメッセージが格納されます。
arduino_exec命令は、シリアル通信を監視して、arduinoからのメッセージを適切に処理します。
アプリケーションの動作中は、一定時間ごとに実行するようにしてください。

**関連**: arduino_init, arduino_bye

**サンプル**
```hsp
	arduino_exec
	if stat {
		; エラーがあれば終了
		dialog arduino_error
		end
	}
```

---

### delay

時間待ち

**構文**
```
delay ms
```

**パラメータ**
- `ms=0～(0)`: 実行を待つ時間(ミリ秒単位)

**説明**

指定された時間、スクリプトの実行を停止させます。
内部的には、await命令と変わりありません。
arduino IDEで用意されているdelay関数と互換で使用することができます。

**関連**: await, arduino_init

---

### pinmode

ピンのモード設定

**構文**
```
pinmode pin, outmode
```

**パラメータ**
- `pin=0～(0)`: デジタルピン番号
- `outmode=0～(0)`: 設定されるモード(MODE_*)

**説明**

arduinoのデジタルピンを指定したモードに設定します。
たとえば、「pinmode 9, MODE_OUTPUT」は、9番のピンをデジタル出力に設定します。
pinmode命令は、firmataで規定されたいくつかのモードを指定することができます。
以下のモードがマクロとして定義されています。
```
	モード名       内容
	--------------------------------
	MODE_INPUT    デジタル入力
	MODE_OUTPUT   デジタル出力
	MODE_ANALOG   アナログ出力
	MODE_PWM      PWM制御(出力)
	MODE_SERVO    サーボ制御(出力)
```
適切にモード設定を行なった後は、指定されたピンでの入出力が可能になります。

**関連**: digitalWrite, analogWrite, digitalRead, analogRead

---

### digitalWrite

デジタルデータの出力

**構文**
```
digitalWrite pin, value
```

**パラメータ**
- `pin=0～(0)`: デジタルピン番号
- `value=0～(0)`: 出力する値

**説明**

pinで指定されたピンに、valueで設定された値を出力します。
出力される値は、0(OFF)、か1(ON)のどちらかになります。「D_LOW」(OFF)、か「D_HIGH」(ON)のマクロを指定することも可能です。

**関連**: analogWrite

---

### analogWrite

アナログデータの出力

**構文**
```
analogWrite pin, value
```

**パラメータ**
- `pin=0～(0)`: デジタルピン番号
- `value=0～(0)`: 出力する値

**説明**

pinで指定されたピンに、valueで設定された値を出力します。
出力される値は、0(最小)から255(最大)の範囲となります。「D_LOW」(0)、か「D_HIGH」(255)のマクロを指定することも可能です。

**関連**: digitalWrite

---

### digitalRead

デジタルデータの読み出し

**構文**
```
digitalRead(pin)
```

**パラメータ**
- `pin=0～(0)`: デジタルピン番号

**説明**

pinで指定されたピンの内容を取得します。
取得される値は、0(OFF)、か255(ON)のどちらかになります。「D_LOW」(OFF)、か「D_HIGH」(ON)のマクロにより比較することも可能です。

**関連**: analogRead, digitalReport

---

### analogRead

アナログデータの読み出し

**構文**
```
analogRead(analogpin)
```

**パラメータ**
- `analogpin=0～(0)`: アナログピン番号

**説明**

pinで指定されたアナログピンの内容を取得します。
取得される値は、0(最小)、か1023(最大)の範囲になります。「A_LOW」(最小)、か「A_HIGH」(最大)のマクロにより比較することも可能です。
```
	digitalReport 0, 1	; アナログポート0を読み出す設定
	value=analogRead(0)	; 実際の値を読み出す
```
初期化の後に、analogReport命令を使って指定されたポートの読み出しを開始する必要があるので注意してください。
また、analogInterval命令によりアナログポート読み出しの周期を設定することも可能です。

**関連**: analogReport, analogInterval, digitalRead

---

### analogReport

アナログデータの読み出し設定

**構文**
```
analogReport analogpin, sw
```

**パラメータ**
- `analogpin=0～(0)`: アナログピン番号
- `sw=0～(0)`: 読み出し設定(0=OFF,1=ON)

**説明**

指定されたアナログピンの読み出しON/OFFを制御します。
analogRead命令による読み出しの設定を行なう場合は、必ず読み出し設定をONにする必要があります。(デフォルトはOFFに設定されています)
読み出し設定がONの時は、analogInterval命令により設定された周期でアナログピンの値が更新されます。

**関連**: analogRead, analogInterval

---

### digitalReport

デジタルデータの読み出し設定

**構文**
```
digitalReport port, sw
```

**パラメータ**
- `port=0～(0)`: デジタルポート番号
- `sw=0～(0)`: 読み出し設定(0=OFF,1=ON)

**説明**

指定されたデジタルピンの読み出しON/OFFを制御します。
読み出し設定がONの時は、デジタルピンの変更を取得可能になります。
(デフォルトはONに設定されていますので、通常は特に設定する必要ありません)
digitalRead命令による読み出しの設定を行なう場合は、必ず読み出し設定がONになっている必要があります。

**関連**: digitalRead

---

### analogInterval

アナログデータの読み出し間隔設定

**構文**
```
analogInterval analogpin, ms
```

**パラメータ**
- `analogpin=0～(0)`: アナログピン番号
- `ms=0～(0)`: 読み出し間隔(ミリ秒単位)

**説明**

指定されたアナログピンの読み出し間隔をミリ秒単位で設定します。

**関連**: analogRead, analogReport

---
