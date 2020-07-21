# int fib(int N) {
# if (N < 1) return 0;
# // 备忘录全初始化为 0
# vector<int> memo(N + 1, 0);
# // 初始化最简情况
# return helper(memo, N);
# }
#
# int helper(vector<int>& memo, int n) {
# // base case
# if (n == 1 || n == 2) return 1;
# // 已经计算过
# if (memo[n] != 0) return memo[n];
# memo[n] = helper(memo, n - 1) +
# helper(memo, n - 2);
# return memo[n];
# }