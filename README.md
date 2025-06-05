# Discord Relay Bot

Discordのテキストチャンネルを中継するボットです。

主な機能：
- テキストメッセージの中継。メッセージ削除・編集も同期します
- 画像・動画の共有

## Makefile

- `make init`：依存関係をインストール（`rye sync`を実行）
- `make run`：実行中のbotを停止後、フォアグラウンドでbotを起動
- `make run-back`：実行中のbotを停止後、バックグラウンドでbotを起動
- `make stop`：実行中のbotプロセスを停止

## 開発環境

- [Rye](https://rye.astral.sh/)

## 導入

```bash
rye sync
```

`pyproject.toml` に定義されたランタイムおよび開発用依存関係をインストールします。

`config.json`にて認証情報およびチャンネルのIDを設定してください。  
サンプルが`config.example.json`にあるので参照してください。

```bash
cp config.example.json config.json
```

## 使用方法

```bash
rye run python bot.py
```
