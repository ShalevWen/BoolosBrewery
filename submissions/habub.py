# ruff: noqa: F403, F405
import base64
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
        hex(int.from_bytes(base64.b85decode('(HXHeWJOBEL|{7*5t)$}#7sinkO`vl@+2y-4;lZNIS9;WS7Xva2}lUCG>8_p0!9oJ35Wn0VAAMfW-=^P_5_HDb(xF`hh~ah-QWKP@JZt?KH#{H>4aV37$hVn4&p$Wky)FFutHMJ?yRE2WWb>avB_Kk8J}UsG1Zt3?&x3uF;46x3jy=v-XiW02~sfm@PL5s5F^nPNeE#?3~wVev4IePLjr<C1<{Jg2|rj;?qJA;@ByUm<b7WO#3=;w?v=W-8c>2RO-mB)5c2LrfPtC_fv7Cr?O`by!8HXC!lV!G5lHUt+?pQl;`*fZK?DxzEUhAYF7EE`?&p}Jzr+8Xa5O*e5Cee;j1lhc?%wXd`2v7|8t(4y?%DJH?&aX_Irq}a9`5eyNWSju|L}aBg9z^K?(Xh`^6vj(+WH>v@-FV-1ODgvUHd@p?gW7D2nX)}@DL-?XQb|x5SsDs?(U&*P!rzn@MP}p%rowH`PP9yp6>4M?(X1$4K+gU?(P{{?(Xi|A%5=e?(X7m@I%h+ND}UPeC|rO?(Tr|?$!YSNRHtE1TkgD4({Q9ZQ}p+itg_2?gfbM|5DQ~?3YZiUheMh?&&{mWCQLMcnL-B48ZRDJJE?i?*Cct?(XjH|8m<A5A}}dD*YG*PUg1`<neCq?5h6lA%O0PEILZ=?(Xg<sn(9@1OPNr`4CtR=|lZ$U;%<6KrkwS?(XjH)-%7K{_f-Yo!`Ho`EKs+?(KQUtj7PM?(XjH-TyD{|Fl_l*nh6<MXlZW|L*QP`|j?CoZY`~?mGJ4_kaKX?(XZlo!_^w@&4}a?(O;i?(YAhKeFA^KaJNqF7D|@9`5epS*>6Hf1vK}?(XjH?%nzH?(R>T?(XjHb;;ki9`5e!|DNvZmaW~$>p=eQ?(XjH>RO%Gd9Lp6?(XjGBD?<X?(XjH?(d)d-^Kp!?(XlO{r|7-?z+qF?(W^(!&5=7?(XjI^Pcbfo!9^V=K0RxCwXDL`T5<?ukQKz-QEAC?jNk~?zmt7rQQ3l{JHM#?(XjH?%(-)q5kgYfBo8OzV7bs<(q!%xBXxL?(XjH#%kTxd;aFEKJMtojn*~>{_gJX?(Xj8_pSe_`}~$k-EjZz?(XjH*Z+R+@}1rJH~GKr?%hZS?(VAd+yDOV?(XjH>_mOqtM~sN?(XjH?&ZfVWk;hM?(P~t-O-Dx?(XjH?(Xh0U)^7S?(Sxv)vx~U?(XjH;QRg3fAY)u?(XjH?(SLn-}xoZ?(XgoVg')))[2:].replace("e", "20").split("d")
    )
    if dat
)
for dat, k in enumerate(
    (
        8717658111744,
        1855606874592557829860611,
        2598496598992762455,
        1109575324838066334200900180,
        33347319020328,
        10780073442596,
        30151021051137,
        755308995549597421057284,
        30253699873545,
        2230348200446401667279106,
        33321328261728,
        30574694315813,
        10015891405069,
        1860195863383588496077906,
        10634558059787,
        1864070364225449761748729,
        32633062864679,
        32730238072102,
        9537542740582,
        28915826857280,
        29053802944310,
        28984749510463,
        109997832,
        7542991387203002165,
    )
):
    for k_i in batched((bin(k)[:1:-1]), 9):
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
