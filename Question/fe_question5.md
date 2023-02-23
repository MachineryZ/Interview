# Financial Engineering Question 5

Jane street

Person A has a 20-sided dice and person B has three 6-sided dice. They both roll their dice and whoever gets a bigger number/sum of numbers wins the game. Is it a fair game? Same game with one more player C who has a 20-sided dice. Is this new game fair? (all dice are fair; a 20-sided dice has number 1,2,…, 20 on each of its 20 sides)

我们看两个骰子的期望和方差：

1. E(dice20) = (1 + 20) / 2 = 10.5
2. Var(dice20) = E(x)**2 - E(x**2) = 399 / 12
3. E(3dice6) = (1 + 6) / 2 * 3 = 19.5
4. Var(3dice6) = 3 * 35/12 = 35 / 4

所以是否公平