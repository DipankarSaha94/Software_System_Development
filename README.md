# SSD Assignment 3a

## GitHub link
* `https://github.com/DipankarSaha94/SSDAssignment3`

## Question 1

* I have assumed user input i.e. Emp id of two employee will be given as space seperated.

## Question 2

* I have considered input will be given one line by another without using `Date1:` , simply `10th September, 2020` and next line `11th September, 2020`. And the input Date2 will be `greater or equal to` input Date1.

* Output will be simply date difference i.e. without `Date Difference:`, only 1 Day.

* Considered date input format is `DD/MM/YYYY` , `DD.MM.YYYY` , `DD-MM-YYYY` , `1st Oct, 2020` , `13th october, 2020`.

## Question 3

* I have assumed date in both the text files will be same. And user input will be given as float format like .5 , 1.5 , 6.

# SSD Assignment 3b

## GitHub link
* `https://github.com/DipankarSaha94/SSDAssignment3`

## Question 1

* For part a i was checking in two parent list of given employee and returning the result, here i am checking based on the number of employee given in the input i.e. from 3 to 5. The first returned common parent for all the given Employee wil be the answer in this case.

* No of lines added in the code is from change 80 to 300.

## Question 2

* I am taking input date format from user and it can be of any format like `dd.mm.yyyy` or `mm/dd/yyyy` or `yyyy-dd-mm` any combination possible. And the answer will be written as no of days difference in the output file. I am going through the input and setting the position for day, month , year and checking the input file format based on that. If it is in format `1st Oct, 2020` then the input should be blank and of size less than 9.

* No of lines added in the code is from 145 to 160.

## Question 3

* Here i am reading all the 5 text files containing employee time schedule and giving output as per the input given by the user like if 4 employee to consider the input will be `3 .5` i.e. no of employee to consider is 4 and common time required is 30 min. For each Employee i am generating the free slots and later on checking all the free slots to find the common available slot.

* No of lines added in the code is from 170 to 220 and 280 to 310. 

# SSD Assignment 3c

## GitHub link
* `https://github.com/DipankarSaha94/SSDAssignment3`

## Question 1

* The function `answer` is divided into 5 different functions as `answer`,`getplist`,`findleader1`,`findleader2`,`findleader3` and used lambda function instead of multiple if else loop to achieve the complexity A.

## Question 2

* I have reduced the multiple if else loop by help of a list check in `changeformat` function. And divide the function `getDifference` into 2 function `getDifference`,`noofdays` to do the repetitive task to achieve the ideal complexity A.

## Question 3

* have deleted the repetitive part in `addtime` function by reducing the argument passed into it, to get the final complexity A. 
