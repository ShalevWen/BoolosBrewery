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
                        b"B~QO=R6!8_vid?U9&Z#uvG91ERZJ5U31Ubkq6Yj2a)@9Twz7S}CN{ydi_N7<=_OWauSgqQY#s{Bak255-Qk*-1m=x<vDumVcD^4ozW4pnyNwqo8{O5Lx4!mnpS)ZTJ(?2pGSh{&3L4HsC(kim!JXq`h`sH({rn@|5~xd`^rFZ5Y~dgTowo_H=a#d$qad?}FSr55o4hD=su(JcS~~Xu+}VSf(eVI79MugkTQCzZER4pCY1t*rZDX5Y*0M2vAT?z>y{Xdmre04r+3^9Wc&(%Q+D@WQbDp$Z@rr8XLQsYbp8C&Z`z!8oTWmB$WW^ymp(ys;QQhB#F^;5jSbCeqN-WuC(=7_jVohh3rG46p_hCHek^)i{eJVAgLGlsoAb*egu8g)=DluotLy>t)TU}$Z+m@z=`k!az?^$C7ZHuw+Qq}rfEpz6Y!?J|9Tr28F^@ug6DO#%MqYQ$m*r1j!|ERwRJX;u96XJQ0(hpR;&7=3|NU2rYu0XC8o_s^PR{SUd8q;+)Btb9e$0B7wO_QL%Li*k0EEK0n<O*$~ubQMW2**U#mGEU$CQi|o9HR8YzCwbqM(@x>@)aKbr-l@bswTOi5f2TsZ2g`%^A7"
                    ),
                    wbits=-9,
                )
            )
        )[2:]
        .replace("d", "77")
        .replace("7", "0" * 4)
        .split("e")
        ####################################
        # ",119b136644f4ac44f603b1011999013c44c42,,900ff20ff0f02ff00ff9ff09200fc00600ff,94800f2340016b000020c0009880019f0,8200620f000f600f88fff990f0ff3f08a5,,,,ff06000000f000f00000f800000f005,f80000ff000f02400091000b00f000520,2020fff2ff00c0ff00b009ff010000600f01,9800020f000f60002000000c000b0f0000f,f02f0000000f0f00ff0080800000000f,1f000f20000f600f00018000800f00024005,100cf000f00020000f0c000f000f00020f04f,f000042000f0000005b0000a5000f204,ff00000000ff00000380000f0f00ff20,f0,909000000000204000000000ff0000000,f000000000f00fff000f00000000a,30000000000000000000000008f0f000009,34000000000300000cf0000000000000,f020f0f0f00000f0000000000000000000,f000000000f000000000f,ff0000000000000f80000000000ff00009,8000000000002020000000000ff000000001,af0000f00000000000000000000005,f000000000000f00000000000000f00000f,5f0000000000af0000000000020af00000f,200000f0f000000000cc0000000009,f10000000000020000000000000000f00,f000000000000000f00f000000000000,f00000000000000000000000f0f000000,f02000ff000000f000000000080000000,6000000f000010000f0000000000000000f6,f0f00000000000000000000f0000000002,2020f0fff00050000000000000000000000f6,600200000008000000000cf00000000f,f000000ff0000000000000000000000002,20000f00000000af,f000000ff00000f00000000000c0000000,1f00000000f020000000000000000000009,80000000000002ff005000000000f,af0000f0000f00f000000000000000000,ff0000000000000f9,,fff000000000000000000,ff0000f0f000000000000000000,,f000000ff000006,ff00000000a,,,f00000000fff0000000000000,,ff000000ffa,3ff0000000000000000f9,,f0ff000000000000000000,f00000000f0000002,,,ff8,,f000000000000f0000000000000000a,fff000000000000000000000000000000,,f00000000000000000000000000000000001,f000000000000fff000000000000a,,,f00000000000000000000000f00000000009,,39a0000000000f0000000000000,ff00000000000000000000000000000000f,,f00000000000000000000ff,f0000000000ff0000000000000,,,f000000f0000000000000000f00000000009,,f2000ff0000000f00000f,9,,ff000000009,,,,f000000000000000000005ff005,,20c000000000000000000000000000000,ff0000000f00000ff,,f0000000000000000000000000000f,f0000000000000000000000a,,,b00000f0f0000000000000,,f0000000000000000000000000000000000fa,ffff00ff00f9,,f20000000000000000000,ff000000009,,,9fff00f00000000,,f00000000f0ff,f000000000000000000000000000f,,f0f0000000000000000000000000000002,ff0000000f00000ff,,,ff0000000000000000000f000000000000f,,f0000000000f00f,f00000000000000000000000000ff,,fff000000000000000000000000000009,90f0000000000000000002".split(
        #     ","
        # )
    )
    if dat
)
for dat, k in enumerate(
    decompress(
        b85decode(
            b"6_3ji03irN8}h(kDF+1lFJavi1IZ+h-Ice42Vmhj17TZhYq(@n0WT7mwB{%<Hr<O|3*UvBQ?ay|C{z}<ifoKbI?Hc$Z_1)4q+OIYF2Ln8XgG)U#*quD@H-Aq!N~+)SVz(lf$jQnCvu>dF3sM<VUP4Nr{CmFx*RWH7(3K^!P_mj<CX|%98p>x7Ydpc@;M&hmT``W@N?7V?~Izj&Q1F*S3KBK$<~P*kEp_IVaVO(<|>aN9$tC)=3mi!Jn0V4vePzj-i$^|zJyT2`T+"
        ),
        wbits=-15,
    )
    .decode()
    .split(",")
    ####################################
    # (
    #     8717658111744,
    #     1855606874592557829860611,
    #     2598496598992762455,
    #     1109575324838066334200900180,
    #     33347319020328,
    #     10780073442596,
    #     30151021051137,
    #     755308995549597421057284,
    #     30253699873545,
    #     2230348200446401667279106,
    #     33321328261728,
    #     30574694315813,
    #     10015891405069,
    #     1860195863383588496077906,
    #     10634558059787,
    #     1864070364225449761748729,
    #     32633062864679,
    #     32730238072102,
    #     9537542740582,
    #     28915826857280,
    #     29053802944310,
    #     28984749510463,
    #     109997832,
    #     7542991387203002165,
    # )
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
