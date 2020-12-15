import jaconv
import kana2vowel

# try~except文。KeyboardInterruptでCtrl+C押されるまでwhile True
try:
    while True:
        # input()で標準入力
        input_val = input("なんか言ってみて：")
        #文字種変換ライブラリjaconvでひらがな->カタカナ
        kata_val = jaconv.hira2kata(input_val)
        #kana2vowel.pyのkana2vowel関数(ユーザー関数)でカタカナから母音に変換
        hira_val = kana2vowel.kana2vowel(kata_val)
        #print(hira_val)

        # ファイル内の特定文字を見つける
        with open('/home/yudai/Dev/ML/word_play/boin.txt') as fin:
            for row, text in enumerate(fin):
                # 文字列の末尾の\nを除去(replaceでも可)
                text = text.rstrip()
                #解析した母音と一致するテキストを見つける
                if text == hira_val:
                    # 母音と一致する行数
                    dst_row = row


        with open("/home/yudai/Dev/ML/word_play/goi.txt") as f:
            # goi.txtで見つけた行を読み込む
            data = f.readlines()[dst_row]
            # 2行目以降から\nが含まれるのでreplace()で除去
            data = data.replace("\n", "")
        print(data + "？\n")
except KeyboardInterrupt:
    print("\nBREAK")