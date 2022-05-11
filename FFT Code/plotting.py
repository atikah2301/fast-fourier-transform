from shared_imports import *

if __name__ == '__main__':

    k, n, t_naive, t_fft = np.transpose(np.loadtxt('Output/test_timing_naive_015624232811.txt',
                                    unpack=True,
                                    delimiter=','))
    # t_naive_expected = [t_naive[0] * 4] + [t_naive[i] * 4 for i in range(len(t_naive[:-1]))]
    # t_fft_expected = [t_fft[0] * 2] + [t_fft[i] * 2 for i in range(len(t_fft[:-1]))]
    # t_naive_expected = [(n[i] ** 2) / (10 ** 6.7) for i in range(len(n))]
    # t_fft_expected = [(n[i] ** 0.5) / (10 ** 1) for i in range(len(n))]

    # plt.plot(n, t_naive_expected, label='Expected Naive', color="red")
    plt.plot(n, t_naive, label=f'Naive Multiplication',
        color='seagreen', marker='o', markersize='8',
        markerfacecolor='mediumseagreen', markeredgecolor='seagreen')

    # plt.plot(n, t_fft_expected, label="Expected FFT", color="orange")
    plt.plot(n, t_fft, label=f'FFT Multiplication',
        color='darkorchid', marker='o', markersize='8',
        markerfacecolor='mediumorchid', markeredgecolor='darkorchid')


    ### Linear Regression Attempt
    # fit_naive = np.polyfit(np.log(n), np.log(t_naive), 1)
    # fit_fft = np.polyfit(np.log(n[2:]), np.log(t_fft[2:]), 1)
    # [1.92373537 - 14.8865877]
    # [1.01709443 - 10.95497214]
    # view the output of the model
    # print(fit_naive)
    # print(fit_fft)
    # plt.plot(n, [fit_naive[1] + fit_naive[0] * i for i in n])
    # plt.plot(n, [fit_fft[1] + fit_fft[0] * i for i in n])
    # plt.plot(n, [10 ** fit_naive[1] * i ** fit_naive[0] for i in n], label="naive regression")
    # plt.plot(n, [10 ** fit_fft[1] * i ** fit_fft[0] for i in n], label="fft regression")

    plt.grid(linestyle='--')
    plt.legend()
    plt.title("Multiplication Runtimes: FFT vs Naive")
    plt.xlabel('Input Size log(n)')
    plt.ylabel('Runtime log(t)')
    plt.xscale('log', base=2)
    plt.yscale('log', base=2)
    plt.show()