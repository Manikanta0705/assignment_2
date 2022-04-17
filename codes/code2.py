'''problem :- Given three identical Boxes A, B and C, Box A contains 2 gold and 1 silver coin, Box B contains 1 gold and 2 silver coins and
    Box C contains 3 silver coins. A person chooses a Box at random and takes out a coin . If the coin drawn is of silver, find the 
    probability that it has been drawn from the Box which has the remaining two coins also of silver.'''

'''SOLUTION:-
 given,
  P(A)=1/3,P(B)=1/3,P(C)=1/3
  P(S/A)=1/3,P(S/B)=2/3,P(S/C)=1,

  P(C/S)=??'''

p_a = 1/3
p_b = 1/3
p_c = 1/3
p_s_a = 1/3
p_s_b = 2/3
p_s_c = 1

x = (p_c) * ( p_s_c)
y = (p_a * p_s_a) + (p_b * p_s_b) + (p_c * p_s_c)
                                     
p_c_s = x/y

print('P(A|B) =', p_c_s)
