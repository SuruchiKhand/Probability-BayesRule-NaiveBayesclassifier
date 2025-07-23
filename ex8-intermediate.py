def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800,11611,1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    for country, fisher_count in zip(countries, fishers):
        probability = fisher_count/total_fishers *100
        print("%s %.2f%%" %(country, probability))
main()