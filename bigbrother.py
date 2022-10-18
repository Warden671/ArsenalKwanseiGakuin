import MeCab
import markovify
import unidic

def main():
    # なのごん
    meigen = [
        '路上、スタンガンの電撃が撃つ群衆の影、ヤイヤイと人は行き秘密裏に事は成る。',
        '聞けよ物陰で｢良き事のため｣と囁く見えないブラザーが暗示のようにキミを追う。',
        '列を成せ、汝従順のマシン、享受せよさあ　思慮は今罪と知るべし。',
        '夜景　遍く憎悪の声は歓喜する。',
        'ヤイヤイと踏み鳴らし逸脱の民を撃てと、聞けよ窓辺で｢良き事のため｣と連呼する見えないブラザーが、保護者のようにキミを見る。',
        '聞けよ窓辺で｢良き事のため｣と連呼する',
        '見えないブラザーが保護者のようにキミを見る。',
        '踏み鳴らせ　汝善良のマシン',
        '連呼せよさあ　思慮は今罪と知るべし。',
        'ヤイヤイと人人人の目がキミを追う。',
        'ヤイヤイと人人人の目がキミを見る。',
        '無情　明日の日はキミのためにはあらずと、隅々に地を覆い逃亡の夢も砕く。',
        '隅々に地を覆い逃亡の夢も砕く。',
        '聞けよ目の前で｢良き事のため｣と囁く',
        '見えないブラザーが暗示のようにキミを見る',
        '列に立て　汝従順の下部',
        '甘受せよさあ　思慮は今罪と知るべし',
      
        ]
    mecab = MeCab.Tagger()

    # 処理不能のデータの定義
    breaking_chars = ['(', ')', '[', ']', '"', "'"]
    # 一文化
    splitted_meigen = ''

    for line in meigen:
        print('Line : ', line)
        parsed_nodes = mecab.parseToNode(line)

        while parsed_nodes:
            try:
                # 不可能な処理のスキップ
                if parsed_nodes.surface not in breaking_chars:
                    splitted_meigen += parsed_nodes.surface
                # 句読点以外であればスペースを付与して分かち書きをする
                if parsed_nodes.surface != '。' and parsed_nodes.surface != '、':
                    splitted_meigen += ' '
                # 句点が出てきたら文章の終わりと判断して改行を付与する
                if parsed_nodes.surface == '。':
                    splitted_meigen += '\n'
            except UnicodeDecodeError as error:
                print('Error : ', line)
            finally:
                # 次の形態素に上書きする。なければNoneが入る
                parsed_nodes = parsed_nodes.next

    print('解析結果 :\n', splitted_meigen)

    # マルコフ連鎖のモデルを作成
    model = markovify.NewlineText(splitted_meigen, state_size=2)

    # 文章を生成する
    sentence = model.make_sentence(tries=100)
    if sentence is not None:
        # 分かち書きされているのを結合して出力する
        print('---------------------------------------------------')
        print(''.join(sentence.split()))

        print('---------------------------------------------------')

    else:
        print('Fuck NANOGON!')


if __name__ == "__main__":
    main()