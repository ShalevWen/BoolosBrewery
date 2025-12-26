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
                        "EswEk8$l3;;fO-6(Y%5P23J16gu#{bCMJiQCB>q=fWV!&;!dx$h&cF)UkidjuGw9L@Ze%@GBSaMEoT1j|EB4>?&|JrukPxutIv1mW{M{&<yOkB^b{U-qWJaUv+V28_3vep?-btRPpzNjB#V^f5kjC%kl`H~%2nus$YOPbF`jiq>3_$?B$dU2U_*qt+#(dAS6WXv;VoLEm+E2YcR?zY4cSN4EWd6DFEaMD`lf3^A1R)eWvbiNJqeafK?67Jj9KS<!Y9U3j2zh8u$|QhhK!T1eB?pF9s`3BL4Wv_!%9I%5VhMeZ^QNazzD*~?xKfW1x0iRJ8%TIO<^C~=EjcPdYq1X1g?1&sC&v_&4?exyLIJI|MgK{%m5M%p;ny99ZZgWvIwfoO=30SEFfdIw!l8Gu}}F+GRr3mcqDe-oQYxU9^`G!TS}dq%~P|tBa?MI9@EK$gM@j=JS3Zv3?Gn71)`xa8>2}V4J&poG-~Gz`Pwh_N19YP70u35Dz?1;pUdpYTRcV^X;K^2#@+t|"
                    ),
                    wbits=-15,
                ),
            )
        )
        .replace("7", "d" * 4)
        .replace("d", "00")
        .split("e")
        ####################################
        # "2,9999992444f42444f4099909999909f444f42,,900ff20ff0f02ff00f09ff09000f000600ff,90f00f2240006f000020900099900f9f0,9f006f0f000f600f80ff0990f00f2f0005,,,,f006000000f000f00000f800000f009,f90000ff000f02400099000f00f000520,20000f02ff0090ff0090000f090000600f05,9f00020f000f6000f0000008000f0f0000f,f02f0000000f0f000f0080f00000000f,90000f20000f600f00099000900f00024009,9009f000f00020000f08000f000f00020f02f,f000042000f0000005f000099000f204,ff00000000ff00000090000f0f00ff20,f0,909000000000204000000000ff0000000,f000000000f000ff000f000000002,f0000000000000000000000000f0f000009,f4000000000f000004f0000000000000,f00000f0f00000f0000000000000000000,f000000000f000000000f,ff0000000000000f000000000000f00009,9000000000002000000000000ff000000009,ff0000f00000000000000000000009,f000000000000f00000000000000f00000f,5f00000000008f0000000000020ff00000f,200000f0f000000000900000000009,f90000000000020000000000000000f00,f000000000000000f00f000000000000,f00000000000000000000000f0f000000,f02000ff000000f000000000000000000,6000000f000090000f000000000000000002,f0f00000000000000000000f0000000002,2000000ff00090000000000000000000000f2,20020000000f0000000009f00000000f,f000000ff0000000000000000000000002,f0000f00000000ff,f000000ff00000f0000000000000000000,9f00000000f020000000000000000000009,8000000000000fff005000000000f,ff0000f0000f00f000000000000000000,ff000000000000009,,f0f000000000000000000,f00000f0f000000000000000000,,f000000ff000002,ff000000002,,,f00000000fff0000000000000,,ff0000000f2,f0f000000000000000009,,f0ff000000000000000000,f00000000f0000002,,,f08,,f000000000000f00000000000000002,f0f000000000000000000000000000000,,f00000000000000000000000000000000009,f0000000000000ff0000000000002,,,f00000000000000000000000f00000000009,,f0f0000000000f0000000000000,ff00000000000000000000000000000000f,,f00000000000000000000ff,f0000000000ff0000000000000,,,f000000f0000000000000000f00000000009,,f2000ff0000000f00000f,9,,ff000000009,,,,f000000000000000000000ff009,,f0f000000000000000000000000000000,ff0000000f000000f,,f0000000000000000000000000000f,f00000000000000000000002,,,f00000f0f0000000000000,,f000000000000000000000000000000000002,ff0000ff0009,,f20000000000000000000,ff000000009,,,9fff00f00000000,,f0ff,f000000000000000000000000000f,,f0f0000000000000000000000000000002,ff0000000f000000f,,,ff0000000000000000000f000000000000f,,f0000000000f00f,f00000000000000000000000000ff,,fff000000000000000000000000000009,f0f0000000000000000002".split(
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
