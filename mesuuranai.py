import MeCab
import markovify
import unidic

def main():
    # なのごん
    meigen = [
        '御目汚し失礼しましたではお客様、善きガチャライフを',
        'またのご来店、お待ちしております',
        'ﾊﾟﾝｼﾞｬﾝを選んだあなた。',
        '決断がすべて裏目に出る日に',
        'ガチャを回せば爆死し、リソースは貯めれず散々かも',
        'こんな日はおとなしくしておくに限ります。',
        'びぇぇぇぇっ。',
        'ﾊﾟﾝｼﾞｬﾝを選んだあなた。',
        '希望の星は堕ちた',
        'ガチャ運は悪いです。',
        '最高レアを引けそうにない運勢なのです',
        '気分転換にお散歩いく？',
        'ガチャ運は乱高下しそう',
        '不安定な運気なので注意',
        'あと、いいものを引けても調子にのると大損するかも',
        '刺激的なんよ～。',
        'みなさ～ん　ぱんじゃんわ～',
        'メス堕ちぃ　ユゥで～す',
        'ユゥちゃんは～？',
        '今日も～～～～～？',
        'まあ、お狐さまとの話で、ミルク飴を買ったくらいだわよ。',
        '遠くで呼んでる',
        '声がする',
        '来てよﾊﾟﾝｼﾞｬﾝ',
        '僕のところへ来てよﾊﾟﾝｼﾞｬﾝ。',
        '私のところへ',
        'ガチャ運は悪い上にヤケになってしまうかも',
        'そのせいで空っけつに',
        '無理に引かずに引き際を見極めて遊ぼうね。',
        '思慮が足りない日になりそう。',
        '貯めてたはずのリソースをガチャにしてしまったり、推しのピックアップじゃないガチャを回してしまったり。',
        'うっかりミスで無駄遣いをしないよう気を付けないと',
        'やらかしたぜ。',
        'ガチャ運の勢いがある日！勢いはだんだんと落ち着いてきてしまうので、スタートダッシュで差をつけろお先に失礼。',
        'ﾊﾟﾝｼﾞｬﾝを選んだあなた。',
        'んー。さすがにしゃぶる欲求はないのよね。',
        '触りたいだけよ。',
        '自分でもだいぶやべー状態を想像して書いてるからね。',
        '職務放棄しておきつねー様の太もももねもねしながら膝枕してもらって太ももとお腹、上に乗っかるおっぱいの柔らかさを堪能するの。',
        'いらっしゃいメス堕ち酒場へようこそ。あら、占い？じゃあ、次の三色から一つ選んで？',
        'あら、占い。',
        'じゃあ、次の三色から一つ選んで。',
        
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