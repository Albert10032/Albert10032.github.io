from manim import *

class DemonstrateAGraphVertexColouring(Scene):
    def construct(self):
        V = [1, 2, 3, 4, 5, 6, 7, 8]
        E = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,1),
             (1,4),(3,5),(4,7),(4,8)]
        G1 = Graph(V,E, layout="kamada_kawai")
        self.play(Create(G1))
        self.wait()
        self.play(G1.animate.move_to([-3,0,0]))
        t1 = MathTex(r"\chi(G) \le \Delta(G) + 1\\").move_to([2,1,0])
        t2 = MathTex(r"&\text{In this case}\\ &\Rightarrow \chi(G) \le 5+1 = 6").move_to([2,0,0])
        t3 = MathTex(r"&\text{In actuality } \chi(G) = 3").move_to([2,-1.1,0])
        self.play(Write(t1))
        self.play(Write(t2))

        G2 = Graph(V,E, layout="kamada_kawai",
                    vertex_config={1: {"fill_color": RED}, 3: {"fill_color": RED}, 7: {"fill_color": RED}, 
                                   2: {"fill_color": GREEN}, 4: {"fill_color": GREEN}, 6: {"fill_color": GREEN}, 
                                   5: {"fill_color": BLUE}, 8: {"fill_color": BLUE},},
                    ).move_to([-3,0,0])
        self.play(Create(G2))
        self.wait()
        self.play(Write(t3))
        self.wait()

class DemonstrateAGraphEdgeColouring(Scene):
    def construct(self):
        V = [1, 2, 3, 4, 5, 6, 7, 8]
        E = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,1),
             (1,4),(3,5),(4,7),(4,8)]
        G1 = Graph(V,E, layout="kamada_kawai")
        self.play(Create(G1))
        self.wait()

        graphpos_1 = [-3.2,0,0]

        self.play(G1.animate.move_to(graphpos_1))
        self.wait()

        t1 = MathTex(r"\chi'(G) = \Delta(G) \text{ or } \Delta(G)+1").move_to([2.1,1,0])
        t2 = MathTex(r"\text{Here } \chi'(G) = \Delta(G) = 5").move_to([2.1,0,0])

        G2 = Graph(V,E, layout="kamada_kawai",
                   edge_config={
                        # From central vertex 
                        (1,4): {"stroke_color": RED},
                        (3,4): {"stroke_color": GREEN},
                        (4,5): {"stroke_color": BLUE},
                        (4,7): {"stroke_color": YELLOW},
                        (4,8): {"stroke_color": PINK},
                        # Others
                        (3,5): {"stroke_color": PINK},
                        (7,8): {"stroke_color": RED},
                        (8,1): {"stroke_color": YELLOW},
                        (2,3): {"stroke_color": RED},
                        (1,2): {"stroke_color": GREEN},
                        (5,6): {"stroke_color": YELLOW},
                        (6,7): {"stroke_color": BLUE},
                    }
                   ).move_to(graphpos_1)
        self.play(Create(G2))
        
        self.play(Write(t1))
        self.play(Write(t2))

        self.wait()
        self.wait(1)


class DemonstrateAGraphTotalColouring(Scene):
    def construct(self):
        V = [1, 2, 3, 4, 5, 6, 7, 8]
        E = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,1),
             (1,4),(3,5),(4,7),(4,8)]
        G1 = Graph(V,E, layout="kamada_kawai")
        self.play(Create(G1))
        self.wait()

        graphpos1 = [-3.2,0,0]

        self.play(G1.animate.move_to(graphpos1))
        self.wait()

        t1 = MathTex(r"\text{Conj: } \chi''(G) = &\Delta(G) + 1 \text{ or }\\ &\Delta(G) + 2").move_to([2.1,1,0])
        t2 = MathTex(r"\text{Here we generated a}\\ \text{ total colouring with }\\ 7 = \Delta(G)+2 \text{ colours.}").move_to([2.1,-1,0])

        G2 = Graph(V,E, layout="kamada_kawai",
                   edge_config={
                        # From central vertex 
                        (1,4): {"stroke_color": RED},
                        (3,4): {"stroke_color": GREEN},
                        (4,5): {"stroke_color": BLUE},
                        (4,7): {"stroke_color": YELLOW},
                        (4,8): {"stroke_color": PINK},
                        # Others
                        (3,5): {"stroke_color": PINK},
                        (7,8): {"stroke_color": RED},
                        (8,1): {"stroke_color": YELLOW},
                        (2,3): {"stroke_color": RED},
                        (1,2): {"stroke_color": GREEN},
                        (5,6): {"stroke_color": YELLOW},
                        (6,7): {"stroke_color": BLUE},
                    },
                   ).move_to(graphpos1)
        
        G3 = Graph(V,E, layout="kamada_kawai",
                   edge_config={
                        # From central vertex 
                        (1,4): {"stroke_color": RED},
                        (3,4): {"stroke_color": GREEN},
                        (4,5): {"stroke_color": BLUE},
                        (4,7): {"stroke_color": YELLOW},
                        (4,8): {"stroke_color": PINK},
                        # Others
                        (3,5): {"stroke_color": PINK},
                        (7,8): {"stroke_color": RED},
                        (8,1): {"stroke_color": YELLOW},
                        (2,3): {"stroke_color": RED},
                        (1,2): {"stroke_color": GREEN},
                        (5,6): {"stroke_color": YELLOW},
                        (6,7): {"stroke_color": BLUE},
                    },                   
                    vertex_config={
                        1: {"fill_color": PINK},
                        2: {"fill_color": YELLOW},
                        3: {"fill_color": BLUE},
                        4: {"fill_color": WHITE},
                        5: {"fill_color": GREEN},
                        6: {"fill_color": PINK},
                        7: {"fill_color": GREEN},
                        8: {"fill_color": BLUE},
                    }
                   ).move_to(graphpos1)

        self.play(Create(G2))
        self.wait()
        self.play(Create(G3))
        self.wait()
        self.play(Write(t1))
        self.wait()
        self.play(Write(t2))
        self.wait()