Welcome to this Online Shoppers Purchasing Intention Dataset Study.

Our goal for this analysis is to figure when someone is most likely to buy on a website.

Here is a description of all the different variables found on the dataset description : 
"Administrative", "Administrative Duration", "Informational", "Informational Duration", "Product Related" and "Product Related Duration" represent 
the number of different types of pages visited by the visitor in that session and total time spent in each of these page categories. 
The values of these features are derived from the URL information of the pages visited by the user and updated in real time when a user takes an action, 
e.g. moving from one page to another. The "Bounce Rate", "Exit Rate" and "Page Value" features represent the metrics measured by "Google Analytics" 
for each page in the e-commerce site. The value of "Bounce Rate" feature for a web page refers to the percentage of visitors 
who enter the site from that page and then leave ("bounce") without triggering any other requests to the analytics server during that session. 
The value of "Exit Rate" feature for a specific web page is calculated as for all pageviews to the page, the percentage that were the last in the session. 
The "Page Value" feature represents the average value for a web page that a user visited before completing an e-commerce transaction. 
The "Special Day" feature indicates the closeness of the site visiting time to a specific special day (e.g. Mother’s Day, Valentine's Day) in which 
the sessions are more likely to be finalized with transaction. The value of this attribute is determined by considering the dynamics of e-commerce 
such as the duration between the order date and delivery date. For example, for Valentina’s day, this value takes a nonzero value between February 2 and February 12, 
zero before and after this date unless it is close to another special day, and its maximum value of 1 on February 8. The dataset also includes 
operating system, browser, region, traffic type, visitor type as returning or new visitor, a Boolean value indicating whether the date of the visit is weekend, and month of the year.

After studying the corellation between the studied attribute and all different variables, 
we found out that the most important value to study to have an accurate prediction is the page values.
However, this value doesn't have an impact if it is low, but only when it reaches high values :
A page value over 100 almost guarantees a positive result. To be more safe one can choose a page value of 150.

Below this, there are both positive and negative results, so we cannot draw any conclusion.
All the other variables don't really draw any positive result, thought the "Special Day" variable does seem
like it should have an impact, it doesn't really because there are so many positive results without this variable = TRUE.