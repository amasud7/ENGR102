# specific model for learning.
rate_initial = 0.1
rate_constant = 0.2
time_constant = 15
time_fatigue = 60
time_stop = 90

# Read time from user
study_time = float(input("How long will you study? "))

# Calculate amount of learned
if (study_time >= 0) and (study_time <= time_constant):
    # warmup period
    end_learn_rate = rate_initial + (rate_constant - rate_initial) / time_constant * study_time
    concepts_learned = study_time * (rate_initial + end_learn_rate) / 2
elif (study_time > time_constant) and (study_time <= time_fatigue):
    # constants period
    concepts_learned = 2.25   # concepts learned during warmup
    concepts_learned += rate_constant * (study_time - time_constant)
elif (study_time > time_fatigue) and (study_time <= time_stop):
    # fatigue period
    concepts_learned = 11.25    # concepts learned through cosntant period
    end_learn_rate = (study_time - time_fatigue) / (time_stop - time_fatigue)
    concepts_learned += (study_time - time_fatigue) * (rate_constant * end_learn_rate) / 2
elif (study_time > time_stop):
    # post fatigue: nothing more to learn
    concepts_learned = 14.25
else:
    # negative tim - nothing can be learned!
    concepts_learned = 0

# output result to user
print("You learned", concepts_learned, "concepts in that time. ")