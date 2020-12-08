# Question:
# Any experience to handle N+1 query in GraphQL

# Answer:
# No I don't have. But I have a little clue.

## N + 1 query is about when query has relationship in there.
## Query books data and its author data. 
## If books number is five, server may fetch database five times to access every book's author.
## One solution is create a dataloader store all the books id in an array, then fetch database one time.
##
## Downside of dataloader is you has to create a dataloader for one data relationship.
## 
## But it still can reduce the times of fetching database by JOIN.
## Create a dataloader go through whole query's info, then fetch database one time.

### Note:
### https://www.youtube.com/watch?v=uCbFMZYQbxE&ab_channel=BenAwad
### https://medium.com/the-marcy-lab-school/what-is-the-n-1-problem-in-graphql-dd4921cb3c1a