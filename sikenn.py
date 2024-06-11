flag = 0

def compare_strings(reference, test):
    global flag
    # 結果を格納するリスト
    result = []
    # 基準文字列と試験文字列を比較
    for i in range(len(reference)):
        if i < len(test) and reference[i] != test[i]:
            result.append('v')
            flag = 1
        else:
            result.append(' ')
    return ''.join(result)

def main():
    global flag
    # ユーザーからの入力を受け取る
    reference = input("基準: ")
    test = input("試験: ")
    
    # 間違い箇所を示す結果を取得
    result = compare_strings(reference, test)
    
    # 基準、試験、間違い箇所を表示
    print("-----------以下より比較結果を示す-----------\n")
    print("基準: " + reference)
    print("      " + result)
    print("試験: " + test)
    
    if flag == 1:
        print("\nvの部分が間違っている")
    else:
        print("\n相違点はない")

if __name__ == "__main__":
    main()