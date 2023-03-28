def progression_func(n_progression, progression_summ):
    if n_progression == 1:
        return progression_summ+1

    progression_summ += n_progression
    n_progression -= 1
    return progression_func(n_progression, progression_summ)


n_progression = int(input("Введите n-ый член прогрессии: "))
progression_summ = 0

print(f"Множество 1+2+...+n = "
      f"{progression_func(n_progression, progression_summ)}")

print(f"множество n(n+1)/2 = {n_progression * (n_progression + 1) // 2}")

if progression_func(n_progression, progression_summ) == \
        n_progression * (n_progression + 1) // 2:
    print("Выражение 1+2+...+n = n(n+1)/2 является верным!!")
