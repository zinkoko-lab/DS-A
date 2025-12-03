了解しました！  
では **Step 1：Hello World（超基本）** を「講師としてステップバイステップ」で解説します。

---

# 🧭 **Step 1：Hello World — 多言語を横断しながら理解する**

目的は単に表示することではなく、

> **プログラミング言語が何をしているのか**  
> **言語ごとの違いは何か**

を理解することです。

---

# ✅ **まずは共通の理解：Hello World の意味**

すべての言語で、Hello World は次の 2 つをやっています：

1. **文字列（String）"hello, world" をメモリに作る**
2. **それを標準出力（console / terminal）に表示する**

---

# 📘 **擬似言語（Pseudo code）で書くとこうなります**

```
START
  SET message = "hello, world"
  PRINT message
END
```

この抽象的な動作を、  
Python・JavaScript・C がどう具体的に書くかを理解していきます。

---

# 🐍 **Python の Hello World**

Python は「スクリプト言語」であり、  
**コンパイルが不要で、文法が最もシンプル。**

```python
print("hello, world")
```

### ✔ Python の特徴（Hello World からわかるポイント）

-   行頭に型を書く必要がない（動的型付け）
-   セミコロン不要
-   main 関数不要
-   インタプリタ（直接実行）

---

# 🌐 **JavaScript の Hello World**

JavaScript は「Web ブラウザ」または「Node.js」で動くスクリプト言語。

```javascript
console.log("hello, world");
```

### ✔ JavaScript の特徴

-   セミコロンが使われる（なくても動くが推奨）
-   `console.log()` を使う（Python の print と同じ）
-   Web ブラウザと Node で評価される

---

# 🧱 **C の Hello World（もっとも重要）**

C は**コンパイル言語**であり、メモリ管理も必要。

```c
#include <stdio.h>

int main() {
    printf("hello, world");
    return 0;
}
```

### ✔ C の重要ポイント（Hello World で覚えるべき基礎）

| 仕組み               | 意味                               |
| -------------------- | ---------------------------------- |
| `#include <stdio.h>` | 標準入力/出力ライブラリの読み込み  |
| `main()`             | C プログラムは必ずここから実行開始 |
| `printf()`           | 文字列を出力                       |
| `return 0;`          | 正常終了を OS に伝える             |

---

# 📌 **3 言語の違い（Hello World からわかる本質）**

| 項目            | Python       | JavaScript   | C              |
| --------------- | ------------ | ------------ | -------------- |
| 実行方法        | インタプリタ | インタプリタ | コンパイル必要 |
| 文法の簡単さ    | ◎            | ○            | △              |
| main 関数必要？ | ×            | ×            | 〇             |
| セミコロン      | 不要         | あっても OK  | 必須           |
| メモリ管理      | 自動         | 自動         | 手動           |

要するに：

> **Python → 高レベルで超簡単**  
> **JS → Python より少し形式的**  
> **C → OS と直接話す低レベル言語で一番むずい**

これをまず押さえましょう。

---

# 🚀 **次のステップ（選択）**

Step 1 が終わったので、次に進めます。

次はどれを学びたいですか？

### A. Step 2：ループ（課題 2 の 1²+2²+…+100² の和）

### B. Step 3：再帰（課題 3 の再帰バージョン）

### C. Step 4：構造体（C 言語の struct の本質）

### D. Step 5：Linked List（ポインタの理解が深まる）

好きなものを選んでください。
