# Group Meeting 2019-12-03

1. Motivate the work (what is your work about and why is it important)
2. Explain what is the problem (a problem is an important thing to solve that has not been solved before or poorly solved by prior work). Here you may also need to explain why solving this problem is important
3. Explain why this problem is challenging
4. Explain your solution idea/approach
5. Explain technical details of your solution (do not forget to explain the **insights behind your steps and ideas**)
6. Explain how you want to evaluate your solution (this is more for the purpose of our group meeting)
7. Explain your experiment's design
8. Present your results. **Tell us what you see, why you see it, and what you learned from it**.
9. Summarize what you have done and takeaway messages: **What should we learn from what you have done**

Answers:

1. Scheduling algorithms are important, otherwise bad things can happen. With multicore platforms the use of threads and communication between them is quite common. In order to make sure that the threads can communicate between them we use **gang scheduling** so we launch all the threads of a task at once. When considering gang scheduling we can have rigid, moldable or malleable gangs.

   There's also the concept of elastic scheduling where each task can have a elastic coefficient and a minimum and maximum time interval and the tasks' release interval are adjusted according to the elasticity and the deadline misses.

2. We want to join the concept of elastic scheduling into gangs. However, instead of doing it adapting the release time period we want to do it with the number of cores and the execution time, as we know that more cores usually reflects in less execution time. We also want to do a response-time analysis of the proposed solution like we are already doing with the fixed priority case.





