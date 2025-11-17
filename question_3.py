"""
2. Forecasting. For this problem, use cambridge.csv or cambridge.dta. The file contains
monthly means of daily maximum temperature (variable maxtemp) in Cambridge, from January
1959 up to September 2018. For example, in September 2018, the average maximum daily
temperature in Cambridge was 19.9 degrees of Celsius.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_stata("cambridge.dta")
print(data.head())
print(data.info())

"""(a) Make a time series plot of maxtemp. Summarize the behavior of these time series. Plot
the correlogram of maxtemp. Comment.
"""

"""
(b) Run the regression of maxtemp on the month dummies (don’t fall into the dummy variable
trap!). How would you interpret the coeﬃcients? Save the residuals from this regression
as variable res.
"""

"""
(c) Make a time series plot of res. Any signs of global warming? Plot a correlogram of res.
Comment.
"""

"""
(d) Regress res on variable t, which indexes time, and a constant. Save the residuals as
variable res1. Plot a correlogram of res1. Compare with the correlogram of res. Can
you explain the diﬀerence?
"""

"""
(e) Estimate an AR(1) model for res1. Test hypothesis of no AR(1) serial correlation in the
errors of this model.
"""


"""
(f) Given your estimates in (b-e), what is your forecast of the mean daily maximum temper-
ature in Cambridge in February 2018?
"""
