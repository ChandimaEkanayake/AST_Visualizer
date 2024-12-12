digraph AST {
	node [fontname=Arial shape=box]
	node0 [label=Module]
	node1 [label=FunctionDef]
	node0 -> node1
	node2 [label=arguments]
	node1 -> node2
	node3 [label=arg]
	node2 -> node3
	node4 [label=arg]
	node2 -> node4
	node5 [label=Return]
	node1 -> node5
	node6 [label=BinOp]
	node5 -> node6
	node7 [label=Name]
	node6 -> node7
	node8 [label=Load]
	node7 -> node8
	node9 [label=Add]
	node6 -> node9
	node10 [label=Name]
	node6 -> node10
	node11 [label=Load]
	node10 -> node11
	node12 [label=FunctionDef]
	node0 -> node12
	node13 [label=arguments]
	node12 -> node13
	node14 [label=arg]
	node13 -> node14
	node15 [label=arg]
	node13 -> node15
	node16 [label=Return]
	node12 -> node16
	node17 [label=BinOp]
	node16 -> node17
	node18 [label=Name]
	node17 -> node18
	node19 [label=Load]
	node18 -> node19
	node20 [label=Sub]
	node17 -> node20
	node21 [label=Name]
	node17 -> node21
	node22 [label=Load]
	node21 -> node22
	node23 [label=FunctionDef]
	node0 -> node23
	node24 [label=arguments]
	node23 -> node24
	node25 [label=arg]
	node24 -> node25
	node26 [label=arg]
	node24 -> node26
	node27 [label=arg]
	node24 -> node27
	node28 [label=If]
	node23 -> node28
	node29 [label=Compare]
	node28 -> node29
	node30 [label=Name]
	node29 -> node30
	node31 [label=Load]
	node30 -> node31
	node32 [label=Eq]
	node29 -> node32
	node33 [label=Constant]
	node29 -> node33
	node34 [label=Return]
	node28 -> node34
	node35 [label=Call]
	node34 -> node35
	node36 [label=Name]
	node35 -> node36
	node37 [label=Load]
	node36 -> node37
	node38 [label=Name]
	node35 -> node38
	node39 [label=Load]
	node38 -> node39
	node40 [label=Name]
	node35 -> node40
	node41 [label=Load]
	node40 -> node41
	node42 [label=If]
	node28 -> node42
	node43 [label=Compare]
	node42 -> node43
	node44 [label=Name]
	node43 -> node44
	node45 [label=Load]
	node44 -> node45
	node46 [label=Eq]
	node43 -> node46
	node47 [label=Constant]
	node43 -> node47
	node48 [label=Return]
	node42 -> node48
	node49 [label=Call]
	node48 -> node49
	node50 [label=Name]
	node49 -> node50
	node51 [label=Load]
	node50 -> node51
	node52 [label=Name]
	node49 -> node52
	node53 [label=Load]
	node52 -> node53
	node54 [label=Name]
	node49 -> node54
	node55 [label=Load]
	node54 -> node55
	node56 [label=Return]
	node42 -> node56
	node57 [label=Constant]
	node56 -> node57
	node58 [label=Assign]
	node0 -> node58
	node59 [label=Name]
	node58 -> node59
	node60 [label=Store]
	node59 -> node60
	node61 [label=Call]
	node58 -> node61
	node62 [label=Name]
	node61 -> node62
	node63 [label=Load]
	node62 -> node63
	node64 [label=Constant]
	node61 -> node64
	node65 [label=Constant]
	node61 -> node65
	node66 [label=Constant]
	node61 -> node66
	node67 [label=Expr]
	node0 -> node67
	node68 [label=Call]
	node67 -> node68
	node69 [label=Name]
	node68 -> node69
	node70 [label=Load]
	node69 -> node70
	node71 [label=Name]
	node68 -> node71
	node72 [label=Load]
	node71 -> node72
}
