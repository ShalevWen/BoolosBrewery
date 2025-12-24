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
        hex(
            int.from_bytes(
                base64.b85decode(
                    "4H26YW<*r1L`DO#0U4PQJVeAT*#Md^FCs##An~91laP$YWi~yOfQutYfoo9g6bXnR8DQ9AW-=^P_5_HDHJOYGgJz0d-QVzU1d;<H10W&`i0On~7~){!K$($Qn~1PNQqAhhEH+FE5Q`j@z!91D9Ah1r2ZjOz6zm`i0rMa|AR^%)l_C$H2nY@kBhf^Vh7>@?@-s^q5eNh@AS6It7_5Mk^@T1V$c6F&q~ZiUUjf7^1oG)yt01KaA|Opm65$UnLx6#j2!W_9-q{(!H3bmDqz~Z~htYESr1e1r4wA~#vUlT{qrb!doisn;AUF`1!58h~3;*DN8h77yE+9Gc+863bx6l6r$=D!=euMJw_8p<`_aG2I<M~~*4j>`~fFL3W1MmL<0zFzzl@OZoexWc>6W$>3WPHOuGx^vP`FC)E4K+f38CrhTcj9mGL(b7IIy~g7H-Pi)U=jp~;UEMtWy1#(_R<3X^@?`|i0}0+F3D8O1$XH`ZDa%CQ-G9S48ZTRy+H5vmwx{;+Yt}-j)Je%PHQma@n_1f?HCS-EILYeBdOTv1Ryk0`4CtRlt0>F0fGWRFe-s}+xh=<`kmSTmUr31tj7O$Al?2T|Fl^))B5a1t=;!K`*=Cc-*4lutv~<w>$;uOukrVN_y3|lvfb18-8UeVVSW{w-#>SLAl>=&bor-qT%8x}|Cgz1-Q0o;K=*g0sogoJciX>re)<31#rJ=o{rdO1%YNP5!&5=0fAgOIx!wM6oZurlVZEK-ukW9o-QT6*`p39m|E1mk%a?cUJE8Y8|J|#1S+nc2{a^og#%kT${%XT`#*Nb;Z+CuQI^X)AzsY2s-*@f*KL07**){pUebaicJ@<FSL*2h$@ppB@Ejlr`8b96Js&{@fU)}TfW}n}8aQpqz%lUV8pPiCiejpHH"
                )
            )
        )[2:]
        .replace("7", "ee")
        .replace("e", "2020")
        .split("d")
        # ",119b13664454ac444603b1011999113c44c42,,9009a2f2f2242ab20f19ff993908cc665363,94808b2348816b502020c140988201960,86266322c54f604888935998c0a83668a5,,,,ff06f049203220320220b8820209845,18202026020202409991599b88b04252c,2020aca2c364c0a108b1c95c01199f61c631,98020202020860203142020c200b01f3203,2022202012095220f9f0808020201023,14490861440c6f2334b18110804302024405,18ac8093f5852202020c885f201a420202043,5f01c42904f2202095bab20a50822204,4b12202010f22020438081920881a82c,2020,919c1350510c2a40f2020114820202020,1202020202faa4f541040202092ca,3b220202020202020202020398a3bfc3ff9,343f2020120381098c11202020202020,202020bff20200801a2020202020202020,f202020205220202039f3,a1202020202020a48b20202020cfff03c9,82082020202020202020202083f22020ff61,a12020ff2020202020103f20203f95,b40202020220480202208032020fff01023,5a4202095109af1202020202020a1305013,202020f06420202020cc33202033f9,813f92020202020202020202020200810,3542202020202020195a202020202020,52020202020202020202026ff043c2020,1220203a3c20204ab32020202080f32020,601204882020120043165c302020202013f6,202fff58a202020202020202005882020ff52,22020c954cb052020202020202020202093f6,640320201538094520200cc02020fb3b,402020ff5920202020202020202020ff32,b110ff58202082af,5420206b3020204f1620202020caaf2020,1802020882c3a4a202020202020202023a9,82020804203452f9105802020943f,a6001820240302a812020202020202020,bf9ff202020203fa9,,9ff962020202020202020,9c3acc6ff202020202020202020,,f202020ffb45936,3fa2020c45a,,,f202020203bfb20202020839c,,f6f20203afa,3ffff202020202020bba9,,3aff1f2020202020202020,f20202020ffa23fb2,,,3f8,,320202020209461202020202020159a,f3f202020202020202020202020202020,,f9f4202020204f9a202020202020202035c9,1202020202020cff920202020a96a,,,c820b40f202020202020202020202020a5a9,,39a202020202020202020202020,bbf2020202020202020202020202020f9ff,,c5f2020202020202020f9ff,faf20202020bacb202020202020,,,cc35341a2020202020202020ff392020ffb9,,f20206f9c20200233961b,9,,faf2020f9f9,,,,fa520201fac20202020b85fffa5,,ffcb92020202020202020202020202020,3ba1f2020202033ff,,ab202020202020202059b32020bb3f,5fff2020202020202020c66a,,,bf20206ac3202020208c68,,3206f20202020202020202020202020205f3a,ffa9fbfc9649,,f20202020202020202020,ff32020ff29,,,935f9bf20202020,,320202020aaf3,f202020202020202020202020c443,,bf5ff12020202020202020202020205c32,3a31b202020201a3f,,,baa2020202020202020202020202020335f,,f3f20202020669f,f2020202020202020202020200fbf,,2cbf920202020202020202020202059f9,925c202020202020201062".split(
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
