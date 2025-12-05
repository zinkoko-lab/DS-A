class Node {
    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

class LinkedList {
    constructor(head = null) {
        this.head = head;
    }

    countNode() {
        let count = 0;
        let curNd = this.head;
        while (curNd) {
            curNd = curNd.next;
            count++;
        }
        return count;
    }

    showList() {
        if (!this.head) {
            console.log("This is an empty linked list.");
            return;
        } else {
            let curNd = this.head;
            let output = "";
            while (curNd) {
                output += curNd.next ? `${curNd.val} -> ` : `${curNd.val}`;
                curNd = curNd.next;
            }
            console.log(output);
        }
    }

    // listの先頭に new node を加えるメソッド
    addFirst(val) {
        const newNode = new Node(val);
        newNode.next = this.head;
        this.head = newNode;
    }

    // 末尾に new node を加えるメソッド
    addLast(val) {
        // 空っぽの list であれば、先頭に new node を加える
        if (!this.head) {
            this.addFirst(val);
        } else {
            // 空っぽでないときは、先頭から一個一個たどって最後の nodeに辿り着くまで行く
            let curNd = this.head;
            const newNode = new Node(val);
            while (curNd.next) {
                curNd = curNd.next;
            }
            curNd.next = newNode;
        }
    }

    // listの任意のindex に new node を加えるメソッド
    add(index, val) {
        const size = this.countNode();

        // (listの長さ+1)より大きいindex番号を与ると、範囲外エラーとなる
        if (index > size + 1) {
            console.error(
                `Your index(${index}) is out of range!\nIndex must in the range of between 1 and ${
                    size + 1
                }.`
            );
            return;
        }

        // index-1 start 仕様だと考え、index番号を0と与えたときはエラーとなる
        if (index == 0) {
            console.error(
                `Your index(${index}) is invalid index number!\nIndex must in the range of between 1 and ${
                    size + 1
                }.`
            );
            return;
        }

        // 有効な範囲は (1 ~ size + 1) or (index < 0)となる

        // index 番号が 1 の場合は listの先頭に new nodeを加える
        if (index == 1) {
            this.addFirst(val);
        }

        // index 番号がマイナスまたは size + 1の場合は末尾に new nodeを加える
        else if (index < 0 || index == size + 1) {
            this.addLast(val);
        }

        // その他の場合(つまり 1 < index <= size)
        else {
            let newNode = new Node(val);
            let curNd = this.head;
            let curNdIdx = 1;
            while (curNdIdx < index - 1) {
                curNd = curNd.next;
                curNdIdx++;
            }
            newNode.next = curNd.next;
            curNd.next = newNode;
        }
    }

    // listの先頭の node を削除するメソッド
    removeFirst() {
        if (!this.head) {
            console.error(
                "This is an empty linked list and no element to remove."
            );
            return;
        } else {
            let curNd = this.head;
            this.head = curNd.next;
            curNd.next = null;
        }
    }

    // listの最後の node を削除するメソッド
    removeLast() {
        // listが空っぽのときはエラーを表示
        if (!this.head) {
            console.error(
                "This is an empty linked list and no element to remove."
            );
            return;
        }

        if (this.countNode() == 1) {
            this.removeFirst(); // listの中身は node 1個のみの場合は先頭を削除
        } else {
            const size = this.countNode();
            let curNd = this.head;
            let curNdIdx = 1;
            while (curNdIdx < size - 1) {
                curNd = curNd.next;
                curNdIdx++;
            }
            curNd.next = null;
        }
    }

    // listの任意の index の node を削除するメソッド
    remove(index) {
        const size = this.countNode();

        // index番号が size + 1より大きいと、範囲外エラーを出す
        if (index > size + 1) {
            console.error(
                `Your index(${index}) is out of range!\nIndex must in the range of between 1 and ${
                    size + 1
                }.`
            );
            return;
        }

        // index-1 start 仕様だと考え、index番号を0と与えたときはエラーを表示
        if (index == 0) {
            console.error(
                `Your index(${index}) is invalid index number!\nIndex must in the range of between 1 and ${
                    size + 1
                }.`
            );
            return;
        }

        // index の有効範囲は (1 ~ size + 1) or (index < 0)

        // index == 1の場合は、 先頭の nodeを削除するメソッドを実行
        if (index == 1) {
            this.removeFirst();
        }

        // index < 0 or index == size + 1 の場合は、最後の nodeを削除するメソッドを実行
        else if (index < 0 || index == size + 1) {
            this.removeLast();
        }

        // 1 < index < index + 1 の場合:
        else {
            let curNd = this.head;
            let curNdIdx = 1;
            while (curNdIdx < index - 1) {
                curNd = curNd.next;
                curNdIdx++;
            }
            const target = curNd.next;
            curNd.next = target.next;
            target.next = null;
        }
    }
}
some_quote = new LinkedList();
some_quote.addFirst("if");
some_quote.addLast("there");
some_quote.add(3, "is");
some_quote.add(4, "no");
some_quote.add(5, "struggle");
some_quote.add(6, "there");
some_quote.add(7, "is");
some_quote.add(8, "no");
some_quote.add(9, "progress");
some_quote.showList();
some_quote.remove(5);
some_quote.showList();
some_quote.add(5, "apple");
some_quote.showList();
