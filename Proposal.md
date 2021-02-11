# Dolphyn Small Business Insights

Team: Math Majors Unite  
  
Members: Georgia Channing, Harry Channing, Owen Queen, Shannon Hall

## Introduction

  Machine learning has become an increasingly prevalent tool in business from product recommendations to user feedback interpretation.  Most of the organizations that moved quickly to integrate machine learning techniques into their workflows had the resources to hire machine learning engineers and data scientists to turn their data into actionable insights.  Hiring machine learning engineers and data scientists is expensive, and is out of reach for most small and medium businesses.  That doesn’t mean that they shouldn’t be able to leverage machine learning to improve their businesses and make their lives easier.  Enter Dolphyn: a one-stop shop for interpreting large scale customer feedback.  Machine learning shouldn’t be monopolized by Fortune500 companies, but should be available to small and medium businesses, who now more than ever need all the support they can get [1].  

  While there exist lots of plug-and-play machine learning libraries, such as Keras, sci-kit learn, and TensorFlow, even the small amount of coding necessary to get models up and running is a barrier to entry.  Our product will smooth the path to integrating machine learning into small business workflows by creating an easy-to-use interactive web platform. Our product will cut down on the overhead needed for the preprocessing steps of machine learning, and it will ideally give small businesses the tools they need to incorporate machine learning into their business development.  

  Our team has varying degrees of experience with machine learning and the preprocessing steps that we will need to implement. We are all fairly new to web application development, so creating both a front and back end for a web application will be a big part of our project and a big learning experience overall. All team members have experience with the Python programming language, which is what we will primarily use for the project through the Django library. We expect that the mixture of math, computer science, and business backgrounds within our team will help us to successfully implement the features that we will need, all the while focusing on the needs of our potential clients.

## Customer Value

  The primary customer of this software would be small-medium businesses (SMBs). Small businesses usually have lots of data to work with but don’t have the budget to outsource the processing and cleaning of their data. Since these businesses don’t have the time or budget to understand how to do that, they need to have an accessible way to leverage their data. We aim to implement a program with an intuitive user interface that can help to efficiently and accurately take care of a large part of their data science workflows.  
  
  From the point of view of the consumer, our solution will create opportunity for technically non-savvy computer users to interact with data management and analysis. In the all-to-near future, companies that can’t effectively leverage the data that they have on hand won’t be able to compete with those that can. This is a particular issue for SMBs that compete with larger corporations that can wildly outspend them to employ qualified data scientists. Our product will mitigate the fear many lay people have of actively learning to code and allow even the least tech-savvy of business owners to leverage their data. We provide the opportunity to use state-of-the-art machine learning tools without the high entry cost of learning to code.
  
  The upside of this implementation is that it will be relatively easy to make sure the backend is effective. Frequently, there are relatively few lines of code that need to be written after understanding the user’s goal. That being said, the goal to make sure that the GUI is easily understandable can be harder to track. We can hope to do our best and use our non-CS peers to get frequent target user feedback. We will also be able to identify some of our own problems as we go.


## Technology

  This software will provide a user-friendly interface to machine learning (ML) tools available through libraries such as SciKit-Learn, TensorFlow, and PyTorch. From a developer’s standpoint, our project is essentially a wrapper to these libraries, so the bulk of our work will be done in providing interface from Django to the ML libraries.  
  
  Our system can be thought of as front-end and back-end components. In the front-end component, our website will feature a polished GUI that allows users to easily process and analyze their data. In the back-end component, our system will perform preprocessing and analysis tasks by leveraging state-of-the-art ML models. The front-end will serve as a friendly interface to the power of the back-end implementation, and a key portion of our project will be the integration of front-end and back-end components to achieve a seamless user experience.  
  
  To test our system, we will feed in common datasets, such as those from Kaggle, that we can use as a demonstration of how our system operates. Using our system, we will attempt to build ML models that analyze this data, performing various classification and/or regression tasks. These sorts of tasks will mimic the use-cases that one of customers might have for our product.  
  
  The project will be implemented primarily in Python, but it may require other web development tools, such as Javascript, HTML, or CSS. We will implement the front-end component in Django, a web framework implemented in Python. The back-end will be implemented in various ML libraries such as Scikit-Learn, TensorFlow, and PyTorch. To perform data preprocessing, we may need to incorporate other classic data science libraries such as Pandas and Numpy.
  
<p align = "center">
  <img src="https://github.com/CS340-21/MathMajorsUnite/blob/main/block_diagram.png">
</p>


## Team

  No team members have built something like this before, at least in the sense that no member has created a similar web application. All members of the team are to some degree familiar with Python and machine learning concepts, as most have worked on projects involving machine learning in the past.  None of the team members are familiar with Django, but we expect that our knowledge of Python will help us learn Django quickly.  One of our team members, Harry, double majors in Business and can frame particular issues of small businesses that we collectively will try to solve.  
  
  All members of the team will at some point “drive” the project, and all members of the team will code significant portions of the overall project.  Georgia will primarily focus on backend design, Harry will focus on user use-cases, and Owen and Shannon will work primarily on the front end design.  All of these roles will overlap, but the above description is a rough sketch of the division of labor.  
  
Owen: Owen has worked with Python for two years, and he has built multiple machine learning models involving image and tabular data. He does not have experience with Django, but he is looking to build his skills in website development with this framework.  

Shannon: Shannon has worked with Python for about two years for various classes and projects. He has less experience with projects involving machine learning and web development, although he has worked briefly with both in the past.  

Harry: Harry has little experience in Python (only CS 425) and none in Django, but has had experience putting together ML tools through CS 425 and implementing them for an autism classification research project. This can be helpful in the iterative steps, creating additional possibilities for the outcome of the project.

Georgia: Georgia has extensive experience in Python. She wrote her Bachelor's thesis in ML for Healthcase based in Python and SQL and now works full-time coding in Python. She has no Django experience, but is excited to branch out into front-end development.


## Project Management

  The design of our product was created with special attention to the time constraints of a single semester class.  Our minimal viable product is indeed quite small and the bulk of our subsequent development will be for iterative feature addition and refinement.  
  
  We will meet synchronously and over Zoom approximately once a week to discuss further development, divide responsibilities, and rotate the “driver”.  We will also discuss over text in the interim periods.  
A tentative schedule for our project is shown below:

| Week                | Goals                                                                                                                           |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------|
| 02/07/21 - 02/13/21 | - Create rough project proposal                                                                                                 |
| 02/14/21 - 02/20/21 | - Finish up project proposal                                                                                                    |
| 02/21/21 - 02/27/21 | - Establish web framework for development<br>- Basic implementation of processing technique                                     |
| 02/28/21 - 03/06/21 | - 3/04: Submit Iteration 1 Status Report<br>- Implement at least one processing technique<br>- Establish basic user interaction |
| 03/07/21 - 03/13/21 | - Further implementation of processing techniques<br>- Developing machine learning framework                                    |
| 03/14/21 - 03/20/21 | - 3/18: Submit Iteration 2 Status Report<br>- Implement at least one classification algorithm                                   |
| 03/21/21 - 03/27/21 | - Clean up and improve processing technique<br>- Add processing techniques<br>- Add machine learning tools                      |
| 03/28/21 - 04/03/21 | - 4/01: Submit Iteration 3 Status Report<br>- Clean up design, improve GUI                                                      |
| 04/04/21 - 04/10/21 | - Work towards final report, presentation<br>- Test processing techniques<br>- Improve and test GUI                             |
| 04/11/21 - 04/17/21 | - 4/15: Present Final Project<br>- 4/15: Finish Final Report                                                                    |

  As far as we are aware, there are no legal or ethical constraints on our product. The only ethical or social concerns that may arise from our project are the inherent ethical concerns related to machine learning. However, we will not seek to remedy these extensive concerns in our project, and we will rely on state-of-the-art machine learning tools. We do not yet have a fixed data source, but we are confident that we will be able to find sample data to do the first iterations of our product. All of the data that we use on this project will be open-sourced.  

  This project has the potential to become a robust system that is incredibly marketable, but in the case that we need to descope this project, we will still be able to produce a viable system that is useful to our customer base. If full functionality cannot be achieved, this project will serve as a data preprocessing tool for our customers. This tool will still be beneficial, allowing customers to avoid complicated data engineering tasks when processing their data. While this descoped version of our project will not provide end-to-end functionality, it will at least provide some of the path required for ML tasks, removing a barrier our customers might face when implementing ML in their small businesses.

## Sources

[1] "14 Smart Ways To Leverage Machine Learning For Small Businesses," Forbes, 2-10-21. [Online]. Available:  https://www.forbes.com/sites/forbestechcouncil/2020/09/24/14-smart-ways-to-leverage-machine-learning-for-small-businesses/?sh=6135b65b3e79
