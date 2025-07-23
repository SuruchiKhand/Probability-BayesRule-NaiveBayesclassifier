countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000,5439000,324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69,77,400,320,26]

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers
    
    total = sum(fishers)
    max_prob = 0
    most_likely_country = ""

    for country, count in zip(countries, fishers):
        prob = count/total
        if prob > max_prob:
            max_prob = prob
            most_likely_country = country
    return(most_likely_country, max_prob * 100)

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is he's from %s; probability %.2f%%" % (country, fraction))

main()
