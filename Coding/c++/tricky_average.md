实现 int64_t average(int64_t x, int64_t y); rounding to 0

例子 1和4的平均数是2.5，那要返回2

-1和-4返回-2



~~~C++
constexpr int average(int a, int b) {
  const int result = (a >> 1) + (b >> 1);
  const int two_odd = (a & b & 1);
  const int one_odd = (a ^ b) & 1;
  return result + (two_odd | one_odd & (result < 0));
}

~~~

