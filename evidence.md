# Nexus lab evidence

## Contributors and participation
Names; who typed, traced behavior, designed or checked tests. Ad hoc groups are fine.

## Baseline
Pinned upstream: 75a8d145aa5bc0c92725197c0e4e9883491c542f.
Interpreter/version, command, actual output. Expected starter: four passes, four failures.

## Our design decision
Audit owner and interface; ordering; one credible alternative; accepted benefit/cost.

## Actual changes
Changed files/functions. What is implemented versus still proposed?
Explain the sanctioned original notification-test expectation change.

## Our added behavior check
Conditions, action, expected observable result and reason for choosing it.

## Final execution evidence
Command and actual output. Separate the lab runner from the original pytest suite.
If a command was not run, say so. Preserve remaining failures and their meaning.

## Limitations and next step
What do the results not establish? What would you check next?

## Individual PR starting points
Each person separately: initial claim, consequential challenge, current disposition.
Copy the shared code/evidence before leaving. No submission is due at class end.



Where does the audit entry live?  

CustomerLifecycleService 
In the deactivate function 

What operation records it, and who calls it? 

Operation- save() 

Who- repository 

When is it recorded relative to public publication? 

Between events and verification 

What cost does your choice introduce? 

 

 

[("case@example.com", "Your Atlas account has been deactivated. " + SECRET)]) 

Reason: The person should be notified of the reason of there deactivation, but then the reason should be deleted after. 