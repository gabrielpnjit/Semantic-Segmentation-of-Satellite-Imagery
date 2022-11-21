# BOHO Hyperparameter Optimization on The Semantic Segmentation
Images of the BOHO application
>![image](https://user-images.githubusercontent.com/89927101/202970326-d4018f48-0607-47da-92c7-7f5c760dcc9d.png)
>![image](https://user-images.githubusercontent.com/89927101/202970358-3c314b88-20d8-4c6b-bcbe-af6c6cb20d92.png)
>![image](https://user-images.githubusercontent.com/89927101/202970392-5e2d03a6-564e-4679-ba40-8297cb8327d8.png)
>![image](https://user-images.githubusercontent.com/89927101/202970411-7bbe5e7f-f9d7-4294-b2a5-72b5452592d2.png)
>![image](https://user-images.githubusercontent.com/89927101/202970452-a092abf3-850f-402e-8993-bae59e01e733.png)
>![image](https://user-images.githubusercontent.com/89927101/202970467-fee5ee32-1124-4200-b08f-366550fbfaf1.png)
>![image](https://user-images.githubusercontent.com/89927101/202970485-8eb54ad4-c6d1-4db4-b1b1-f3d64eba9a1a.png)
>![image](https://user-images.githubusercontent.com/89927101/202970500-7822a96b-8c80-4765-ac69-8c415dbef413.png)
>![image](https://user-images.githubusercontent.com/89927101/202970509-1740dbb7-c59d-46fc-a0b7-7c55222ff0ad.png)
>![image](https://user-images.githubusercontent.com/89927101/202970525-33a7480d-a619-4a43-8d04-054f18de59d5.png)
>![image](https://user-images.githubusercontent.com/89927101/202970536-c0409b11-d972-4598-be53-9578d08e8945.png)
>![image](https://user-images.githubusercontent.com/89927101/202970554-b83972d2-c330-402a-b59a-733d28bc4f12.png)
>![image](https://user-images.githubusercontent.com/89927101/202970562-0f815470-2516-4c5d-b171-bbf551fb42f7.png)
>>**WE WERE ONLY ABLE TO RUN IT WITH 5 EPOCHS, RAN INTO A MEMORY AND PEFORMACE ISSUES RUNNING IT LOCALLY**
## What is BOHO?
>BOHO is the combination of the bayesian optimization and hyperband optimization, and the reason for the combination is 
> to gain the benefits both optimzations offer. The Bayesian optimization has the benefit of using prior knowledge since the
> bayesian works with data that is given while being very data efficient and another benefit is that is semi-paralleizable.
The Hyperband optimization has the benefits of being able to be easily parallelizable and it removes bad values, as well as including the 
>successive halving method which helps with the budgeting, so it keeps the best halves and keeps removing the worse halves, and continues
>for each iteration. When these two optimizations combine, they provide a stronger and better hyperparameter optimization algorithim which 
>makes it the most robust, flexible, and scalable.
