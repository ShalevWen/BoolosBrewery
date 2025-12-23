# ruff: noqa: F403, F405
from functools import reduce
from itertools import *  # pyright: ignore[reportWildcardImportFromLibrary]
from strats import *


# This is an optimized version of ganitsu_optim.

# I don't even know how I did it, but in the process of compressing the data
# I also improved the questions average


perm_scenarios = list(
    product(
        permutations(responses := (Foo, Bar, Baz)),
        permutations(fields := (Math, Phys, Phil, Engg)),
    )
)


def unpack_int(s: str) -> int:
    return int("".join(f"{ord(c):0{4 if (ord(c) > 0xFF) else 2}x}" for c in s), 16)


personas = (Alice, Bob, Charlie, Dan)
data_table = dict(
    (
        k + 9 * (k >= 18) + 29 * (k >= 45),
        (
            [i for i in range(144) if unpack_int(dat) & (0b100 << i)],
            personas[unpack_int(dat) & 0b11],
        ),
    )
    for k, dat in enumerate(
        ",𑦱㹤䕊쑄总ထ馑៤䱂,,选ꋢ툤⪰༙ﻙ㤈챧坣,𤄉䠈눴蠖딂䘌ᐉ蠀ᵠ,𢂆♣⋅你䢈静飀꡶梥,,,,ﻠ洄鈃∃  ஈ  顅,‑艂䉠  ␉餕馸謄┬,  겢썤삡ࢱ쥜ę鹡옱,妀    蘀̔  쉀뀞㈃,•  ဉ到類肀  ဣ,𑑍ࡡ䐌渣㒱脐聃ʂ䐅,𘫈ा塒  惈藐Ƥ  ⁇,弁쐩Ӓ  閺눚傂∄,䬒  ჲ  䎀膚ࢁ꠬,  ,愩ᧁ㔅Ⴢꐍ  ᅈ    ,즡    ⾪䵔၀  鋊,𢞲          禊㯼㻽,p㐽  ဃ脉谑      ,   뿙ʀ耚        ,鼿    刀  㧧,ⲡ      ꒋ    쿝ߍ,茈          菒  ﹡,궡  Ｂ    ဿ  羕,נּ    Ҁ  ࠇ  ﻰဣ,𦞤  锐髡      ꅰ倓,   큤    찳  短,hᏽ            ࠐ,㕂      ᥚ      ,ꈗ          ⛯м  ,䠒  穼  䪷    胣  ,怐҈  က䌖屰    ៦,𠋿햊        ֈ  ﹒,2  쥴쬅          鏶,搃  ᕸॅ  ೀ  כּ,𘥀  ﹙          ﹲ,널﹘  芯,𘁔  歰  世    컭  ,ↀ  蠬㩊        ➭,h  聀ͅ⾑ր  퐿,n态舢䀰⪁        ,挻﷿    㿭,,ﯽￖ        ,緇곆￢        ,,Ｏ  ﾴ奶,蟾  쑞,,,﷿    㯻    蟜,,뽭  㻾,ｷ﷿      믭,,ﭾ？        ,﷿    ﾢ㾲,,,㏸,,玢    鑡      ᗞ,忿羠              ,,ﷴ    侞        痉,ﭱ      쿽    ꥮ,,,젠됏            ꗭ,,矞            ,𢮿              ﷿,,ﱟ        ﷿,ﾯ    뫋      ,,,찵㐞        Ｙ  ﾽ,,翿  濜  ɷ혛,﷽,,쿯  ﷽,,,,ﾥ  ᾬ    롟ﾥ,,ﯯﲽ              ,ￗ먟    矿,,ꛫ        嶷  뭿,忿        왮,,,枿  櫃    豨,,c息              彺,￭ﯼ홉,,烿          ,翷  Ｍ,,,路樂    ,,䠇    ꫳ,뿿            쑇,,꺿翱            屲,敇ꌛ    ᨿ,,,𘯪              ㍟,,彿    暟,廿            ྿,,𧿲쯽            巹,ￒ尠      ၢ".split(
            ","
        )
    )
    if dat
)
for dat, k in enumerate(
    "߭볪㼀,𘣰ꙵ흚钾ⴃ,␏뛣괆㙗,㥝᭮𮎵𝗓𢩔,Ṕ䜚묨,鳞ç𫴤,᭬ᓦ㴁,鿱懸㗊蓀딄,ᮃﴈ묉,ǘ䭫𐍬颙𢤂,Ṏ㧯㩠,ᯎ맋㜥,जƦ㤍,𘧩歹𗒪N👒,বഎ㔋,𘪻瓹㫺ꦌ뛹,ᶭ羽뜧,᷄騶딦,諊𝣚f,ᩌ綖镀,ᩬ鶚霶,ƥ좛𬼿,ڎ漈,梮𖬼𡃟5".split(
        ","
    )
):
    for k_i in batched((bin(unpack_int(k))[:1:-1]), 9):
        data_table[int("".join(k_i[::-1]), 2)] = dat  # pyright: ignore[reportArgumentType]


class Strategy(Hard):
    engg_question_limit = 2

    def solve(self):
        nodo_actual = 1
        while True:
            if isinstance(target := data_table[nodo_actual], int):
                self._guess = dict(
                    zip(
                        map(str, personas),
                        perm_scenarios[target][1],
                    )
                )  # pyright: ignore[reportAttributeAccessIssue]
                return
            nodo_actual = nodo_actual * 3 + responses.index(
                self.get_response(
                    target[1].ask(
                        reduce(
                            Expr.or_,
                            [
                                reduce(
                                    Expr.and_,
                                    [
                                        p.studies(sfield).and_(
                                            Person.ask(str(f)[:4], True).equals(  # pyright: ignore[reportArgumentType]
                                                sresponse
                                            )
                                        )
                                        for p, f, sresponse, sfield in zip(
                                            personas,
                                            fields,
                                            *perm_scenarios[var],
                                        )
                                    ],
                                )
                                for var in target[0]
                            ],
                        )
                    )
                )
            )
