#GPT Learning hub Gradient decent algo for f(x) = x^2

class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        if iterations == 0:
            return init
        d = 0 
        curr_guess = float(init)
        for i in range (iterations):
            d = 2 * curr_guess 
            curr_guess = curr_guess - (d * learning_rate)
        curr_guess = round(curr_guess, 5)
        return curr_guess

    