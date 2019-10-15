'''
Question:
You are on a flight and wanna watch two movies during this flight.
You are given List<Integer> movieDurations which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).

Input: movieDurations = [90, 85, 75, 60, 120, 150, 125], d = 250
Output: [0, 6]
Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215 is the maximum number within 220 (250min - 30min)

Find the pair of movies with the longest total duration and return they indexes. If multiple found, return the pair with the longest movie.
'''
def pair_movie(movies, time):

  idx_value_list = [[x, y] for x,y in zip(range(len(movies)), movies)]
  idx_value_list.sort(key = lambda x:x[1])

  left, right = 0, len(movies) - 1
  target = time - 30
  IDX, VALUE = 0, 1
  res = []
  max_pair_duration = -float("inf")

  while left <= right:
    curr_pair_duration = idx_value_list[left][VALUE] + idx_value_list[right][VALUE]
    if  curr_pair_duration > target:
      right -=1
    elif curr_pair_duration > max_pair_duration:
      max_pair_duration = curr_pair_duration
      res = [idx_value_list[left][IDX],idx_value_list[right][IDX]]
    elif curr_pair_duration == max_pair_duration and movies[res[1]] < idx_value_list[right][VALUE]:
      res = [idx_value_list[left][IDX],idx_value_list[right][IDX]]
    else:
      left +=1
  
  return res

movies = [90, 85, 75, 60, 120, 150, 125]
time = 250
print(pair_movie(movies, time))
