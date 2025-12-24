# ruff: noqa: F403, F405
from base64 import b85decode
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
        hex(
            int.from_bytes(
                b85decode(
                    '(HXHeWJOBEL|{7*5t)$_#7sinkO{6YE-Jq9pZT5$&TeDbNb4g`7PSuS;FyjXVAx`2e_%+6lUbO+s6L8a-QVzMGUMXwi0+<U815zx;!c?!n~1(8EZ*wMEH+FE9=?^p9_Ae3*?@kA4&?663jyvu;x6IoQtzICfO0();Ev$Nae?UL4kYE#?11lHC&-2V8b?Fb{=_a%F6mpV>Ruw`)VJ?0<T!Zhj^6E&p5Sy3bcgL1;{H!w1P98~cXy7y@0~Pp<ALbG7kzvG?g;94?%#e=e)HNFdPukI|M2P9=y!gD^6vf}q3-{F;RE-T+kP%c4ld*F_dQxp>F%!=dLH3De+EbF$M2niH+Oyr5YtpAaq4%~cYg2iN6{|hr%Hb4<L=gY?icO{?)Kg<|5&Gf;8*1>F6@;|<#&GXZDa#;fR_xwbG<<B|5<l_<1Ml8^^WK&{Z#I2bmo4}{_PkCEIy}qsn~SxQu*b1@7iGK?gIj+ciaB=?y23M`DcFZp6u^;ecylkPBzo}?!;Q%-+nv$e(BBMZ|*w!)Bktwson4K_kQj7?{eMK_}w?|lwo%st@HPHcisL+<mz{Pofmxnm+I=>+>XBYcYdkeIj47hyZ3i@|J}!T@BRAs>#VnZ-N&bX@9BG;-|la4d)eLk{_mfi-QT6|AFO`m|K;8P%a?b4?K|&&@BP}he&yqH{a<%}YTeuS!+ws9)8_Yge&zG6|EcfJN!|B%?f*9^-Ptw%_wCbu?>+Z-eB<4}U-5T$<1ISte&hY!x~F${U)}Tf=I`HkcMreaEVp-l@12rdckW^'
                )
            )
        )[2:]
        .replace("7", "eee")
        .replace("e", "20")
        .split("d")
        # ",119b13664454ac444603b1011999113c44c42,,9009a202f2202ab20f19ff992008c2062063,94820b2342016b502020c200988201960,86266202020f604888935998c0a83208a5,,,,ff062020203220320220b8820209205,18202026020202420991209b88b20252c,2020aca2c364c0a120b2095c01202061c201,98020202020860202042020c200b0120203,2022202012095220f920808020202023,14200820200c620202018120820302024205,120c8020f5202202020c885f201a420202043,5f20c42204f2202095bab20a52022204,4b20202020f22020438202020820a820,2020,9192020020202040f2020204820202020,1202020202f204f520040202020ca,3202020202020202020202020820b2020f9,34202020120381208c11202020202020,202020bff20200820a2020202020202020,f202020205220202020f3,a1202020202020a48b20202020cfff0209,82082020202020202020202083f22020f201,a12020ff2020202020103f20202095,b20202020220480202202032020f2020203,5a4202092020af1202020202020a1202013,202020f06420202020cc20202020f9,813202020202020202020202020200810,3542202020202020120a202020202020,52020202020202020202020ff04202020,1220203a2020204a202020202082032020,6202020820201202020202002020202020f6,202fff58a2020202020202020052020202052,22020c954c2052020202020202020202020f6,640320202038092020200cc02020203b,402020ff59202020202020202020202032,b120ff58202082af,5420206b202020420620202020c20f2020,1802020202c320a202020202020202020a9,82020204202052f9205202020920f,a6020820200302a202020202020202020,bf20f2020202020a9,,9ff962020202020202020,92020c20f202020202020202020,,f202020ffb42036,3fa2020c45a,,,f202020203bfb20202020209c,,f6f20203afa,3ff2020202020202020a9,,20ff1f2020202020202020,f20202020f2020202,,,3f8,,320202020209461202020202020120a,f3f202020202020202020202020202020,,f20420202020420a202020202020202020c9,1202020202020cff920202020a20a,,,c820b20f20202020202020202020202020a9,,39a202020202020202020202020,bbf202020202020202020202020202020ff,,c20202020202020202020ff,faf20202020bacb202020202020,,,c202020a2020202020202020f209202020b9,,f20206f2020200202020b,9,,faf2020f9f9,,,,fa520201fac20202020205ff205,,ffcb92020202020202020202020202020,3b20f2020202020ff,,ab202020202020202052032020203f,5f202020202020202020206a,,,bf202020c3202020208208,,3206f20202020202020202020202020205f3a,ffa920fc2049,,f20202020202020202020,ff320202029,,,935f20f20202020,,32020202020f3,f202020202020202020202020c203,,bf5ff12020202020202020202020202032,3a20b20202020203f,,,baa2020202020202020202020202020205f,,f3f20202020620f,f2020202020202020202020200fbf,,2cb2020202020202020202020202020f9,925c202020202020202062".split(
        #     ","
        # )
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
