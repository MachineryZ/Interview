## 牌力计算

1. royal stright flush皇家同花顺：4
2. straight flush：4 * (13 - 4 - 1) = 36 
3. four of a kind 炸弹（4条）：炸弹 * kickers = （13） * （4 * 12） = 624
4. full house 葫芦：(13 * 4C3) * （4C2 * 12）= 13 * 4 * 12 * 6 = 3744
5. Flush 同花（去掉同花顺）：4 * 13C5 - 40 = 5148 - 40 = 5108
6. straight 顺子（去掉同花顺）：(A ~ 5) 每个都可以选一个花色，然后去掉flush，10 * （4 * 4 * 4 * 4 * 4 - 4）=10200
7. set 三条：选一个点数 选两个 kicker （不能选一对的 kicker）：13 * 4C3 * (48C2 - 12 * 4C2) = 54912
8. two pair 两对：先选中两个点数，然后每个点数选两张牌出来 再在剩下的点数里选出来一个 13C2 * 4C2 * 4C2 * 11C1 * 4C1 = 123552
9. pair 一对：选一个点数，然后再在剩下的里面选出来3个点数：13C1 * 4C2 * 12C3 * 4C1 * 4C1 * 4C1 = 1098240
10. 剩下的，减少一下就好了

---

底池计算：

当前有 100 的底池，转牌圈，假设你的 outs 是 x，那么你应该下注多少抢下这个底池？

先计算胜率的估计

总共有 52张牌，翻牌是3，手牌2，总共5张牌，剩余47张牌，发出来outs 的概率是 x/47，那么赢得底池的概率就是 x/47。那么假设下注是t，赢得底池的概率是 x/47 能赢 100 ，期望是 (100 + t对手的筹码)* x/47；失败则损失 t，期望是 -t * (1 - x/47)

以outs = 10为例，(100 + t) * 10/47 = t * (1 - 10/47)，t = 37，这只是转牌圈的胜率与下注的关系

---

outs 的计算



----

实际的计算



