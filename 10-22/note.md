# Note

## Introduction and suggestions

我负责的上机课资料会放在一个 Github 仓库: <https://github.com/royess/intro-computation-materials>

对内容的建议、勘误: [联系我](mailto:yanyx1999@pku.edu.cn). 更建议大家在 Github 上提 issue.

我有经验的 topics: 科学计算与画图, 多线程, 图形界面编程, 网络爬虫.

### 编程建议

- 最简单的 debug 方式: 插入 print 语句.
- 学会读懂报错内容.
- 多在 Baidu, Google, StackOverflow, Github... 搜索你遇到的问题.
- 查看文档. 文档经常是解决问题的最好帮手.

## Execises

### Game of Life

假如一个宇宙是 m x n 大小的棋盘, 每一个格子上有一个细胞. 这个宇宙按照回合的方式演化.

更新规则:

1. 如果一个细胞是活的, 而它周围有 2 个或 3 个活的细胞, 那么它下回合仍然是活的. 否则下回合死亡.
2. 如果一个细胞是死的, 而它周围有恰好 3 个活的细胞, 那么它下回合复活. 否则不变化.
3. 我们假设宇宙具有周期性边界条件. 比如位置在 (x,0) 的点在左边界上, 它左边相邻的细胞是右边界的 (x, n-1).

请补全 `game_of_life_blank.py` 中的 `update` 函数, 使得它可以按照上面的规则更新宇宙. 输出结果可以和 `result.txt` 进行比对.

(参考的答案代码是 `game_of_life_blank.py`. `game_of_life_visual.py` 是基于 matplotlib 的可视化脚本.)
