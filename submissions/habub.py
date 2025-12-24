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
        ",119b13664454ac444603b1011999117c44c42,,9009a2f2f2242ab00f19ff993908cc675763,94808b2348816b502460c140988001960,86266322c54f604888975998c0a87668a5,,,,ff06f049203220320200b8820209845,18242426020202409991599b88b04252c,2020aca2c364c0a108b1c95c01199f61c631,98020202020860003142020c240b01f3203,2022202010095230f9f0808020201023,14490861440c6f2334b18110804302824405,18ac8093f5852202060c885f001a420202047,5f01c42904f2202095bab21a50822204,4b12202010f220204380819a0881a82c,2020,919c1350510c2a40f2020114820202020,1202020202faa4f541040202092ca,7b220202020202020202020798a3bfc3ff9,343f2020100381098c11202020202020,202020bff90280801a2020202020202020,f202020205200202039f7,a1202020202020a48b20202020cfff07c9,83082020202020202020202083f22020ff61,a12020ff2220202020103f20207f95,b40202020200480202008072020fff01023,7a4202095109af1202020202020a1705013,202020f06420202020cc33202077f9,813f92020202020202020202020200810,3542202020202020195a202020202020,72020202020202020202026ff043c2020,1220207a7c20204ab72020202080f32020,601004882020100043165c702020202017f6,202fff58a202020202020202005882020ff52,22020c974cb052020202020202020202093f6,640320201578094520200cc02020fb3b,402020ff5920202020202020202020ff72,b110ff58202082af,5420206b7020204f1620202020caaf2020,1802020882c3a4a202020202020202027a9,82020804003452f9105802020943f,a6001822240302a812020202020202020,bf9ff202020203fa9,,9ff962020202020202020,9c7acc6ffa22020202020202020,,f2f2020ffb45976,7fa2020c45a,,,f202020203bfb20202020879c,,f6f20203afa,7ffff202020202020bba9,,7aff1f2020202020202020,f20202020ffa23fb2,,,3f8,,3a2202020209461202020202020159a,f7fa02020202020202020202020202020,,f9f4202020204f9a202020202020202075c9,1202020202020cff920202020a96a,,,c820b40f202020202020202020202020a5a9,,79a202020202020202020202020,bbf2020202020202020202020202020f9ff,,c5f2020202020202020f9ff,faf20202020bacb202020202020,,,cc35341a2020202020202020ff392020ffb9,,f20206f9c20200277961b,9,,faf2020f9f9,,,,fa520201fac20202020b85fffa5,,ffcb92020202020202020202020202020,7ba1f2020202077ff,,ab202020202020202059b72020bb7f,5fff2020202020202020c66a,,,bf20206ac3202020208c68,,3606f20202020202020202020202020205f7a,ffa9fbfc9649,,f20202020202020202020,ff72020ff29,,,937f9bf20202020,,720202020aaf3,f202020202020202020202020c447,,bf7ff12020202020202020202020205c72,7a31b202020201a3f,,,baa0000002020202020202020202020335f,,f7f20202020669f,f2020202020202020202020200fbf,,2cbf920202020202020202020202059f9,925c000000002020201062".split(
            ","
        )
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
