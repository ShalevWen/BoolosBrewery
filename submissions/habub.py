# ruff: noqa: F403, F405
from base64 import b85decode
from functools import reduce
from itertools import *  # pyright: ignore[reportWildcardImportFromLibrary]
from zlib import decompress
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


personas = (Alice, Bob, Charlie, Dan)
data_table = dict(
    (
        k + 9 * (k >= 18) + 29 * (k >= 45),
        (
            [i for i in range(144) if int(dat, 16) & (0b100 << i)],
            personas[int(dat, 16) & 0b11],
        ),
    )
    for k, dat in enumerate(
        hex(
            int.from_bytes(
                decompress(
                    b85decode(
                        'EswE^+&~P5S(6-@N;pNp)vU8{TgF6%xXRCvyu!h4d0H21T<I0om2u@)v@KY%)kHRdK?C}K{rXgn<M{gV@E67~j^Xj~C<|F(o`2aq%>(cy6(Bz^FV+Mehv!__C-6h=Dco(fuX%3o!1}DaIEX=Z2?GfKJ)9-805(WyFY}*?k9K1XJe$N!1=#M&%OGdDSQvuvYgcpze3roe9c{7O8LFurdHoWVQ#A<4dYFqq%?pWMwKXuHEF#wM7T;U_M2<DoNUmwSBxEJ)3d~TH`_w8@ucRdP4-8rz6~5O%9rjPRR2H!oyt)aXikWXzWH<U)69G}%@&pzTrL>b!=lBZlZer_ru}a(Gi6BD^1xmV+M3dG$B`S6KtUDgkA(EDfvOE$vW1eXBeCoGyRaO_i<<5!Owia_mq%I;SY;r%A_06;DE!Bm^J1OFp^IuyzkuH7oleZRFzsE$CYBLjf@gOJREgDNr+{Y8P`^046fUvkC8#4ah2lIp^-qBj(zBTPoPMrM%'
                    ),
                    wbits=-9,
                ),
            )
        )
        .replace("7", "00")
        .replace("3", "0" * 5)
        .split("1")
        ####################################
        # "f,9999992666f62666f6099909999909f666f62,,900ff20ff0f02ff00f09ff09000f000600ff,90f00f2260006f000020900099900f9f0,9f006f0f000f600f90ff0990f00f2f0005,,,,f006000000f000f00000f900000f009,f90000ff000f02600099000f00f000520,20000f02f00090ff0090000f090000600f05,9f00020f00006000f0000009000f0f0000f,f02f0000000f0f000f0090f00000000f,90000f20000f600f00099000900f00026009,9009f000f00020000f09000f000f00020f00f,f000062000f0000009f000099000f204,ff00000000ff00000090000f0f00ff20,f0,909000000000206000000000ff0000000,f000000000f000ff000f000000002,f0000000000000000000000000f0f000009,f6000000000f000006f0000000000000,f00000f0f00000f0000000000000000000,f000000000f000000000f,ff0000000000000f000000000000f00009,9000000000002000000000000ff000000009,ff0000f00000000000000000000009,f000000000000f00000000000000f00000f,6000000000009f0000000000020f000000f,200000f0f000000000900000000009,f90000000000020000000000000000f00,f000000000000000f00f000000000000,f00000000000000000000000f0f000000,f02000ff000000f000000000000000000,60000000000090000f000000000000000002,f0f00000000000000000000f0000000002,2000000ff00090000000000000000000000f2,f0020000000f0000000009f00000000f,f000000ff0000000000000000000000002,f0000f00000000ff,f000000ff00000f0000000000000000000,9f00000000f020000000000000000000009,9000000000000fff006000000000f,ff0000f0000f00f000000000000000000,ff000000000000009,,f0f000000000000000000,f00000f0f000000000000000000,,f0000000f000002,ff000000002,,,f00000000fff0000000000000,,ff0000000f2,f0f000000000000000009,,f0f0000000000000000000,f00000000f0000002,,,f08,,f000000000000f00000000000000002,f0f000000000000000000000000000000,,f00000000000000000000000000000000009,f0000000000000ff0000000000002,,,f00000000000000000000000f00000000009,,f0f0000000000f0000000000000,ff00000000000000000000000000000000f,,f00000000000000000000ff,f0000000000ff0000000000000,,,f00000000000000000000000f00000000009,,f2000ff0000000f00000f,9,,ff000000009,,,,f000000000000000000000ff009,,f0f000000000000000000000000000000,ff0000000f000000f,,f0000000000000000000000000000f,f00000000000000000000002,,,f00000f0f0000000000000,,f000000000000000000000000000000000002,f00000ff0009,,f20000000000000000000,ff000000009,,,9ff000f00000000,,f0ff,f000000000000000000000000000f,,f0f0000000000000000000000000000002,ff0000000f000000f,,,ff0000000000000000000f000000000000f,,f0000000000f00f,f000000000000000000000000000f,,fff000000000000000000000000000009,f0f0000000000000000002".split(
        #     ","
        # )
    )
    if dat
)
for dat, k in enumerate(
    decompress(
        b85decode(
            "6_3ji03irN8}h(kDF+1lFJavi1IZ+h-Ice42Vmhj17TZhYq(@n0WT7mwB{%<Hr<O|3*UvBQ?ay|C{z}<ifoKbI?Hc$Z_1)4q+OIYF2Ln8XgG)U#*quD@H-Aq!N~+)SVz(lf$jQnCvu>dF3sM<VUP4Nr{CmFx*RWH7(3K^!P_mj<CX|%98p>x7Ydpc@;M&hmT``W@N?7V?~Izj&Q1F*S3KBK$<~P*kEp_IVaVO(<|>aN9$tC)=3mi!Jn0V4vePzj-i$^|zJyT2`T+"
        ),
        wbits=-15,
    )
    .decode()
    .split(",")
):
    for k_i in batched((bin(int(k, 16))[:1:-1]), 9):
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
