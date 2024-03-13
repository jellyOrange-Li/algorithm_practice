
if __name__ == "__main__":
    dp = [0] * 20
    dp[2] = 1
    for i in range(3,20):
        for j in range(1,i):
            dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
    print(dp)


