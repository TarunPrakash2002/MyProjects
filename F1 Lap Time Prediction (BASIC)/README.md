This was my first hands-on project working with F1 data — I wanted to combine 
my interest in F1 with applied machine learning before taking on something more 
complex. It's intentionally scoped as a foundational project: real telemetry 
data, proper leakage handling, and a comparison across three model types.
More advanced F1-based projects are planned as follow-ups in the future, building on what this project taught 
me about feature validation and generalization testing.

I have attached the python file which I used to import the F1 data. I have also attached the scaler pickle file on which I performed the feature scaling. And finally I have attached the 2021 F1 dataset I imported and used for my project.

## NOTE
This is a first, complete version of the lap time prediction model. I identified 
a generalization limitation (see conclusion section) while testing the model 
against unseen races, and traced it to race-identity acting as a shortcut. 
Fixing this properly would mean re-engineering the race feature into actual 
track characteristics (track length, corner count, etc.) rather than one-hot 
race identity — which I'm scoping as a separate follow-up project rather than 
extending this one indefinitely.
