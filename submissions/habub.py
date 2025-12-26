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
                        "C6B#s6HyR_C##LM+w6n}k-`pzB`Q1b5T!+a0!#|pAa`4>LI;gSDASl%8m;8WF2+|*fpBy0Xp3AZW^cyO&Ci)R-#OWz|9Jgrc6B|wIX`>#aDQ<<yYlzgp~$6RnM(Hv>44CUA2lns-{7zOmVxLq{6TrJxz2rnTjvOuAg5u8D&y@?aQ*g)>_vf6k_-nRqn|ChTirOMUM?BY!51amQ%BFBZ#JM~n4jgU6D*u-G4C~>=vs>pT^>xR8xp~;l0(UD&Q2+?bE=eu8j;HIo)u<`K-OS$T(S!h?`XATc$XMPi6YZHMo{QKGJR*t(8>vj@{-FiG#yD59mLSEO?NU$9QhaP2}K$NdyCvYaauQwpKmfo-WXZnR8JKdl2u3Vy$!R5S6`Ey8iXPVHoLSay+l3&HoK#8V6ieE>@HSTcJ?1u0Zqc7tq+Bdk){$&T{Dd$#;Lai$Yd&}Sf!ew4+hmMW30To=HJq&k?`Ox^vYY51oMD3n}<3d8?=%68ppyqhH0X-^<6_IDE%RcMe&kC?Toi+|DT1(c<0Rr`nbS8q?$?tZeIW"
                    ),
                    wbits=-9,
                ),
            )
        )
        .replace("7", "d" * 4)
        .replace("d", "0" * 3)
        .split("e")
        ####################################
        # "1,1199116644f42444f6019101199901f444f42,,900ff20ff0f02ff00f09ff09000f000600ff,90f00f2240006f000020800098800f9f0,8f006f0f000f600f80ff0990f00f2f0005,,,,f006000000f000f00000f800000f005,f80000ff000f02400091000f00f000520,20000f02ff0080ff0090000f010000600f01,9f00020f000f6000f0000008000f0f0000f,f02f0000000f0f000f0080f00000000f,10000f20000f600f00018000800f00024005,1004f000f00020000f08000f000f00020f04f,f000042000f0000005f000085000f204,ff00000000ff00000080000f0f00ff20,f0,909000000000204000000000ff0000000,f000000000f000ff000f000000002,f0000000000000000000000000f0f000009,f4000000000f000004f0000000000000,f00000f0f00000f0000000000000000000,f000000000f000000000f,ff0000000000000f000000000000f00009,8000000000002000000000000ff000000001,ff0000f00000000000000000000005,f000000000000f00000000000000f00000f,5f00000000008f0000000000020ff00000f,200000f0f000000000800000000009,f10000000000020000000000000000f00,f000000000000000f00f000000000000,f00000000000000000000000f0f000000,f02000ff000000f000000000000000000,6000000f000010000f000000000000000006,f0f00000000000000000000f0000000002,2000000ff00050000000000000000000000f6,60020000000f0000000008f00000000f,f000000ff0000000000000000000000002,f0000f00000000ff,f000000ff00000f0000000000000000000,1f00000000f020000000000000000000009,8000000000000fff005000000000f,ff0000f0000f00f000000000000000000,ff000000000000009,,f0f000000000000000000,f00000f0f000000000000000000,,f000000ff000006,ff000000002,,,f00000000fff0000000000000,,ff0000000f2,f0f000000000000000009,,f0ff000000000000000000,f00000000f0000002,,,f08,,f000000000000f00000000000000002,f0f000000000000000000000000000000,,f00000000000000000000000000000000001,f0000000000000ff0000000000002,,,f00000000000000000000000f00000000009,,f0f0000000000f0000000000000,ff00000000000000000000000000000000f,,f00000000000000000000ff,f0000000000ff0000000000000,,,f000000f0000000000000000f00000000009,,f2000ff0000000f00000f,9,,ff000000009,,,,f000000000000000000000ff005,,f0f000000000000000000000000000000,ff0000000f000000f,,f0000000000000000000000000000f,f00000000000000000000002,,,f00000f0f0000000000000,,f000000000000000000000000000000000002,ff0000ff0009,,f20000000000000000000,ff000000009,,,9fff00f00000000,,f0ff,f000000000000000000000000000f,,f0f0000000000000000000000000000002,ff0000000f000000f,,,ff0000000000000000000f000000000000f,,f0000000000f00f,f00000000000000000000000000ff,,fff000000000000000000000000000009,f0f0000000000000000002"
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
