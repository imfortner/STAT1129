
# Question 1
matrix1 <- matrix(c(7,2,9,4,12,13), nrow=2, ncol=3)
matrix1
matrix2 <- matrix(c(1,2,3,7,8,9,12,13,14,19,20,21), nrow=3, ncol=4)
matrix2
matrix1 %*% matrix2
# Question 2 Part A
data <- data.frame(
  id = c(1,2,3,4,5),
  name = c("Peter", "Amy", "Ryan", "Gary", "Michelle"),
  salary = c(623.30,515.20,611,729,843.25)
)
data
# Part B
new_col_df <- cbind(data, department = c("Human Resources","Front Office Admin", "IT", "Leadership", "Security"))
new_col_df
# Part C Extract 1st, 3rd, and 5th rows, with 2nd and 3rd columns, 
# using c function. (3 points).
result = new_col_df[c(1,3,5), c(2,3)]
result
# Part D
x <- c("Peter","Gary", "Michelle")
y <- c(623.30,729.00,843.25)
barplot(y, names.arg = x, xlab = "employee", ylab = "salary")
# Part E plot a bar chart to show the salary of row 1,4,5 and label the bar with people’s name correspondingly.
summary(data)
mylabel <- c("Amy", "Michelle", "Peter")
colors <- c("pink", "purple", "turquoise")
x <- c(515.2,843.2,623.3)
pie(x, label = mylabel, main = "Pie Chart for Min, Max, and Medium Salary", col = colors)
legend("bottomleft", mylabel, fill = colors)
# Question 3  Pick two functions in your final project, transfer that into R programming. 
# One function should involve “if else” (4 points), the other function should involve “for loop or while loop” (4 points).
Rockpaperscissors <- function (your_choice = c('rock','paper','scissors')){
  Y <- your_choice
  R <- sample(c('rock','paper','scissors'),1)
  if (Y == "rock" && R == "scissors"||
      Y == "scissors" && R == "paper"||
      Y == "paper" && R == "rock"){
    print ("You win!")
  } else if (R == "rock" && Y == "scissors"||
             R == "scissors" && Y == "paper"||
             R == "paper" && Y == "rock"){
    print ("You lose!")
  } else {
    print('Its a tie!')}
    while(Y== "quit")
      {
      print("game ended")
      if (Y == "rock" && R == "scissors"||
          Y == "scissors" && R == "paper"||
          Y == "paper" && R == "rock"){
        break
    }
    }
}
Rockpaperscissors("rock")
Rockpaperscissors("paper")









    
    
    
  