import MeCab
import markovify
import unidic

def main():
    # なのごん
    meigen = [
        'なのごんのアカウントはご自由にフォローしたりクソリプ送り付けてもいいよ。',
        '大怪獣なのごんは体長70メートルでしっぽの長さ60センチでフグと青梅の毒を体内にもってます。',
        'なのごんを好きっていう感情の寿命って鬼短いから人でも物でも好きなことがある人は死ぬほど熱中すべきだと思います。',
        'なのごんは8月の世界から現れた生命体で、あちこちに現れる。',
        'なのごんは調子がいい時こそ気を引き締める目標は高く鼻を伸ばし、地に足つけて真摯にYouTubeに向き合う腰の低い天狗スタイル。',
        'キレ草を吸いすぎた世界線のなのごん。',
        '昔の子だからなのごんのふくちゃんとはるちゃんはこの端末に居ないの。',
        '雷雨の日にはもっと増えるよ',
        'よく分裂したり消滅したりするけど雨の日にいっぱい増えるよ。',
        'なのごんにとって、成功も失敗も全て作戦通り。',
        'なのごんのやらない言い訳より、できる理由を探す用は何に目を向けるかで180度見える景色が変わってくるそして決断するにあたって時間が経過すればするほど言い訳を探してしまうから、思い立ったら即行動に移すシンプルかつこれが人生のエッセンス。',
        'なのごんは面白いと言われたら喜んで、つまらないとdisられたら無視する幸せでいる秘訣です。',
        'なのごんは8月の世界から現れた生命体で、あちこちに現れる。',
        'なのごんが挫折する1番の原因は「やる前の努力量の見積もりのミス」だと思う死ぬ気でやりもしないで諦めていく奴が多すぎる「こんだけやったら上手くいくだろ」じゃなくて、「上手くいくまでやる」と決めないと現実の厳しさを目の前に折れる。',
        'なのごんが上手くいかないのは全部自分のせいだし、結果が出ないのも自分のせい時代でも、家庭でも、他人のせいでもなく全部自分のせい結果に全責任を負えないようじゃ二流だしパンピーだと思うから俺らはコツコツやることやる。',
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