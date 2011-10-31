#!/usr/bin/python
import sys
sys.path.insert(0, "..")
from mcda.types import criterion, criteria, alternative, alternatives, profile, threshold_old, alternative_performances, performance_table, threshold, thresholds, constant, alternative_affectation, alternatives_affectations

# Criteria
prix = criterion('prix', 'prix', False, -1, 25)
transport = criterion('transport', 'transport', False, -1, 45)
envir = criterion('envir', 'environment', False, 1, 10)
residents = criterion('residents', 'residents', False, 1, 12)
competition = criterion('competition', 'competition', False, 1, 8)
c = criteria([ prix, transport, envir, residents, competition ])

# Actions
a1 = alternative('a1', 'a1')
a2 = alternative('a2', 'a2')
a3 = alternative('a3', 'a3')
a4 = alternative('a4', 'a4')
a5 = alternative('a5', 'a5')
a6 = alternative('a6', 'a6')
a7 = alternative('a7', 'a7')
a = alternatives([ a1, a2, a3, a4, a5, a6, a7 ])

# Performance table
p1 = alternative_performances('a1', {'prix': 120, 'transport':  284, 'envir': 5, 'residents': 3.5, 'competition': 18})
p2 = alternative_performances('a2', {'prix': 150, 'transport':  269, 'envir': 2, 'residents': 4.5, 'competition': 24})
p3 = alternative_performances('a3', {'prix': 100, 'transport':  413, 'envir': 4, 'residents': 5.5, 'competition': 17})
p4 = alternative_performances('a4', {'prix':  60, 'transport':  596, 'envir': 6, 'residents': 8.0, 'competition': 20})
p5 = alternative_performances('a5', {'prix':  30, 'transport': 1321, 'envir': 8, 'residents': 7.5, 'competition': 16})
p6 = alternative_performances('a6', {'prix':  80, 'transport':  734, 'envir': 5, 'residents': 4.0, 'competition': 21})
p7 = alternative_performances('a7', {'prix':  45, 'transport':  982, 'envir': 7, 'residents': 8.5, 'competition': 13})
pt = performance_table([ p1, p2, p3, p4, p5, p6, p7 ])

# FIXME: Reference actions
b1 = {'prix': 100, 'transport': 1000, 'envir': 4, 'residents': 4, 'competition': 15}
b2 = {'prix':  50, 'transport':  500, 'envir': 7, 'residents': 7, 'competition': 20}

# FIXME: Indifference, Preference and Veto
q = threshold_old('q', 'indifference',  {'prix': 15,  'transport':  80, 'envir': 1, 'residents': 0.5, 'competition': 1})
p = threshold_old('p', 'preference', {'prix': 40, 'transport': 350, 'envir': 3, 'residents': 3.5, 'competition': 5})
v = threshold_old('v', 'veto', {'prix': 100, 'transport': 850, 'envir': 5, 'residents': 4.5, 'competition': 8})

# FIXME: Profiles
prof1 = profile('p1', 'profile_down', b1, q, p, v)
prof2 = profile('p2', 'profile_up', b2, q, p, v)
profiles = [ prof1, prof2 ]

# Reference actions
b1 = alternative('b1')
b2 = alternative('b2')
b = alternatives([b1, b2])

# Performance table of reference actions
pb1 = alternative_performances('b1', {'prix': 100, 'transport': 1000, 'envir': 4, 'residents': 4, 'competition': 15})
pb2 = alternative_performances('b2', {'prix':  50, 'transport':  500, 'envir': 7, 'residents': 7, 'competition': 20})
ptb = performance_table([pb1, pb2])

# Indifference threshold
q_prix = threshold('q', 'indifference', constant('q1', 15))
q_transport = threshold('q', 'indifference', constant('q2', 80))
q_envir = threshold('q', 'indifference', constant('q3', 1))
q_residents = threshold('q', 'indifference', constant('q4', 0.5))
q_competition = threshold('q', 'indifference', constant('q5', 1))

# Preference threshold
p_prix = threshold('p', 'preference', constant('p1', 40))
p_transport = threshold('p', 'preference', constant('p2', 350))
p_envir = threshold('p', 'preference', constant('p3', 3))
p_residents = threshold('p', 'preference', constant('p4', 3.5))
p_competition = threshold('p', 'preference', constant('p5', 5))

# Veto threshold
v_prix = threshold('v', 'veto', constant('v1', 100))
v_transport = threshold('v', 'veto', constant('v2', 850))
v_envir = threshold('v', 'veto', constant('v3', 5))
v_residents = threshold('v', 'veto', constant('v4', 4.5))
v_competition = threshold('v', 'veto', constant('v5', 8))

# Thresholds by criterion
prix.thresholds = thresholds([q_prix, p_prix, v_prix])
transport.thresholds = thresholds([q_transport, p_transport, v_transport])
envir.thresholds = thresholds([q_envir, p_envir, v_envir])
residents.thresholds = thresholds([q_residents, p_residents, v_residents])
competition.thresholds = thresholds([q_competition, p_competition, v_competition])

# Lambda
lbda = 0.75

# Alternatives affectations
aap1 = alternative_affectation('a1', 2)
aap2 = alternative_affectation('a2', 1)
aap3 = alternative_affectation('a3', 2)
aap4 = alternative_affectation('a4', 3)
aap5 = alternative_affectation('a5', 1)
aap6 = alternative_affectation('a6', 2)
aap7 = alternative_affectation('a7', 2)
aap = alternatives_affectations([aap1, aap2, aap3, aap4, aap5, aap6, aap7])

aao1 = alternative_affectation('a1', 2)
aao2 = alternative_affectation('a2', 3)
aao3 = alternative_affectation('a3', 2)
aao4 = alternative_affectation('a4', 3)
aao5 = alternative_affectation('a5', 2)
aao6 = alternative_affectation('a6', 2)
aao7 = alternative_affectation('a7', 2)
aao = alternatives_affectations([aao1, aao2, aao3, aao4, aao5, aao6, aao7])

# FIXME: Affecations
affect_p = {'a1': 2, 'a2': 1, 'a3': 2, 'a4': 3, 'a5': 1, 'a6': 2, 'a7':2}
affect_o = {'a1': 2, 'a2': 3, 'a3': 2, 'a4': 3, 'a5': 2, 'a6': 2, 'a7':2}
