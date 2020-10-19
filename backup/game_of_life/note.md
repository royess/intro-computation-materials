# Game of Life

假如一个宇宙是 m x n 大小的棋盘, 每一个格子上有一个细胞. 这个宇宙按照回合的方式演化, 被称之为生命游戏. 生命游戏由  John Horton Conway 在 1970 年提出.

![conway](conway.jpg)

更新规则:

1. 如果一个细胞是活的, 而它周围有 2 个或 3 个活的细胞, 那么它下回合仍然是活的. 否则下回合死亡.
2. 如果一个细胞是死的, 而它周围有恰好 3 个活的细胞, 那么它下回合复活. 否则不变化.
3. 我们假设宇宙具有周期性边界条件. 比如位置在 (a,0) 的点在左边界上, 它左边相邻的细胞是右边界的 (a, n-1).

![glidergun](glidergun.gif)

请补全 `game_of_life_blank.py` 中的 `update` 函数, 使得它可以按照上面的规则更新宇宙. 输出结果可以和 `result.txt` 进行比对.

参考答案: `game_of_life.py`. 而 `game_of_life_visual.py` 是基于 matplotlib 的可视化脚本.