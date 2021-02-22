from manim import *


class Introduction(Scene):
    def construct(self):
        # title
        title_line = Text('Derivation of the Ideal Gas Law')
        # write the title
        self.play(Write(title_line))
        # fade out the title
        self.wait(1)
        self.play(FadeOut(title_line))

        # create equations
        ideal_gas_eos = TexMobject('PV', '=', 'n', 'RT')
        vdw_eos = Tex('$P=\\frac{RT}{V-b}-\\frac{a}{V^2}$')
        virial_eos = Tex('$\\frac{PV}{RT}=A+\\frac{B}{V}+\\frac{C}{V^2}+\\frac{D}{V^3}\\hdots$')

        # write the IG EOS
        self.play(Write(ideal_gas_eos))
        self.wait(1)

        # fade other 2 in
        ideal_gas_eos.generate_target()
        ideal_gas_eos.target.shift(2 * UP)
        virial_eos.shift(2 * DOWN)
        self.play(MoveToTarget(ideal_gas_eos), FadeIn(virial_eos), FadeIn(vdw_eos))
        self.wait(1)

        # fade other 2 out and restore position of IG EOS
        ideal_gas_eos.target.shift(2 * DOWN)
        self.play(MoveToTarget(ideal_gas_eos), FadeOut(vdw_eos), FadeOut(virial_eos))
        self.wait(1)

        # shift IG EOS
        shifted_ig_eos = TexMobject('{PV', '\\over', 'RT}', '=', 'n')
        self.play(*[
            Transform(
                ideal_gas_eos.get_part_by_tex(tex),
                shifted_ig_eos.get_part_by_tex(tex),
                run_time=2
            )
            for tex in ("PV", "RT", "=", "n")
        ], Write(shifted_ig_eos.get_part_by_tex("over")))
        self.wait(1)

        # reset IG EOS
        self.play(FadeOut(ideal_gas_eos), FadeOut(shifted_ig_eos.get_part_by_tex("over")))
        self.wait(1)

        self.wait(1)
