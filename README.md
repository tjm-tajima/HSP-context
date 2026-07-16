# HSP Knowledge

このリポジトリは、HSP のヘルプソース（`.hs`）を Markdown に変換し、参照しやすく整理した知識ベースです。HSP で「何を作りたいか」から必要な命令を探せるように、カテゴリ別の索引と、命令ごとの詳細ドキュメントをまとめています。

## 何が入っているか

- [Knowledge_index.md](Knowledge_index.md) は、目的別に参照先をまとめた入口です。
- [src/](src) には、HSP ヘルプソースから変換した Markdown が並んでいます。
- [converter/convert_hs_to_md.py](converter/convert_hs_to_md.py) は、`.hs` から `.md` を生成する変換スクリプトです。

## 使い方

まず [Knowledge_index.md](Knowledge_index.md) を開き、作りたい機能に近いカテゴリを探してください。そこから各 `src/*.md` に移動すると、命令の構文、パラメータ、説明、サンプルを確認できます。

## 更新方法

`.hs` を追加・更新したあと、次のスクリプトを実行すると `src/` 配下の Markdown を再生成できます。

```bash
python converter/convert_hs_to_md.py
```

このスクリプトは `src/` 配下の `.hs` をまとめて読み込み、同名の `.md` を出力します。元データは Shift-JIS 系の文字コードを前提にしているため、変換時はその点に注意してください。

## ディレクトリ構成

- `Knowledge_index.md` - 目的別索引
- `converter/` - 変換ツール
- `src/` - 変換済みの Markdown と元の `.hs`
<<<<<<< HEAD

## ライセンス

本ドキュメントは、Hot Soup Processor (HSP) の公式リファレンスを基にMarkdown形式へ変換・再構成したものです。
元のドキュメントの著作権は Onion Software / onitama に帰属し、修正BSDライセンスの下で配布されています。詳細なライセンス条文については [LICENSEファイルへのリンク](HSPLicense.txt) を参照してください。
=======
>>>>>>> a498351 (first commit)
